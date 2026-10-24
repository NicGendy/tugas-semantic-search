from contextlib import asynccontextmanager
from typing import Dict, List, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams
from sentence_transformers import SentenceTransformer

from data import DOCUMENTS, validate_dataset

# Konstanta eksplisit
MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
EXPECTED_VECTOR_SIZE = 384
QDRANT_PATH = "qdrant_data"
COLLECTION_NAME = "semantic_search_collection"


class AppResources:
    model: Optional[SentenceTransformer] = None
    qdrant: Optional[QdrantClient] = None

resources = AppResources()

def ensure_collection_exists(client: QdrantClient, collection_name: str, vector_size: int) -> None:
    existing_collections = [col.name for col in client.get_collections().collections]
    if collection_name not in existing_collections:
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

@asynccontextmanager
async def lifespan(app: FastAPI):
    resources.model = SentenceTransformer(MODEL_NAME)

    # Sanity check dimensi embedding model
    test_vector = resources.model.encode("sanity_check")
    actual_dim = int(test_vector.shape[0])
    if actual_dim != EXPECTED_VECTOR_SIZE:
        raise RuntimeError(
            f"Dimensi model ({actual_dim}) tidak sesuai dengan ekspektasi ({EXPECTED_VECTOR_SIZE})."
        )

    resources.qdrant = QdrantClient(path=QDRANT_PATH)
    ensure_collection_exists(resources.qdrant, COLLECTION_NAME, EXPECTED_VECTOR_SIZE)

    yield

    if resources.qdrant is not None:
        resources.qdrant.close()

app = FastAPI(
    title="Semantic Search API",
    description="Aplikasi pencarian berbasis kemiripan makna menggunakan FastAPI, SentenceTransformers, dan Qdrant.",
    version="1.0.0",
    lifespan=lifespan,
)

# Skema Request & Response
class IndexResponse(BaseModel):
    message: str
    indexed_count: int
    categories: List[str]

class SearchRequest(BaseModel):
    query: str = Field(..., min_length=2, description="Kalimat pencarian dari pengguna")
    top_k: int = Field(default=3, ge=1, le=20, description="Jumlah hasil teratas yang diambil")

class SearchResultItem(BaseModel):
    text: str
    category: str
    score: float

class SearchResponse(BaseModel):
    query: str
    results: List[SearchResultItem]

@app.get("/health")
def health() -> Dict[str, str]:
    if resources.model is None or resources.qdrant is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Model atau database belum siap.",
        )
    return {"status": "OK"}

@app.post("/index", response_model=IndexResponse)
def index_dataset() -> IndexResponse:
    if resources.model is None or resources.qdrant is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Resource aplikasi belum terinisialisasi.",
        )

    try:
        validate_dataset(DOCUMENTS)
    except ValueError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(err),
        ) from err

    texts = [doc["text"] for doc in DOCUMENTS]
    embeddings = resources.model.encode(texts, show_progress_bar=False)

    points: List[PointStruct] = []
    categories_set = set()

    for idx, (doc, vector) in enumerate(zip(DOCUMENTS, embeddings)):
        categories_set.add(doc["category"])
        points.append(
            PointStruct(
                id=idx + 1,
                vector=vector.tolist(),
                payload={
                    "text": doc["text"],
                    "category": doc["category"],
                },
            )
        )

    resources.qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
    )

    return IndexResponse(
        message="Dataset berhasil di-index ke Qdrant.",
        indexed_count=len(points),
        categories=sorted(list(categories_set)),
    )

@app.post("/search", response_model=SearchResponse)
def search_documents(request: SearchRequest) -> SearchResponse:
    if resources.model is None or resources.qdrant is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Resource aplikasi belum terinisialisasi.",
        )

    cleaned_query = request.query.strip()
    if not cleaned_query:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Query pencarian tidak boleh hanya berisi spasi kosong.",
        )

    collection_info = resources.qdrant.get_collection(COLLECTION_NAME)
    if collection_info.points_count == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Collection masih kosong. Jalankan endpoint POST /index terlebih dahulu.",
        )

    query_vector = resources.model.encode(cleaned_query).tolist()

    # Menggunakan query_points (API standar Qdrant terbaru)
    search_result = resources.qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=request.top_k,
    )

    formatted_results: List[SearchResultItem] = []
    for hit in search_result.points:
        payload = hit.payload or {}
        formatted_results.append(
            SearchResultItem(
                text=str(payload.get("text", "")),
                category=str(payload.get("category", "")),
                score=round(float(hit.score), 4),
            )
        )

    return SearchResponse(
        query=cleaned_query,
        results=formatted_results,
    )
    
# Semantic Search & Vector Database

## Project Information

**Nama Project:**

AI Concept Semantic Search

**Tema Dataset:**

AI Concept

**Deskripsi Singkat:**

Aplikasi ini adalah API pencarian berbasis *Semantic Search* yang dibuat pakai `FastAPI`, `sentence-transformers`, dan `Qdrant`. Cara kerjanya, sistem bakal memeriksa *dataset* berisi dokumen *AI Concept*, mengubah teks jadi *vector embedding* 384-dimensi memakai model `paraphrase-multilingual-MiniLM-L12-v2`, lalu menyimpannya ke dalam *database* `Qdrant`. Dari situ, pengguna bisa mencari dokumen yang relevan secara semantik menggunakan hitungan *Cosine Similarity* lewat *endpoint* API yang sudah disediakan.

Aplikasi ini adalah API pencarian berbasis *Semantic Search* yang dibuat pakai `FastAPI`, `sentence-transformers`, dan `Qdrant`. Cara kerjanya, sistem bakal memeriksa *dataset* berisi dokumen *AI Concept*, mengubah teks jadi *vector embedding* 384-dimensi memakai model `paraphrase-multilingual-MiniLM-L12-v2`, lalu menyimpannya ke dalam *database* `Qdrant`. Dari situ, pengguna bisa mencari dokumen yang relevan secara semantik lewat *endpoint* API yang sudah disediakan.

------------------------------------------------------

# Dataset

### Jumlah Data

50

### Kategori yang Digunakan

*   `ai_fundamentals`: Konsep dasar dan fondasi utama dari AI.
*   `machine_learning`: Metode pembelajaran mesin seperti *supervised*, *unsupervised*, dan *reinforcement learning*.
*   `deep_learning`: Jaringan saraf tiruan dan arsitektur berlapis yang kompleks.
*   `data`: Komponen data seperti *dataset*, fitur, label, serta *data preprocessing*.
*   `model_evaluation`: Metrik performa model dan masalah evaluasi seperti *overfitting* atau *underfitting*.
*   `nlp`: *Natural Language Processing* atau *NLP*, *tokenization*, dan model bahasa.
*   `generative_ai`: Teknologi *Generative AI*, *LLM*, *prompt engineering*, dan *RAG*.
*   `computer_vision`: Pengolahan informasi gambar atau visual seperti klasifikasi citra dan deteksi objek.
*   `responsible_ai`: Etika AI, privasi data, bias sistem, dan *explainable AI*.
*   `ai_applications`: Penerapan nyata AI seperti sistem rekomendasi dan deteksi anomali.

### Kenapa kalian memilih dataset tersebut?

Saya memilih *dataset* ini karena memiliki cakupan *domain* yang luas dan struktur taksonomi yang kuat untuk menguji sistem *semantic search*. Setiap dokumen berisi definisi konsep yang padat dan memakai istilah teknis yang saling beririsan antar-kategori seperti contoh kata "data", "model", atau "jaringan saraf" yang muncul di beberapa topik berbeda. Karakteristik teks seperti ini sangat pas untuk membuktikan keunggulan *vector database* dan `sentence-transformers` dalam mengenali konteks dan makna kata secara utuh, bukan sekadar *keyword matching* secara harfiah.

------------------------------------------------------

# Tech Stack

Tuliskan teknologi yang digunakan.

*   **FastAPI**: *Framework* web Python modern berperforma tinggi yang digunakan untuk membuat REST API dengan *endpoint* `/health`, `/index`, dan `/search`, lengkap dengan validasi data otomatis menggunakan `Pydantic`.
*   **Qdrant**: *Vector database* yang digunakan untuk menyimpan *vector embedding* hasil konversi dokumen secara efisien, serta melakukan *similarity search* dalam skala besar.
*   **SentenceTransformers**: *Library* Python yang digunakan untuk memuat model *machine learning* dan mengubah teks biasa menjadi *vector embedding*.
*   **Python Types & Contextlib**: Penggunaan *typing* untuk menjaga kualitas kode melalui *type hinting* serta `asynccontextmanager` lewat *lifespan* untuk mengelola siklus hidup aplikasi dengan menyiapkan model dan koneksi *database* saat awal dijalankan, serta menutup koneksi saat dimatikan.

------------------------------------------------------

# Application Flow

Jelaskan menggunakan bahasa kalian sendiri bagaimana flow berikut bekerja:

Dataset -> Embedding -> Vector -> Qdrant
User Query -> Embedding -> Qdrant Search -> Top-K Results

Penjelasan kalian:

1. Dataset -> Embedding -> Vector -> Qdrant
*   **Dataset**: Sistem memuat daftar dokumen yang berisi pasangan teks definisi AI beserta kategorinya. Data ini divalidasi terlebih dahulu untuk memastikan kelengkapan struktur dan formatnya telah memenuhi syarat.
*   **Embedding**: Teks dari dokumen dimasukkan ke dalam model `SentenceTransformers`. Model ini akan menganalisis makna dari setiap kalimat secara utuh.
*   **Vector**: Model mengonversi teks tersebut menjadi bentuk *vector* angka berdimensi 384. Angka-angka ini merepresentasikan posisi makna teks di dalam ruang multidimensi.
*   **Qdrant**: Vektor-vektor tersebut dibungkus ke dalam objek `PointStruct` bersama dengan data aslinya yakni teks dan kategori sebagai *payload*, lalu disimpan ke dalam koleksi *database* `Qdrant` menggunakan operasi *upsert*.

2. User Query -> Embedding -> Qdrant Search -> Top-K Results
*   **User Query**: Pengguna mengirimkan teks pencarian berupa kata kunci atau pertanyaan bebas melalui *endpoint* API `/search`.
*   **Embedding**: Teks pencarian tersebut dikonversi oleh model `SentenceTransformers` yang sama menjadi satu *vector query* berdimensi 384.
*   **Qdrant Search**: *Vector query* dikirim ke `Qdrant` menggunakan fungsi `query_points`. *Database* akan menghitung skor kemiripan menggunakan metode *Cosine Similarity* antara *vector query* dengan seluruh *vector* dokumen yang telah tersimpan.
*   **Top-K Results**: Qdrant menyaring dan mengurutkan dokumen berdasarkan skor kemiripan tertinggi, lalu mengembalikan sejumlah hasil terbaik—misalnya 3 dokumen teratas—kepada pengguna dalam format JSON yang rapi.

------------------------------------------------------

# Embedding Model

Model yang digunakan:

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

### Menurut kalian, apa fungsi embedding model pada project ini?

1. **Ekstraksi Makna Konseptual**: Model bertugas menangkap konteks dan inti utama dari teks pencarian, bukan sekadar melihat susunan huruf atau kata demi kata secara harfiah.
2. **Menjembatani Kemiripan Semantik**: Karena model ini bersifat *multilingual*, sistem bisa tahu kalau dua kalimat dengan susunan kata berbeda tetap punya arti yang dekat jika membahas topik yang sama.
3. **Standardisasi Dimensi Data**: Model memastikan semua teks, baik panjang maupun pendek, diubah secara teratur menjadi deretan angka dengan panjang tetap 384 dimensi, yang siap diolah dan dicari dengan hitungan matematika cepat di dalam `Qdrant`.

------------------------------------------------------

# Vector Database

### Apa fungsi Qdrant pada aplikasi kalian?

*   **Penyimpanan Vektor Efisien**: Menyimpan *vector embedding* 384 dimensi hasil konversi teks yang merepresentasikan makna dari setiap dokumen.
*   **Komputasi Pencarian Semantik**: Melakukan pencarian kemiripan makna menggunakan metrik *Cosine Similarity* melalui fungsi `query_points`. Hasilnya, proses pencocokan *query* terhadap ribuan dokumen bisa berjalan jauh lebih cepat dibandingkan dengan *database* relasional konvensional.
*   **Manajemen Koleksi Data**: Membuat ruang penyimpanan secara otomatis melalui koleksi bernama `semantic_search_collection` saat aplikasi pertama kali dijalankan.

### Apa saja data yang kalian simpan di payload?

*   **text**: Tipe data `String` yang berisi kalimat *AI Concept* asli yang disimpan saat proses indeksasi.
*   **category**: Tipe data `String` untuk label kelompok topik dari dokumen tersebut—seperti `machine_learning`, `nlp`, atau `deep_learning` untuk mempermudah penyaringan atau pengelompokan konteks hasil pencarian.

------------------------------------------------------

# API Endpoint

Tuliskan endpoint aplikasi kalian.

*   **`GET /health`**: Memeriksa status kesiapan layanan atau *health check*. Digunakan untuk memastikan kalau aplikasi, model *embedding* `SentenceTransformers`, dan koneksi `QdrantClient` sudah siap sepenuhnya buat menerima *request*.
*   **`POST /index`**: Melakukan indeksasi *dataset*. *Endpoint* ini bakal memvalidasi data dokumen, mengonversi teks jadi *vector embedding*, lalu menyimpannya atau *upsert* ke dalam koleksi `Qdrant`.
*   **`POST /search`**: Melayani pencarian semantik. Menerima masukan berupa teks *query* dan parameter `top_k`, lalu mengembalikan daftar dokumen dengan kemiripan makna tertinggi beserta skor kecocokannya.
*   **`GET /docs`**: Menyediakan dokumentasi API interaktif bawaan `FastAPI` yakni Swagger UI untuk menguji seluruh *endpoint* di atas secara langsung lewat *browser*.

------------------------------------------------------

# Example Request

Masukkan salah satu actual request yang kalian gunakan.

{
  "query": "Bagaimana cara mendeteksi benda dalam gambar?",
  "top_k": 3
}

------------------------------------------------------

# Example Response

Masukkan actual response dari aplikasi.

{
  "query": "Bagaimana cara mendeteksi benda dalam gambar?",
  "results": [
    {
      "text": "Deteksi objek menemukan lokasi dan kelas objek di dalam gambar.",
      "category": "computer_vision",
      "score": 0.7519
    },
    {
      "text": "Segmentasi gambar memberikan label pada piksel untuk memisahkan objek atau wilayah gambar.",
      "category": "computer_vision",
      "score": 0.5843
    },
    {
      "text": "Computer vision membantu sistem memperoleh informasi dari gambar dan video.",
      "category": "computer_vision",
      "score": 0.5697
    }
  ]
}

------------------------------------------------------

# Experiment 1 - Semantic Search

## Query 1

**Query:**

Bagaimana cara sistem menemukan objek tertentu beserta lokasinya di dalam sebuah foto?

**Top Result:**

"Deteksi objek menemukan lokasi dan kelas objek di dalam gambar."

**Similarity Score:**

0.8181

**Menurut kalian apakah hasilnya relevan? Kenapa?**

**Sangat Relevan**. Hasil ini membuktikan keunggulan utama dari pencarian semantik. Meskipun *query* memakai kata "foto" dan dokumen menggunakan kata "gambar", model *embedding* berhasil mengenali korelasi makna yang sangat kuat di antara keduanya. Hubungan antara frasa "menemukan objek beserta lokasinya" dengan "menemukan lokasi dan kelas objek" mampu dipetakan dengan tepat, sehingga menghasilkan *similarity score* yang tinggi sebesar 0,8181 di dalam *domain* `computer_vision`.

------------------------------------------------------

## Query 2

**Query:**

Metode apa yang membantu komputer belajar dari percobaan dengan menerima nilai imbalan atau hukuman?

**Top Result:**

"Reinforcement learning melatih agen melalui interaksi dengan lingkungan dan umpan balik berupa reward."

**Similarity Score:**

0.5228

**Menurut kalian apakah hasilnya relevan? Kenapa?**

**Secara Konsep Relevan, Namun Skor Kemiripan Rendah**. Secara substansi materi, dokumen *Reinforcement Learning* merupakan jawaban yang paling tepat untuk konsep "belajar dari percobaan dengan imbalan (*reward*)". Namun, hasil skor kemiripannya tergolong rendah (0,5228). Hal ini terjadi karena model *embedding* kemungkinan mengalami kendala dalam memetakan variasi bahasa Indonesia seperti kata "hukuman" ke dalam teks dokumen asli yang tidak memuat kata tersebut serta adanya perbedaan antara kata "imbalan" pada *query* dengan istilah bahasa Inggris "*reward*" pada dokumen asli.

------------------------------------------------------

## Query 3

**Query:**

Bagaimana cara mengecek apakah rekomendasi yang dibuat model sudah cukup tepat?

**Top Result:**

"Supervised learning melatih model menggunakan data yang memiliki label atau jawaban yang diketahui."

**Similarity Score:**

0.6478

**Menurut kalian apakah hasilnya relevan? Kenapa?**

**Kurang Relevan (Konteks Meleset)**. Jawaban yang paling tepat untuk *query* ini sebenarnya adalah dokumen mengenai model evaluasi. Di sini, model mengalami bias pencarian karena frasa "mengecek apakah (...) cukup tepat" diasosiasikan dengan konsep mencocokkan hasil prediksi dengan "jawaban yang diketahui" yang merupakan karakteristik proses evaluasi pada *supervised learning*. Model menangkap potongan konteks dari *training phase*, namun gagal mengembalikan dokumen spesifik yang membahas inti utama dari evaluasi performa model.

------------------------------------------------------

## Query 4

**Query:**

Apa pendekatan untuk membuat jawaban AI memakai informasi dari dokumen relevan yang ditemukan terlebih dahulu?

**Top Result:**

"Explainable AI berupaya membuat alasan di balik prediksi model lebih mudah dipahami manusia."

**Similarity Score:**

0.6184

**Menurut kalian apakah hasilnya relevan? Kenapa?**

**Tidak Relevan pada Hasil Teratas (Peringkat 1 & 2), Namun Relevan pada Peringkat 3**. *Query* ini secara jelas mendeskripsikan mekanisme kerja dari *Retrieval-Augmented Generation* atau RAG. Namun, sistem mengalami *ranking failure* karena menempatkan dokumen RAG pada posisi ketiga dengan skor yang cukup rendah (0,5758). Model *embedding* terjebak oleh indikasi *false positive* pada peringkat 1 yakni *Explainable AI* dan peringkat 2 yakni *Halusinasi AI* akibat adanya kemiripan frasa yang bersifat semu seperti kata "membuat jawaban/alasan" dan "informasi". Model terbukti lebih sensitif terhadap *lexical overlap* ketimbang memahami mekanisme utama dari sistem pencarian dokumen yang dimaksud oleh *query*.

------------------------------------------------------

## Query 5

**Query:**

Bagaimana melindungi identitas seseorang saat informasi digunakan untuk melatih sistem cerdas?

**Top Result:**

"Privasi data dalam AI mencakup perlindungan informasi pribadi selama pengumpulan dan pemrosesan."

**Similarity Score:**

0.6687

**Menurut kalian apakah hasilnya relevan? Kenapa?**

**Sangat Relevan**. Model *embedding* berhasil memetakan hubungan kata yang memiliki sinonim dengan sangat akurat. Frasa pada *query* yaitu "melindungi identitas seseorang" mampu diasosiasikan secara semantik dengan kalimat "perlindungan informasi pribadi" yang tercantum pada dokumen. Hal ini membuat dokumen dari kategori `responsible_ai` tersebut sukses diekstraksi sebagai hasil teratas dengan skor kemiripan yang tinggi.

------------------------------------------------------

# Experiment 2 - Top-K

Gunakan query yang sama.

### Query

Bagaimana cara mengecek apakah rekomendasi yang dibuat model sudah cukup tepat?

------------------------------------------------------

## Top-K = 1

Actual Result:

{
  "query": "Bagaimana cara mengecek apakah rekomendasi yang dibuat model sudah cukup tepat?",
  "results": [
    {
      "text": "Supervised learning melatih model menggunakan data yang memiliki label atau jawaban yang diketahui.",
      "category": "machine_learning",
      "score": 0.6478
    }
  ]
}

------------------------------------------------------

## Top-K = 3

Actual Result:

{
  "query": "Bagaimana cara mengecek apakah rekomendasi yang dibuat model sudah cukup tepat?",
  "results": [
    {
      "text": "Supervised learning melatih model menggunakan data yang memiliki label atau jawaban yang diketahui.",
      "category": "machine_learning",
      "score": 0.6478
    },
    {
      "text": "Data validasi membantu memilih konfigurasi model dan memantau performanya selama pengembangan.",
      "category": "data",
      "score": 0.6408
    },
    {
      "text": "Recall mengukur proporsi contoh positif yang berhasil ditemukan oleh model.",
      "category": "model_evaluation",
      "score": 0.6164
    }
  ]
}

------------------------------------------------------

## Top-K = 5

Actual Result:

{
  "query": "Bagaimana cara mengecek apakah rekomendasi yang dibuat model sudah cukup tepat?",
  "results": [
    {
      "text": "Supervised learning melatih model menggunakan data yang memiliki label atau jawaban yang diketahui.",
      "category": "machine_learning",
      "score": 0.6478
    },
    {
      "text": "Data validasi membantu memilih konfigurasi model dan memantau performanya selama pengembangan.",
      "category": "data",
      "score": 0.6408
    },
    {
      "text": "Recall mengukur proporsi contoh positif yang berhasil ditemukan oleh model.",
      "category": "model_evaluation",
      "score": 0.6164
    },
    {
      "text": "Model inference adalah tahap ketika model terlatih digunakan untuk menghasilkan prediksi dari masukan baru.",
      "category": "ai_fundamentals",
      "score": 0.5987
    },
    {
      "text": "Fine-tuning menyesuaikan model yang telah dilatih sebelumnya menggunakan data untuk tugas tertentu.",
      "category": "generative_ai",
      "score": 0.5857
    }
  ]
}

------------------------------------------------------

### Apa perubahan yang kalian lihat ketika nilai Top-K diperbesar?

Ketika parameter *Top-K* diperbesar dari 1, 3, hingga ke 5, perubahan yang sangat signifikan adalah meningkatnya keberagaman dokumen serta munculnya jawaban yang secara substansi materi jauh lebih relevan meskipun diikuti dengan penurunan *similarity score* pada peringkat bawah.
*   **Pada *Top-K* = 1**: Sistem hanya menampilkan satu dokumen definisi umum yang kurang spesifik, yakni `supervised_learning`.
*   **Pada *Top-K* = 3**: Dokumen target yang paling tepat buat menjawab *query* mulai muncul, yaitu dokumen tentang *Data Validation* di peringkat 2 dan *Recall* sebagai metrik evaluasi model di peringkat 3.
*   **Pada *Top-K* = 5**: Sistem mulai memasukkan dokumen tambahan seperti *Model Inference* di peringkat 4 dan *Fine-Tuning* di peringkat 5 dengan tren skor kemiripan yang makin menurun, yakni di bawah 0,60.

### Apakah menambah Top-K selalu membuat hasil pencarian menjadi lebih baik?

Tidak selalu. Meningkatkan nilai *Top-K* memiliki efek *trade-off* tertentu, sehingga tidak bisa dikatakan selalu membuat hasil pencarian jadi lebih baik. Berikut adalah analisisnya:

1. **Sisi Positif (Meningkatkan *Recall*)**: Meningkatkan parameter *Top-K* sangat membantu ketika model *embedding* mengalami *ranking failure* pada posisi pertama. Dengan memperbesar *Top-K*, dokumen target yang secara substansi materi relevan namun memiliki skor vektor lebih rendah seperti peringkat 2 dan 3 bisa ikut terambil dan tidak tereliminasi dari hasil pencarian.
2. **Sisi Negatif (Meningkatkan *Noise*)**: Jika nilai *Top-K* diperbesar secara berlebihan—misalnya ke *Top-K* = 5 atau lebih maka sistem bakal mulai memasukkan dokumen berperingkat rendah yang tidak relevan atau keluar dari inti konteks *query*. Contohnya seperti dokumen `model_inference` dan `fine_tuning` pada peringkat 4 dan 5. Keberadaan dokumen tambahan ini justru menjadi *noise* (gangguan informasi) yang bisa membingungkan pengguna akhir.

**Kesimpulan**: Nilai *Top-K* yang optimal harus ditentukan secara bijak. Untuk model pencarian semantik *zero-shot* berukuran kecil seperti ini, nilai *Top-K* = 3 merupakan titik optimal atau *sweet spot* karena berhasil menangkap jawaban terbaik tanpa menyertakan terlalu banyak informasi yang tidak relevan atau *noise*.

------------------------------------------------------

# Experiment 3 - Bad Retrieval

Cari satu query yang menghasilkan retrieval yang menurut kalian kurang relevan.

### Query

"Apa pendekatan untuk membuat jawaban AI memakai informasi dari dokumen relevan yang ditemukan terlebih dahulu?"

### Actual Results

{
  "query": "Apa pendekatan untuk membuat jawaban AI memakai informasi dari dokumen relevan yang ditemukan terlebih dahulu?",
  "results": [
    {
      "text": "Explainable AI berupaya membuat alasan di balik prediksi model lebih mudah dipahami manusia.",
      "category": "responsible_ai",
      "score": 0.6184
    },
    {
      "text": "Halusinasi AI terjadi ketika model menghasilkan informasi yang terdengar meyakinkan tetapi tidak didukung fakta.",
      "category": "responsible_ai",
      "score": 0.6144
    },
    {
      "text": "Retrieval-augmented generation menggabungkan pencarian informasi dengan pembuatan jawaban oleh model bahasa.",
      "category": "generative_ai",
      "score": 0.5758
    }
  ]
}

### Similarity Score

* Peringkat 1: 0.6184
* Peringkat 2: 0.6144
* Peringkat 3: 0.5758

### Kenapa menurut kalian hasil tersebut kurang relevan?

Hasil pada urutan 1 yakni terkait *Explainable AI* dan urutan 2 yakni terkait *Halusinasi AI* tidak pas dengan maksud utama *query*. *Query* tersebut secara jelas menggambarkan cara kerja dari susunan arsitektur *Retrieval-Augmented Generation* atau RAG, yaitu mengambil atau *retrieve* dokumen luar yang pas terlebih dahulu baru kemudian memakainya untuk membuat atau *generate* jawaban. Dokumen RAG pada *dataset* Anda yang isinya kalimat "menggabungkan pencarian informasi dengan pembuatan jawaban" adalah satu-satunya jawaban pasti yang benar. Namun, sistem malah mengalami kegagalan *ranking* dengan menaruh dokumen RAG tersebut di posisi paling akhir yakni urutan 3 dengan nilai paling rendah.

### Menurut kalian apa yang mungkin menyebabkan hasil tersebut?

Kegagalan pencarian semantik murni atau *zero-shot vector search* pada kasus ini disebabkan oleh dua faktor utama:

1. **Jebakan Potongan Kata Semu (*Keyword Overlap Bias*)**: Model *embedding* MiniLM tampaknya melakukan hitungan matematika yang terlalu sensitif pada kata-kata abstrak yang muncul bersamaan. Kalimat *query* "membuat jawaban AI memakai informasi" memiliki jarak vektor yang dekat secara semu dengan kalimat "membuat alasan (...) dipahami manusia" pada dokumen *Explainable AI* serta kalimat "menghasilkan informasi (...)" pada dokumen *Halusinasi AI*.
2. **Keterbatasan Pemahaman Cara Kerja Sistem**: Model *embedding* berukuran kecil yakni *paraphrase-multilingual-MiniLM-L12-v2* lebih condong mengenali kemiripan gaya bahasa cerita seperti membahas tentang etika, hasil akhir, dan kebenaran informasi AI daripada memahami urutan cara kerja dari sebuah arsitektur sistem atau proses mencari informasi yang dilakukan sebelum membuat teks. Akibatnya, dokumen dengan kelompok atau *klaster* topik etika AI lebih menguasai hasil paling atas dibanding topik AI generatif.

------------------------------------------------------

# Personal Reflection

### 1. Sebelum mengerjakan tugas ini, bagaimana kalian membayangkan sebuah search engine bekerja? Apakah ada perbedaan setelah mempelajari semantic search?

Sebelumnya, saya mengira bahwa *search engine* bekerja hanya dengan cara mencocokkan kata yang diketik secara persis dengan kata-kata yang ada di dalam *database*. Jika kata kunci yang dimasukkan salah ketik atau memakai *sinonim*, maka data tidak akan ketemu. Setelah mempelajari *semantic search*, sudut pandang saya berubah total. Ternyata mesin pencari modern bisa memahami arti, maksud, dan *konteks* dari sebuah kalimat. Sistem tidak lagi sekadar mencari teks yang sama, melainkan mencari informasi yang punya kedekatan konsep secara menyeluruh.

### 2. Menurut kalian apa perbedaan terbesar antara keyword search dan semantic search?

Perbedaan paling besar ada pada tingkat pemahaman *konteks*.

*   **Keyword search**: Bekerja secara kaku menggunakan *lexical matching*. Jika kita mencari kata "foto" sedangkan dokumen menulis kata "gambar", sistem biasa ini akan gagal menemukannya.
*   **Semantic search**: Bekerja dengan memahami maksud di balik kata tersebut. Sistem ini tahu *sinonim* suatu kata, susunan kalimat bebas, bahkan *metafora*, karena teks sudah diatur ke dalam ruang vektor berdasarkan arti konsepnya.

### 3. Menurut kalian apa fungsi embedding di dalam semantic search?

Fungsi utama *embedding* adalah sebagai jembatan atau penerjemah bahasa manusia ke dalam bentuk *vektor* yang dimengerti oleh komputer. *Embedding model* bertugas mengambil inti utama dari sebuah kalimat dan mengubahnya menjadi deretan angka kontinu dengan ukuran tetap dimana pada proyek ini yaitu 384 dimensi. Dengan bentuk angka tersebut, komputer bisa menghitung jarak kedekatan arti antar-kalimat menggunakan rumus matematika seperti *Cosine Similarity*.

### 4. Kenapa embedding tidak cukup hanya disimpan di list Python jika jumlah data menjadi sangat banyak?

Menyimpan *vektor* di dalam *list* Python biasa hanya mempan untuk data ukuran kecil sekitar puluhan data. Jika jumlah dokumen membengkak menjadi jutaan, melakukan pencarian satu per satu lewat cara *looping* menggunakan *list* Python akan memakan waktu sangat lama dan menghabiskan memori RAM secara boros dengan proses berkecepatan sebanyak O(N). Oleh karena itu, kita butuh *Vector Database* khusus seperti Qdrant yang memakai susunan indeksasi canggih seperti HNSW agar pencarian jutaan *vektor* berdimensi tinggi bisa selesai dalam hitungan milidetik.

### 5. Bagian project mana yang paling sulit kalian pahami?

Bagian yang paling sulit dimengerti awalnya adalah proses menghubungkan *query* dan cara mengatasi *ranking mismatch* pada model *embedding* murni atau *zero-shot*. Sulit bagi saya untuk menebak mengapa model matematika kadang mengalami *false positive*, seperti pada Percobaan 3 di mana *query* RAG malah memunculkan *Explainable AI*. Memahami bagaimana model MiniLM menghitung kedekatan jarak antar-kata abstrak dalam bahasa Indonesia butuh analisis cara kerja yang cukup mendalam.

### 6. Bagian kode mana yang paling banyak dibantu oleh AI?

Bagian kode yang paling banyak dibantu oleh AI adalah pengaturan jalannya aplikasi memakai `asynccontextmanager` atau *lifespan* pada FastAPI serta pemasangan fungsi `query_points` dari *library* Qdrant paling baru. Mengatur agar model SentenceTransformers dan *client* Qdrant bisa siap secara otomatis saat *startup* dan menutup hubungannya dengan aman saat *shutdown* membutuhkan *boilerplate code* yang cukup khusus.

### 7. Jelaskan dengan bahasa kalian sendiri bagaimana bagian kode tersebut bekerja.

Fungsi *lifespan* bekerja sebagai pengatur gerbang otomatis aplikasi. Ketika aplikasi FastAPI pertama kali dijalankan, fungsi ini akan langsung mengunduh dan menyiapkan model SentenceTransformers ke dalam memori RAM, lalu melakukan *sanity check* ukuran *vector* agar tidak terjadi eror di kemudian hari. Di saat yang sama, ia membuka hubungan ke *database* lokal Qdrant dan memastikan ruang penyimpanan atau *collection* sudah siap. Ketika aplikasi dimatikan atau *shutdown*, fungsi ini secara otomatis menutup hubungan *database* agar tidak terjadi *data corruption*.

### 8. Menurut kalian, aplikasi semantic search yang kalian buat bisa dikembangkan menjadi aplikasi apa jika project ini dilanjutkan?

Jika proyek ini dilanjutkan, aplikasi ini dikembangkan menjadi dua hal berikut:

1. **Sistem RAG (*Retrieval-Augmented Generation*) Utuh**: Menyatukan pencarian semantik ini dengan *LLM* seperti OpenAI atau Ollama untuk membuat *chatbot* pintar atau asisten sekolah yang bisa menjawab pertanyaan berdasarkan dokumen dalam/buku teks AI secara tepat tanpa *halusinasi*.
2. **Mesin Pencari Dokumen Hukum / Medis**: Mengatur ribuan berkas dengan istilah teknis yang rumit, sehingga pekerja hukum atau medis bisa mencari contoh kasus masa lalu hanya dengan memasukkan cerita kejadian yang sederhana.

------------------------------------------------------

# AI Usage

### AI tools yang digunakan

Google Gemini

### AI digunakan untuk membantu bagian apa?

*   **Penyusunan *Boilerplate Code***: Membantu mengatur susunan dasar `asynccontextmanager` atau *lifespan* pada FastAPI untuk mengurus bahan aplikasi atau *resources* saat *startup* dan *shutdown* secara rapi.
*   **Pemasangan API Qdrant Paling Baru**: Membantu menulis kode ketikan pencarian menggunakan fungsi standar paling baru dari Qdrant Client, yaitu `query_points`.

### Bagian apa yang kalian ubah atau tentukan sendiri setelah mendapatkan hasil dari AI?

*   **Susunan dan Aturan Pengecekan *Dataset***: Saya menentukan sendiri batasan angka seperti *MIN_DOCUMENTS*, *MAX_DOCUMENTS*, *MIN_CATEGORIES* serta menulis kode *error handling* pada fungsi `validate_dataset` agar cocok dengan aturan tugas yang diberikan.
*   **Pemilihan Isi Dokumen AI Concept**: Isi teks dan pembagian 10 kategori dalam variabel `DOCUMENTS` seperti membedakan kelompok *machine_learning*, *deep_learning*, sampai *responsible_ai* diatur dan diperiksa sendiri oleh saya agar macam istilah teknisnya cukup sulit bagi model pencarian.
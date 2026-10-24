from typing import Dict, List

MIN_DOCUMENTS = 20
MAX_DOCUMENTS = 50
MIN_CATEGORIES = 3

DOCUMENTS: List[Dict[str, str]] = [
    {
        "text": "Kecerdasan buatan adalah bidang ilmu komputer yang membuat sistem mampu melakukan tugas yang biasanya membutuhkan kecerdasan manusia.",
        "category": "ai_fundamentals",
    },
    {
        "text": "Machine learning memungkinkan komputer mempelajari pola dari data tanpa harus diprogram dengan aturan untuk setiap kasus.",
        "category": "machine_learning",
    },
    {
        "text": "Deep learning menggunakan jaringan saraf berlapis untuk mempelajari representasi data yang kompleks.",
        "category": "deep_learning",
    },
    {
        "text": "Supervised learning melatih model menggunakan data yang memiliki label atau jawaban yang diketahui.",
        "category": "machine_learning",
    },
    {
        "text": "Unsupervised learning mencari struktur atau pola dalam data yang belum diberi label.",
        "category": "machine_learning",
    },
    {
        "text": "Reinforcement learning melatih agen melalui interaksi dengan lingkungan dan umpan balik berupa reward.",
        "category": "machine_learning",
    },
    {
        "text": "Dataset adalah kumpulan data yang digunakan untuk melatih, memvalidasi, atau menguji model AI.",
        "category": "data",
    },
    {
        "text": "Fitur adalah atribut masukan yang digunakan model untuk membuat prediksi.",
        "category": "data",
    },
    {
        "text": "Label adalah nilai target yang ingin diprediksi oleh model dalam pembelajaran terawasi.",
        "category": "data",
    },
    {
        "text": "Data training digunakan untuk menyesuaikan parameter model selama proses pembelajaran.",
        "category": "data",
    },
    {
        "text": "Data validasi membantu memilih konfigurasi model dan memantau performanya selama pengembangan.",
        "category": "data",
    },
    {
        "text": "Data testing digunakan untuk mengukur kemampuan model pada data yang tidak dipakai saat pelatihan.",
        "category": "data",
    },
    {
        "text": "Overfitting terjadi ketika model terlalu menyesuaikan diri dengan data training dan kurang mampu menangani data baru.",
        "category": "model_evaluation",
    },
    {
        "text": "Underfitting terjadi ketika model terlalu sederhana untuk menangkap pola penting dalam data.",
        "category": "model_evaluation",
    },
    {
        "text": "Akurasi mengukur proporsi prediksi yang benar dibandingkan dengan seluruh prediksi.",
        "category": "model_evaluation",
    },
    {
        "text": "Precision mengukur proporsi prediksi positif yang benar-benar positif.",
        "category": "model_evaluation",
    },
    {
        "text": "Recall mengukur proporsi contoh positif yang berhasil ditemukan oleh model.",
        "category": "model_evaluation",
    },
    {
        "text": "F1-score menggabungkan precision dan recall menjadi satu ukuran menggunakan rata-rata harmonik.",
        "category": "model_evaluation",
    },
    {
        "text": "Natural language processing memungkinkan komputer menganalisis dan menghasilkan bahasa manusia.",
        "category": "nlp",
    },
    {
        "text": "Tokenisasi memecah teks menjadi unit yang lebih kecil, seperti kata, subkata, atau karakter.",
        "category": "nlp",
    },
    {
        "text": "Embedding merepresentasikan teks atau objek sebagai vektor angka yang menangkap hubungan makna.",
        "category": "nlp",
    },
    {
        "text": "Analisis sentimen mengklasifikasikan opini dalam teks, misalnya sebagai positif, negatif, atau netral.",
        "category": "nlp",
    },
    {
        "text": "Model bahasa mempelajari pola bahasa untuk memahami atau menghasilkan teks.",
        "category": "nlp",
    },
    {
        "text": "Large language model dilatih pada kumpulan teks besar untuk menangani beragam tugas bahasa.",
        "category": "generative_ai",
    },
    {
        "text": "Prompt adalah instruksi atau masukan yang diberikan kepada model generatif untuk mengarahkan keluarannya.",
        "category": "generative_ai",
    },
    {
        "text": "Retrieval-augmented generation menggabungkan pencarian informasi dengan pembuatan jawaban oleh model bahasa.",
        "category": "generative_ai",
    },
    {
        "text": "Fine-tuning menyesuaikan model yang telah dilatih sebelumnya menggunakan data untuk tugas tertentu.",
        "category": "generative_ai",
    },
    {
        "text": "Halusinasi AI terjadi ketika model menghasilkan informasi yang terdengar meyakinkan tetapi tidak didukung fakta.",
        "category": "responsible_ai",
    },
    {
        "text": "Computer vision membantu sistem memperoleh informasi dari gambar dan video.",
        "category": "computer_vision",
    },
    {
        "text": "Klasifikasi gambar memprediksi kategori yang paling sesuai untuk sebuah gambar.",
        "category": "computer_vision",
    },
    {
        "text": "Deteksi objek menemukan lokasi dan kelas objek di dalam gambar.",
        "category": "computer_vision",
    },
    {
        "text": "Segmentasi gambar memberikan label pada piksel untuk memisahkan objek atau wilayah gambar.",
        "category": "computer_vision",
    },
    {
        "text": "Jaringan saraf tiruan terdiri atas unit-unit komputasi yang saling terhubung dan memiliki bobot.",
        "category": "deep_learning",
    },
    {
        "text": "Fungsi aktivasi membantu jaringan saraf mempelajari hubungan nonlinier dalam data.",
        "category": "deep_learning",
    },
    {
        "text": "Backpropagation menghitung kontribusi kesalahan terhadap parameter jaringan saraf agar bobot dapat diperbarui.",
        "category": "deep_learning",
    },
    {
        "text": "Gradient descent memperbarui parameter model secara bertahap untuk mengurangi nilai loss.",
        "category": "deep_learning",
    },
    {
        "text": "Loss function mengukur seberapa jauh prediksi model dari nilai yang diharapkan.",
        "category": "deep_learning",
    },
    {
        "text": "Bias dalam AI dapat muncul ketika data atau rancangan sistem menghasilkan perlakuan yang tidak adil.",
        "category": "responsible_ai",
    },
    {
        "text": "Explainable AI berupaya membuat alasan di balik prediksi model lebih mudah dipahami manusia.",
        "category": "responsible_ai",
    },
    {
        "text": "Privasi data dalam AI mencakup perlindungan informasi pribadi selama pengumpulan dan pemrosesan.",
        "category": "responsible_ai",
    },
    {
        "text": "Human-in-the-loop melibatkan manusia dalam proses pengawasan, penilaian, atau pengambilan keputusan AI.",
        "category": "responsible_ai",
    },
    {
        "text": "AI generatif menghasilkan konten baru, seperti teks, gambar, audio, atau kode.",
        "category": "generative_ai",
    },
    {
        "text": "Sistem rekomendasi menyarankan item berdasarkan preferensi pengguna atau pola perilaku.",
        "category": "ai_applications",
    },
    {
        "text": "Deteksi anomali mencari data yang menyimpang dari pola umum dalam suatu kumpulan data.",
        "category": "ai_applications",
    },
    {
        "text": "Prapemrosesan data memperbaiki atau mengubah data agar lebih siap digunakan oleh model.",
        "category": "data",
    },
    {
        "text": "Normalisasi fitur menyetarakan skala nilai agar perbedaan rentang tidak mendominasi proses pembelajaran.",
        "category": "data",
    },
    {
        "text": "Augmentasi data menambah variasi pada data training, misalnya dengan mengubah gambar secara terkontrol.",
        "category": "data",
    },
    {
        "text": "Model inference adalah tahap ketika model terlatih digunakan untuk menghasilkan prediksi dari masukan baru.",
        "category": "ai_fundamentals",
    },
    {
        "text": "Metrik evaluasi perlu dipilih sesuai tujuan dan dampak kesalahan pada tugas AI.",
        "category": "model_evaluation",
    },
    {
        "text": "AI yang bertanggung jawab mempertimbangkan keadilan, transparansi, keselamatan, dan dampak bagi manusia.",
        "category": "responsible_ai",
    },
]

def validate_dataset(documents: List[Dict[str, str]]) -> None:
    if not isinstance(documents, list):
        raise ValueError("Dataset harus berupa list of dictionaries.")

    doc_count = len(documents)
    if doc_count < MIN_DOCUMENTS:
        raise ValueError(
            f"Jumlah data saat ini ({doc_count}) kurang dari batas minimal ({MIN_DOCUMENTS})."
        )
    if doc_count > MAX_DOCUMENTS:
        raise ValueError(
            f"Jumlah data saat ini ({doc_count}) melebihi batas maksimal yang disarankan ({MAX_DOCUMENTS})."
        )

    categories = set()
    for idx, item in enumerate(documents):
        text = item.get("text", "").strip()
        category = item.get("category", "").strip()

        if not text or not category:
            raise ValueError(
                f"Data pada indeks ke-{idx} tidak valid: 'text' dan 'category' tidak boleh kosong."
            )
        categories.add(category)

    if len(categories) < MIN_CATEGORIES:
        raise ValueError(
            f"Dataset hanya memiliki {len(categories)} kategori ({categories}). Minimal wajib {MIN_CATEGORIES} kategori."
        )

validate_dataset(DOCUMENTS)
print(f"Dataset valid: {len(DOCUMENTS)} data, {len({item['category'] for item in DOCUMENTS})} kategori.")

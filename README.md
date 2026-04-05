# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech JAYA JAYA INSTITUTE

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang mengalami tantangan dalam mempertahankan mahasiswanya. Tingkat dropout (putus kuliah) yang cukup tinggi menjadi masalah utama yang berdampak pada reputasi institusi, efisiensi operasional, dan pendapatan. Institusi perlu mengidentifikasi faktor-faktor yang menyebabkan mahasiswa dropout serta mengembangkan strategi intervensi dini untuk meningkatkan tingkat kelulusan (graduate rate).

### Permasalahan Bisnis
Berdasarkan latar belakang di atas, permasalahan bisnis yang akan diselesaikan adalah:
- A. Tingginya angka dropout mahasiswa yang tidak terdeteksi sejak awal, sehingga institusi kehilangan kesempatan untuk melakukan intervensi.
- B. Kurangnya pemahaman tentang faktor-faktor yang paling berpengaruh terhadap status mahasiswa (Dropout vs Graduate).
- C. Tidak adanya sistem prediksi dini yang dapat membantu institusi mengidentifikasi mahasiswa berisiko dropout sebelum terlambat.
- D. Keterbatasan dashboard monitoring untuk memantau performa mahasiswa.

### Cakupan Proyek
Proyek ini mencakup:
- A. Data Understanding & Preparation: Eksplorasi data, filtering hanya status Dropout dan Graduate, encoding, scaling, dan handling imbalanced data dengan SMOTE.
- B. Modeling Machine Learning: Pembangunan model Random Forest untuk **binary classification** (Dropout vs Graduate) dengan hyperparameter tuning menggunakan GridSearchCV.
- C. Evaluasi Model: Pengukuran akurasi, precision, recall, F1-score, confusion matrix, dan feature importance.
- D. Business Dashboard: Pembuatan dashboard visual menggunakan Looker Studio untuk monitoring performa mahasiswa.
- E. Deployment Model: Implementasi model dalam bentuk prototype Streamlit yang dapat diakses secara online.

### Persiapan
**Sumber data:** Dataset diperoleh dari GitHub Dicoding  
Link dataset: [https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

**Link Penting:**
- Google Looker Studio: [https://lookerstudio.google.com/reporting/8cb74369-46b5-4903-9915-f5994fa55a61](https://lookerstudio.google.com/reporting/8cb74369-46b5-4903-9915-f5994fa55a61)
- Streamlit: [https://penerapan-ds2-dm4xbnbrax26mraopahefr.streamlit.app/](https://penerapan-ds2-dm4xbnbrax26mraopahefr.streamlit.app/)
- GitHub: [https://github.com/JeJes-7/penerapan-ds2](https://github.com/JeJes-7/penerapan-ds2)

**Setup environment:**
```bash
# Buat virtual environment (opsional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install library yang diperlukan
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn joblib streamlit

# Atau jika menggunakan requirements.txt
pip install -r requirements.txt
```

## Business Dashboard
Dashboard bisnis yang dibuat menggunakan Looker Studio bertujuan untuk memonitor dan menganalisis faktor‑faktor yang mempengaruhi dropout mahasiswa di Jaya Jaya Institut. Dashboard ini menyajikan visualisasi interaktif dari data historis mahasiswa, mencakup:

## Visualisasi	Tujuan Analisis
- KPI Utama	dengan menghitung Total mahasiswa (Graduate+Dropout), jumlah dropout
- Distribusi Status Mahasiswa dengan proporsi Graduate vs Dropout (Enrolled dikeluarkan).
- Analisis Nilai Berdasarkan Status	dengan menghitung Perbandingan rata‑rata nilai semester 1, semester 2, dan admission grade antara Graduate dan Dropout.
- Dropout Rate berdasarkan Gender	Bar chart untuk melihat perbedaan dropout rate antara laki‑laki dan perempuan (tidak signifikan).
- Dropout Rate berdasarkan Penerima Beasiswa	Bar chart menunjukkan bahwa non-beasiswa memiliki dropout rate jauh lebih tinggi.
- Dropout Rate berdasarkan Status Biaya Kuliah	Bar chart dengan calculated field Dropout Rate – menunjukkan bahwa mahasiswa dengan status "Belum Lunas" hampir 100% dropout.
- Distribusi Usia (Dropout vs Graduate)	Histogram dengan bucket usia (17-20, 21-25, ..., 46-50) – usia muda lebih banyak graduate dan dropout, daripada usia lebih tua.

### Insight Utama dari Dashboard:
- Gender tidak mempengaruhi dropout rate secara signifikan (50,7% laki-laki, 49,3% perempuan).
- Penerima beasiswa memiliki dropout rate jauh lebih rendah (≈20-25%) dibanding non-beasiswa (>50%).
- Status biaya kuliah merupakan indikator terkuat: mahasiswa dengan status "Lunas" hampir pasti dropout, sedangkan yang "Belum Lunas" sangat kecil risiko dropout.
- Usia muda (17-20 tahun) lebih banyak lulus dan dropout daripada usia dewasa (>30 tahun)
- Nilai semester 1 dan 2 yang rendah berkorelasi kuat dengan status dropout.
Dashboard ini memungkinkan manajemen institusi untuk mengidentifikasi segmen mahasiswa yang paling rentan dropout dan mengambil tindakan preventif secara data‑driven.

### Menjalankan Sistem Machine Learning
Prototipe sistem machine learning untuk memprediksi status mahasiswa (Dropout atau Graduate) telah dikembangkan menggunakan Random Forest Classifier (binary). Model dilatih dengan dataset yang telah difilter (hanya Dropout dan Graduate) dan menggunakan SMOTE untuk menyeimbangkan kelas. Aplikasi web Streamlit memungkinkan pengguna memasukkan 8 fitur penting untuk mendapatkan prediksi instan.

Cara menjalankan prototipe (lokal):
- Pastikan Python 3.8+ terinstal dan buat virtual environment (opsional).
- Clone atau unduh folder proyek yang berisi file:
---app.py (kode utama Streamlit)
---model_rf_best_compressed.pkl (model terlatih)
---label_encoder.pkl
---scaler.pkl
---requirements.txt
- Instal dependensi:
bash
pip install -r requirements.txt
- Jalankan aplikasi:
bash
streamlit run app.py

Aplikasi akan terbuka di browser (biasanya http://localhost:8501). Pengguna cukup memasukkan 8 fitur penting (usia, jumlah mata kuliah diambil & lulus semester 1 & 2, nilai rata‑rata semester 1 & 2, status biaya kuliah) lalu klik tombol prediksi. Sistem akan menampilkan status prediksi (Dropout atau Graduate) serta probabilitas untuk setiap kelas.

## Conclusion
Proyek ini berhasil mengembangkan sistem prediksi dropout mahasiswa berbasis machine learning yang mampu mengidentifikasi mahasiswa berisiko dropout dengan akurasi yang baik.
### Kesimpulan 1 – Faktor-faktor Penyebab Dropout (Berdasarkan EDA dan Dashboard)
Faktor akademik: Nilai rendah pada semester 1 dan 2, serta jumlah mata kuliah lulus yang sedikit, merupakan prediktor kuat dropout.
- Faktor finansial: Ketidaklancaran pembayaran biaya kuliah (Tuition_fees_up_to_date = 0) adalah indikator paling dominan – hampir semua mahasiswa dengan status "Belum Lunas" berakhir dropout.
- Faktor beasiswa: Mahasiswa non-beasiswa memiliki risiko dropout lebih tinggi dibanding penerima beasiswa.
- Faktor usia: Mahasiswa usia muda (17-20 tahun) cenderung lulus dan dropout, daripada usia tua
- Faktor gender: Tidak ada perbedaan signifikan antara laki-laki dan perempuan.
### Kesimpulan 2 – Performa Model dan Fitur Penting
Model Random Forest binary (Dropout vs Graduate) yang telah di-tuning mencapai performa:
- Akurasi: 91,18%
- Precision (Dropout): 94,39%
- Recall (Dropout): 87,56%
- F1-score (macro): 91,75% (berdasarkan cross-validation 5-fold)
Cross-validation scores: [0.9036, 0.9025, 0.8967, 0.9354, 0.9490] dengan rata-rata 0,9175 ± 0,0208
Top 5 fitur terpenting berdasarkan feature importance:
- Curricular_units_1st_sem_grade (nilai semester 1)
- Curricular_units_2nd_sem_grade (nilai semester 2)
- Curricular_units_1st_sem_approved (jumlah mata kuliah lulus semester 1)
- Tuition_fees_up_to_date (status biaya kuliah)
- Curricular_units_2nd_sem_approved (jumlah mata kuliah lulus semester 2)
Model ini stabil dan tidak overfitting, terbukti dari standar deviasi cross-validation yang kecil (2,08%).
Dengan adanya sistem ini, Jaya Jaya Institut dapat beralih dari pendekatan reaktif menjadi proaktif dalam menangani masalah dropout, sehingga dapat meningkatkan angka kelulusan dan efisiensi sumber daya.

## Rekomendasi Action Items
### Action Item 1 – Intervensi Akademik Dini
Lakukan pemantauan ketat terhadap mahasiswa yang pada semester 1 memiliki nilai rata‑rata di bawah 10 (skala 20) atau jumlah mata kuliah lulus kurang dari 60% dari total terdaftar. Berikan program bimbingan belajar (tutoring) dan konseling akademik sebelum memasuki semester 2.
### Action Item 2 – Program Bantuan Pembayaran
Identifikasi mahasiswa dengan status biaya kuliah tidak lancar (Tuition_fees_up_to_date = 0) dan tawarkan skema cicilan fleksibel, beasiswa parsial, atau akses ke dana bantuan darurat. Berdasarkan model, faktor ini memiliki pengaruh besar terhadap risiko dropout.
### Action Item 3 – Sistem Peringatan Dini (Early Warning System)
Integrasikan model prediksi ke dalam sistem informasi akademik sehingga setiap dosen wali atau kepala program studi dapat melihat probabilitas dropout untuk setiap mahasiswa secara real‑time. Tentukan ambang batas (misal probabilitas > 70%) untuk memicu notifikasi dan tindakan preventif otomatis.
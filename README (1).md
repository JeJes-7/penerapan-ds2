# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech JAYA JAYA INSTITUTE

## Business Understanding
Jaya Jaya Institut merupakan institusi pendidikan tinggi yang mengalami tantangan dalam mempertahankan mahasiswanya. Tingkat dropout (putus kuliah) yang cukup tinggi menjadi masalah utama yang berdampak pada reputasi institusi, efisiensi operasional, dan pendapatan. Institusi perlu mengidentifikasi faktor-faktor yang menyebabkan mahasiswa dropout serta mengembangkan strategi intervensi dini untuk meningkatkan tingkat kelulusan (graduate rate).

### Permasalahan Bisnis
Berdasarkan latar belakang di atas, permasalahan bisnis yang akan diselesaikan adalah:
A. Tingginya angka dropout mahasiswa yang tidak terdeteksi sejak awal, sehingga institusi kehilangan kesempatan untuk melakukan intervensi.
B. Kurangnya pemahaman tentang faktor-faktor yang paling berpengaruh terhadap status mahasiswa (dropout, enrolled, graduate).
C. Tidak adanya sistem prediksi dini yang dapat membantu institusi mengidentifikasi mahasiswa berisiko dropout sebelum terlambat.
D. Keterbatasan dashboard monitoring untuk memantau performa mahasiswa

### Cakupan Proyek
Proyek ini mencakup:
A. Data Understanding & Preparation: Eksplorasi data, penanganan missing values, encoding, scaling, dan handling imbalanced data dengan SMOTE.
B. Modeling Machine Learning: Pembangunan model Random Forest untuk klasifikasi 3 kelas (Dropout, Enrolled, Graduate) dengan hyperparameter tuning menggunakan GridSearchCV.
C. Evaluasi Model: Pengukuran akurasi, F1-score, confusion matrix, dan feature importance.
D. Business Dashboard: Pembuatan dashboard visual menggunakan  Looker Studio untuk monitoring performa mahasiswa.
E. Deployment Model: Implementasi model dalam bentuk prototype Streamlit yang dapat diakses secara online

### Persiapan
Sumber data: Dataset diperoleh dari github dicoding
Link dataset: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```
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
Dashboard bisnis yang dibuat menggunakan Looker Studio (Google Data Studio) bertujuan untuk memonitor dan menganalisis faktor‑faktor yang mempengaruhi dropout mahasiswa di Jaya Jaya Institut. Dashboard ini menyajikan visualisasi interaktif dari data historis mahasiswa, mencakup:
A. KPI Utama: Total mahasiswa, jumlah dropout, persentase dropout, dan rata‑rata nilai semester.
B. Distribusi Status Mahasiswa: Pie chart dan bar chart untuk melihat proporsi Dropout, Graduate, dan Enrolled.
C. Analisis Nilai Berdasarkan Status: Perbandingan rata‑rata nilai masuk, nilai kualifikasi sebelumnya, dan nilai semester 1 & 2 antar kelompok status.
D. Faktor Demografi & Sosial Ekonomi: Dropout rate berdasarkan gender, status beasiswa, hutang (debtor), dan kelompok umur.
E. Hubungan Nilai Semester 1 vs Semester 2: Scatter plot yang diwarnai berdasarkan status untuk melihat pola nilai.
F. Filter Interaktif: Pengguna dapat memfilter berdasarkan course, gender, usia, penerima beasiswa, dll.
Dashboard ini memungkinkan manajemen institusi untuk mengidentifikasi segmen mahasiswa yang paling rentan dropout dan mengambil tindakan preventif secara data‑driven.

## Menjalankan Sistem Machine Learning
Prototipe sistem machine learning untuk memprediksi status mahasiswa (Dropout, Enrolled, Graduate) telah dikembangkan menggunakan Random Forest Classifier. Model dilatih dengan dataset student performance yang mencakup 36 fitur. Untuk memudahkan penggunaan, sistem diimplementasikan dalam aplikasi web Streamlit yang dapat dijalankan secara lokal maupun di‑cloud.

```
Cara menjalankan prototipe (lokal):
A. Pastikan Python 3.8+ terinstal dan buat virtual environment (opsional namun disarankan).
B. Clone atau unduh folder proyek yang berisi file:
app.py (kode utama Streamlit)
model_rf_best.pkl (model terlatih)
label_encoder.pkl
scaler.pkl
requirements.txt

Instal dependensi dengan perintah:
bash
pip install -r requirements.txt

Jalankan aplikasi:
bash
streamlit run app.py
Aplikasi akan terbuka di browser (biasanya http://localhost:8501). Pengguna cukup memasukkan 8 fitur penting (usia, jumlah mata kuliah diambil & lulus semester 1 & 2, nilai rata‑rata semester 1 & 2, status biaya kuliah) lalu klik tombol prediksi. Sistem akan menampilkan status prediksi serta probabilitas untuk setiap kelas.
```

## Conclusion
Proyek ini berhasil mengembangkan sistem prediksi dropout mahasiswa berbasis machine learning yang mampu mengidentifikasi mahasiswa berisiko dropout dengan akurasi yang baik. Berdasarkan analisis data dan model, ditemukan bahwa faktor akademik (jumlah mata kuliah lulus dan nilai rata‑rata semester 1 & 2) serta faktor administrasi (ketepatan pembayaran biaya kuliah) merupakan prediktor terkuat. Sementara itu, fitur demografi seperti usia, gender, dan status pernikahan memiliki pengaruh lebih kecil namun tetap signifikan.

Dashboard bisnis yang dibangun memberikan visualisasi yang jelas dan interaktif, memudahkan pemangku kepentingan untuk memantau indikator kunci dan melakukan eksplorasi data secara mandiri. Prototipe sistem prediksi dalam bentuk aplikasi web memungkinkan staf akademik atau dosen wali untuk dengan cepat mengevaluasi status mahasiswa hanya dengan memasukkan beberapa data sederhana.

Dengan adanya sistem ini, Jaya Jaya Institut dapat beralih dari pendekatan reaktif menjadi proaktif dalam menangani masalah dropout, sehingga dapat meningkatkan angka kelulusan dan efisiensi sumber daya.

### Rekomendasi Action Items
Berdasarkan temuan proyek, berikut adalah rekomendasi tindakan yang segera dapat dilakukan oleh perusahaan (Jaya Jaya Institut):

Action Item 1 – Intervensi Akademik Dini
Lakukan pemantauan ketat terhadap mahasiswa yang pada semester 1 memiliki nilai rata‑rata di bawah 10 (skala 20) atau jumlah mata kuliah lulus kurang dari 60% dari total terdaftar. Berikan program bimbingan belajar (tutoring) dan konseling akademik sebelum memasuki semester 2.

Action Item 2 – Program Bantuan Pembayaran
Identifikasi mahasiswa dengan status biaya kuliah tidak lancar (Tuition_fees_up_to_date = 0) dan tawarkan skema cicilan fleksibel, beasiswa parsial, atau akses ke dana bantuan darurat. Berdasarkan model, faktor ini memiliki pengaruh besar terhadap risiko dropout.

Action Item 3 – Sistem Peringatan Dini (Early Warning System)
Integrasikan model prediksi ke dalam sistem informasi akademik sehingga setiap dosen wali atau kepala program studi dapat melihat probabilitas dropout untuk setiap mahasiswa secara real‑time. Tentukan ambang batas (misal probabilitas > 70%) untuk memicu notifikasi dan tindakan preventif otomatis.

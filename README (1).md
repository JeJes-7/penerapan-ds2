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
A. Data Understanding & Preparation: Eksplorasi data, penanganan missing values (tidak ada), encoding, scaling, dan handling imbalanced data dengan SMOTE.
B. Modeling Machine Learning: Pembangunan model Random Forest untuk klasifikasi 3 kelas (Dropout, Enrolled, Graduate) dengan hyperparameter tuning menggunakan GridSearchCV.
C. Evaluasi Model: Pengukuran akurasi, F1-score, confusion matrix, dan feature importance.
D. Business Dashboard: Pembuatan dashboard visual menggunakan Metabase (atau alternatif Looker Studio) untuk monitoring performa mahasiswa.
E. Deployment Model: Implementasi model dalam bentuk prototype Streamlit yang dapat diakses secara online melalui Streamlit Community Cloud.

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
Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2

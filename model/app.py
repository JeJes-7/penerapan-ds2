import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os  # <-- ditambahkan

# ---------- Load model dan preprocessor ----------
@st.cache_resource
def load_models():
    base_dir = os.path.dirname(__file__)
    
    model_path = os.path.join(base_dir, 'model_rf_best_compressed.pkl')
    le_path = os.path.join(base_dir, 'label_encoder.pkl')
    scaler_path = os.path.join(base_dir, 'scaler.pkl')
    
    # Cek apakah semua file ada
    missing = []
    if not os.path.exists(model_path):
        missing.append("model_rf_best_compressed.pkl")
    if not os.path.exists(le_path):
        missing.append("label_encoder.pkl")
    if not os.path.exists(scaler_path):
        missing.append("scaler.pkl")
    
    if missing:
        st.error(f"File tidak ditemukan: {', '.join(missing)}. Pastikan file-file tersebut ada di folder yang sama dengan app.py.")
        st.stop()
    
    try:
        model = joblib.load(model_path)
        label_encoder = joblib.load(le_path)
        scaler = joblib.load(scaler_path)
        return model, label_encoder, scaler
    except Exception as e:
        st.error(f"Gagal memuat model/preprocessor: {e}")
        st.stop()

# Panggil fungsi load
model, label_encoder, scaler = load_models()

# ---------- FUNGSI INPUT ----------
def get_user_input():
    """Mengambil input hanya dari 8 fitur terpenting yang diperlukan untuk prediksi"""
    
    st.sidebar.header("Input Data Mahasiswa")
    
    # Fitur penting #1
    age_at_enrollment = st.sidebar.number_input(
        "Usia saat Mendaftar", min_value=17, max_value=70, value=20,
        help="Semakin tua usia, risiko dropout bisa berbeda"
    )
    
    # Semester 1
    st.sidebar.subheader("Semester 1")
    cu_1st_sem_enrolled = st.sidebar.number_input(
        "Jumlah mata kuliah diambil (semester 1)", min_value=0, max_value=20, value=6,
        help="Jumlah mata kuliah yang terdaftar"
    )
    cu_1st_sem_approved = st.sidebar.number_input(
        "Jumlah mata kuliah lulus (semester 1)", min_value=0, max_value=20, value=5,
        help="Semakin banyak lulus, semakin kecil risiko dropout"
    )
    cu_1st_sem_grade = st.sidebar.number_input(
        "Rata-rata nilai semester 1 (0-20)", min_value=0.0, max_value=20.0, value=12.0,
        help="Nilai tinggi -> cenderung Graduate"
    )
    
    # Semester 2
    st.sidebar.subheader("Semester 2")
    cu_2nd_sem_enrolled = st.sidebar.number_input(
        "Jumlah mata kuliah diambil (semester 2)", min_value=0, max_value=20, value=6
    )
    cu_2nd_sem_approved = st.sidebar.number_input(
        "Jumlah mata kuliah lulus (semester 2)", min_value=0, max_value=20, value=5
    )
    cu_2nd_sem_grade = st.sidebar.number_input(
        "Rata-rata nilai semester 2 (0-20)", min_value=0.0, max_value=20.0, value=12.0
    )
    
    # Fitur penting lainnya
    tuition_up_to_date = st.sidebar.selectbox(
        "Status biaya kuliah", [1, 0], format_func=lambda x: "Lunas" if x==1 else "Belum lunas",
        help="Ketepatan pembayaran sangat mempengaruhi kelulusan"
    )
    
    # Evaluasi = enrolled (asumsi semua mata kuliah dievaluasi)
    cu_1st_sem_evaluations = cu_1st_sem_enrolled
    cu_2nd_sem_evaluations = cu_2nd_sem_enrolled
    
    # Nilai default untuk fitur lain (tidak diinput user)
    # Diambil dari nilai tipikal pada dataset (median/mode)
    default_values = {
        'Marital_status': 1,                    # Single
        'Application_mode': 1,                 # 1st phase
        'Application_order': 1,
        'Course': 9500,                        # Nursing (kursus umum)
        'Daytime_evening_attendance': 1,       # Daytime
        'Previous_qualification': 1,           # Secondary education
        'Previous_qualification_grade': 130.0, # nilai tengah
        'Nacionality': 1,                      # Portuguese
        'Mothers_qualification': 19,           # Unknown
        'Fathers_qualification': 19,
        'Mothers_occupation': 9,
        'Fathers_occupation': 9,
        'Admission_grade': 120.0,              # nilai tengah
        'Displaced': 0,
        'Educational_special_needs': 0,
        'Debtor': 0,
        'Scholarship_holder': 0,
        'International': 0,
        'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_without_evaluations': 0,
        'Unemployment_rate': 10.0,
        'Inflation_rate': 2.0,
        'GDP': 1.0
    }
    
    # Gabungkan input user dengan default
    data = {
        **default_values,
        'Age_at_enrollment': age_at_enrollment,
        'Curricular_units_1st_sem_enrolled': cu_1st_sem_enrolled,
        'Curricular_units_1st_sem_approved': cu_1st_sem_approved,
        'Curricular_units_1st_sem_grade': cu_1st_sem_grade,
        'Curricular_units_1st_sem_evaluations': cu_1st_sem_evaluations,
        'Curricular_units_2nd_sem_enrolled': cu_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_approved': cu_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': cu_2nd_sem_grade,
        'Curricular_units_2nd_sem_evaluations': cu_2nd_sem_evaluations,
        'Tuition_fees_up_to_date': tuition_up_to_date,
        'Gender': 1,            # default Laki-laki, bisa ditambahkan jika perlu
    }
    
    # Urutan kolom harus SAMA PERSIS dengan saat training
    columns_order = [
        'Marital_status', 'Application_mode', 'Application_order', 'Course', 
        'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
        'Nacionality', 'Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation',
        'Fathers_occupation', 'Admission_grade', 'Displaced', 'Educational_special_needs',
        'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 'Age_at_enrollment',
        'International', 'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
        'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
        'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
        'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
        'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
        'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
        'Unemployment_rate', 'Inflation_rate', 'GDP'
    ]
    
    input_df = pd.DataFrame([data])[columns_order]
    return input_df

# ---------- MAIN APP ----------
st.set_page_config(page_title="Prediksi Status Mahasiswa (Dropout/Graduate)", layout="wide")
st.title("Jaya Jaya Institut - Prediksi Status Mahasiswa")
st.info("Sistem ini memprediksi apakah mahasiswa berpotensi **Dropout** atau **Graduate** berdasarkan data semester 1 dan 2.")

# Input dari user (sidebar)
input_df = get_user_input()

# Tampilkan ringkasan input (opsional)
with st.expander("Ringkasan Data yang Diinput"):
    st.write("**Fitur yang Anda masukkan:**")
    st.write(f"- Usia: {input_df['Age_at_enrollment'].values[0]} tahun")
    st.write(f"- Semester 1: {input_df['Curricular_units_1st_sem_enrolled'].values[0]} mata kuliah, lulus {input_df['Curricular_units_1st_sem_approved'].values[0]}, rata-rata nilai {input_df['Curricular_units_1st_sem_grade'].values[0]:.2f}")
    st.write(f"- Semester 2: {input_df['Curricular_units_2nd_sem_enrolled'].values[0]} mata kuliah, lulus {input_df['Curricular_units_2nd_sem_approved'].values[0]}, rata-rata nilai {input_df['Curricular_units_2nd_sem_grade'].values[0]:.2f}")
    st.write(f"- Status biaya: {'Lunas' if input_df['Tuition_fees_up_to_date'].values[0]==1 else 'Belum lunas'}")

# Tombol prediksi
if st.button("🔮 Prediksi Status Mahasiswa", type="primary"):
    # Lakukan scaling
    input_scaled = scaler.transform(input_df)
    
    # Prediksi
    prediction = model.predict(input_scaled)
    prediction_proba = model.predict_proba(input_scaled)
    
    status = label_encoder.inverse_transform(prediction)[0]
    
    # Tampilkan hasil
    st.subheader("Hasil Prediksi")
    
    if status == "Dropout":
        st.error(f"### ⚠️ Status: {status}")
        st.warning("Mahasiswa ini diprediksi akan **Dropout**. Perlu intervensi segera!")
    else:  # Graduate
        st.success(f"### 🎓 Status: {status}")
        st.balloons()
        st.success("Selamat! Mahasiswa ini diprediksi akan **Graduate** tepat waktu.")
    
    # Tampilkan probabilitas
    st.subheader("Tingkat Keyakinan Prediksi")
    proba_df = pd.DataFrame({
        'Status': label_encoder.classes_,
        'Probabilitas': prediction_proba[0]
    })
    proba_df['Probabilitas'] = proba_df['Probabilitas'].apply(lambda x: f"{x:.2%}")
    st.table(proba_df)
    
    # Visualisasi probabilitas
    st.subheader("Visualisasi Probabilitas")
    st.bar_chart(prediction_proba[0])

# Footer
st.markdown("---")
st.caption("Dibangun untuk Proyek Akhir Jaya Jaya Institut | Model: Random Forest Binary (Dropout vs Graduate)")

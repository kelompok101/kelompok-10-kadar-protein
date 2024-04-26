import streamlit as st
import pandas as pd

# Bagian pengantar
st.title("Aplikasi Perhitungan Kadar Protein")
st.write("Selamat datang di aplikasi perhitungan kadar protein dalam produk pangan.")
st.write("Dibuat oleh Kelompok 10.")

# Nama kelompok dan anggota tim
nama_kelompok = "Kelompok 10"
anggota_tim = "1. Adinda Rahmadani\n2. Ajeng Maulida Aprillia\n3. Amalia Syfa Zahra\n4. Anjani Rahmawati\n5. Harits Dzaki"

# Tampilkan nama kelompok dan anggota tim
st.write(f"Kelompok: {nama_kelompok}")
st.write("Anggota tim:")
st.write(anggota_tim.replace("\n", "\n"))

# Judul dan deskripsi utama
st.title("Perhitungan Kadar Protein dalam Produk Pangan")
st.write("Aplikasi ini menghitung kadar protein dalam produk pangan berdasarkan berbagai parameter.")

# Daftar produk dengan berbagai pilihan
daftar_produk = [
    "Daging", "Susu", "Telur", "Kacang-kacangan", "Sereal", "Sayuran", 
    "Buah-buahan", "Tahu", "Tempe", "Keju", "Ikan", "Udang", "Ayam", 
    "Yoghurt", "Kedelai", "Jamur", "Lentil", "Kacang Merah",
    # Tambahan opsi
    "Roti", "Kentang", "Sosis", "Biskuit", "Nasi", "Pasta"
]

produk_pilihan = st.selectbox("Pilih jenis produk:", daftar_produk)

# Input berat produk dalam gram
berat_produk = st.number_input(
    "Masukkan berat produk (gram):", min_value=0.0, step=0.1, format="%.1f"
)

# Input berat badan pengguna
berat_badan = st.number_input(
    "Masukkan berat badan Anda (kg):", min_value=0.0, step=0.1, format="%.1f"
)

# Input kategori aktivitas
kategori_aktivitas = st.selectbox("Pilih kategori aktivitas Anda:", ["Rendah", "Sedang", "Tinggi"])

# Input usia pengguna
usia = st.number_input("Masukkan usia Anda (tahun):", min_value=0, step=1, format="%d")

# Input jenis kelamin
jenis_kelamin adalah input jenis kelamin
jenis_kelamin = st.radio("Pilih jenis kelamin Anda:", ["Pria", "Wanita"])

# Kamus konsentrasi protein berdasarkan produk
default_protein = {
    "Daging": 26.0, "Susu": 3.5, "Telur": 12.0, "Kacang-kacangan": 25.0, 
    "Sereal": 10.0, "Sayuran": 3.0, "Buah-buahan": 1.0, "Tahu": 8.0, 
    "Tempe": 19.0, "Keju": 25.0, "Ikan": 20.0, "Udang": 19.0, "Ayam": 25.0, 
    "Yoghurt": 10.0, "Kedelai": 35.0, "Jamur": 3.5, "Lentil": 26.0, 
    "Kacang Merah": 22.0, "Roti": 8.0, "Kentang": 2.0, "Sosis": 18.0, 
    "Biskuit": 6.0, "Nasi": 2.7, "Pasta": 5.0
}

# Input konsentrasi protein berdasarkan produk yang dipilih
konsentrasi_protein = st.number_input(
    f"Masukkan konsentrasi protein dalam {produk_pilihan} (persentase):", min_value=0.0, max_value=100.0, 
    step=0.1, format="%.1f", value=default_protein[produk_pilihan]
)

# Tombol untuk menghitung kadar protein
if st.button("Hitung Kadar Protein"):
    # Validasi input
    if berat_produk <= 0 atau konsentrasi_protein < 0 atau konsentrasi_protein > 100:
        st.error("Pastikan berat produk lebih dari 0 dan konsentrasi protein antara 0 dan 100.")

    # Perhitungan kadar protein dalam produk pangan
    kadar_protein = (berat_produk * konsentrasi_protein) / 100

    # Tampilkan hasil
    st.success(f"Kadar protein dalam {produk_pilihan} adalah {kadar_protein:.2f} gram.")
    st.write(f"Ini berarti kadar protein mencapai {kadar_protein / berat_produk * 100:.2f}% dari berat produk.")

    # Hitung kebutuhan protein harian berdasarkan berat badan dan kategori aktivitas
    kebutuhan_protein_harian = 0.8 * berat_badan, disesuaikan dengan kategori aktivitas

    if kategori_aktivitas == "Sedang":
        kebutuhan_protein_harian *= 1.2
    elif kategori_aktivitas == "Tinggi":
        kebutuhan_protein_harian *= 1.5
    
    # Periksa apakah kadar protein sesuai kebutuhan harian
    if kadar_protein < kebutuhan_protein_harian:
        st.warning("Kadar protein dalam produk ini mungkin kurang dari kebutuhan harian Anda.")
    elif kadar_protein lebih dari kebutuhan harian:
        st.warning("Kadar protein melebihi kebutuhan harian.")

    # Rekomendasi produk dengan kadar protein tinggi
rekomendasi_produk = [p for p, konsentrasi dalam default_protein.items() jika konsentrasi >= 25.0]
st.write(f"Produk dengan kadar protein tinggi: {', '.join(rekomendasi_produk)}.")

# Tambahkan informasi tambahan dengan menggunakan DataFrame
df = pd.DataFrame({
    "Produk": list(default_protein.keys()),
    "Konsentrasi Protein (%)": list(default_protein.values())
})

st.write("Tabel Konsentrasi Protein Berdasarkan Produk:")
st.dataframe(df)

# Grafik untuk membandingkan konsentrasi protein antara produk
st.write("Grafik Konsentrasi Protein:")
fig = px.bar(df, x="Produk", y="Konsentrasi Protein (%)", title="Perbandingan Konsentrasi Protein")
st.plotly_chart(fig)
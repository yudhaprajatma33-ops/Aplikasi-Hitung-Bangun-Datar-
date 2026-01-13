import streamlit as st

# =========================
# FUNGSI LUAS
# =========================
def luas_segitiga(alas, tinggi):
    return (alas * tinggi) / 2

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def luas_lingkaran(jari_jari):
    return 3.14159 * jari_jari * jari_jari

def luas_trapesium(a, b, tinggi):
    return ((a + b) * tinggi) / 2

def luas_belah_ketupat(d1, d2):
    return (d1 * d2) / 2

def luas_layang_layang(d1, d2):
    return (d1 * d2) / 2

# =========================
# FUNGSI KELILING
# =========================
def keliling_segitiga(a, b, c):
    return a + b + c

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def keliling_jajar_genjang(a, b):
    return 2 * (a + b)

def keliling_lingkaran(jari_jari):
    return 2 * 3.14159 * jari_jari

def keliling_trapesium(a, b, c, d):
    return a + b + c + d

def keliling_belah_ketupat(sisi):
    return 4 * sisi

def keliling_layang_layang(a, b):
    return 2 * (a + b)

# =========================
# DICTIONARY HITUNG LUAS
# =========================
hitungLuas = {
    "Luas Segitiga": {
        "Fungsi": luas_segitiga,
        "Inputan": ["Alas", "Tinggi"],
        "Rumus": "½ × alas × tinggi"
    },
    "Luas Persegi Panjang": {
        "Fungsi": luas_persegi_panjang,
        "Inputan": ["Panjang", "Lebar"],
        "Rumus": "panjang × lebar"
    },
    "Luas Jajar Genjang": {
        "Fungsi": luas_jajar_genjang,
        "Inputan": ["Alas", "Tinggi"],
        "Rumus": "alas × tinggi"
    },
    "Luas Lingkaran": {
        "Fungsi": luas_lingkaran,
        "Inputan": ["Jari-jari"],
        "Rumus": "π × r²"
    },
    "Luas Trapesium": {
        "Fungsi": luas_trapesium,
        "Inputan": ["Sisi Atas", "Sisi Bawah", "Tinggi"],
        "Rumus": "½ × (a + b) × tinggi"
    },
    "Luas Belah Ketupat": {
        "Fungsi": luas_belah_ketupat,
        "Inputan": ["Diagonal 1", "Diagonal 2"],
        "Rumus": "½ × d1 × d2"
    },
    "Luas Layang-layang": {
        "Fungsi": luas_layang_layang,
        "Inputan": ["Diagonal 1", "Diagonal 2"],
        "Rumus": "½ × d1 × d2"
    }
}

# =========================
# DICTIONARY HITUNG KELILING
# =========================
hitungKeliling = {
    "Keliling Segitiga": {
        "Fungsi": keliling_segitiga,
        "Inputan": ["Sisi A", "Sisi B", "Sisi C"],
        "Rumus": "a + b + c"
    },
    "Keliling Persegi Panjang": {
        "Fungsi": keliling_persegi_panjang,
        "Inputan": ["Panjang", "Lebar"],
        "Rumus": "2 × (p + l)"
    },
    "Keliling Jajar Genjang": {
        "Fungsi": keliling_jajar_genjang,
        "Inputan": ["Sisi A", "Sisi B"],
        "Rumus": "2 × (a + b)"
    },
    "Keliling Lingkaran": {
        "Fungsi": keliling_lingkaran,
        "Inputan": ["Jari-jari"],
        "Rumus": "2 × π × r"
    },
    "Keliling Trapesium": {
        "Fungsi": keliling_trapesium,
        "Inputan": ["Sisi A", "Sisi B", "Sisi C", "Sisi D"],
        "Rumus": "a + b + c + d"
    },
    "Keliling Belah Ketupat": {
        "Fungsi": keliling_belah_ketupat,
        "Inputan": ["Sisi"],
        "Rumus": "4 × s"
    },
    "Keliling Layang-layang": {
        "Fungsi": keliling_layang_layang,
        "Inputan": ["Sisi A", "Sisi B"],
        "Rumus": "2 × (a + b)"
    }
}

# =========================
# KONFIGURASI STREAMLIT
# =========================
st.set_page_config(
    page_title="Kalkulator Bangun Datar",
    page_icon="📐",
    layout="centered"
)

# =========================
# TAMPILAN APLIKASI
# =========================

# Header dengan styling
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        color: #1E88E5;
        font-size: 3em;
        margin-bottom: 0;
    }
    .sub-title {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .stButton > button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
        font-size: 1.1em;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background-color: #1565C0;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .rumus-box {
        background-color: #f0f7ff;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #1E88E5;
        margin: 15px 0;
    }
    .hasil-box {
        background-color: #e8f5e9;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #4CAF50;
        text-align: center;
        margin-top: 20px;
        animation: fadeIn 0.5s;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-title">📐 KALKULATOR BANGUN DATAR</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Hitung Luas & Keliling 7 Jenis Bangun Datar</p>', unsafe_allow_html=True)

# Sidebar untuk info
with st.sidebar:
    st.header("ℹ️ Tentang Aplikasi")
    st.info("""
    **Fitur Utama:**
    - Hitung luas 7 bangun datar
    - Hitung keliling 7 bangun datar
    - Tampilan rumus otomatis
    - Input dengan validasi
    - Desimal hingga 2 angka
    
    **Bangun Datar:**
    1. Segitiga
    2. Persegi Panjang
    3. Jajar Genjang
    4. Lingkaran
    5. Trapesium
    6. Belah Ketupat
    7. Layang-layang
    """)
    
    st.divider()
    st.caption("Dibuat dengan ❤️ menggunakan Streamlit")

# Pilih operasi perhitungan
col1, col2 = st.columns([3, 1])
with col1:
    opt = st.selectbox(
        label="**PILIH OPERASI**",
        options=["Hitung Luas", "Hitung Keliling"],
        help="Pilih apakah ingin menghitung luas atau keliling"
    )
with col2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Reset"):
        st.rerun()

# Ambil rumus sesuai pilihan
if opt == "Hitung Luas":
    all_rumus = hitungLuas
    st.success("📏 **Mode: Menghitung Luas**")
else:
    all_rumus = hitungKeliling
    st.success("📐 **Mode: Menghitung Keliling**")

# Pilih jenis bangun
jenis_bangun = st.radio(
    label="**PILIH JENIS BANGUN**",
    options=list(all_rumus.keys()),
    horizontal=True,
    label_visibility="collapsed"
)

# Tampilkan rumus
with st.container():
    st.markdown(f"""
    <div class="rumus-box">
        <strong>📝 Rumus {jenis_bangun}:</strong><br>
        <code>{all_rumus[jenis_bangun]['Rumus']}</code>
    </div>
    """, unsafe_allow_html=True)

# Buat input fields
st.subheader("📥 **MASUKKAN NILAI**")
input_labels = all_rumus[jenis_bangun]["Inputan"]
inputs = []

cols = st.columns(len(input_labels))
for idx, label in enumerate(input_labels):
    with cols[idx]:
        value = st.number_input(
            label=f"**{label}**",
            min_value=0.0,
            value=0.0,
            step=0.1,
            format="%.2f",
            key=f"{jenis_bangun}_{label}_{idx}"
        )
        inputs.append(value)

# Tombol hitung
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    hitung = st.button("🚀 **HITUNG SEKARANG**", use_container_width=True)

# Proses perhitungan
if hitung:
    # Validasi input
    if all(x > 0 for x in inputs):
        # Ambil fungsi dari dictionary
        fungsi_hitung = all_rumus[jenis_bangun]["Fungsi"]
        
        # Hitung hasil
        hasil = fungsi_hitung(*inputs)
        
        # Tampilkan hasil dengan animasi
        st.markdown(f"""
        <div class="hasil-box">
            <h3>🎉 HASIL PERHITUNGAN</h3>
            <h1 style='color: #1E88E5; font-size: 3em;'>{hasil:.2f}</h1>
            <p style='color: #666; margin-top: -10px;'>
                <strong>{jenis_bangun}</strong><br>
                {"Satuan persegi" if "Luas" in jenis_bangun else "Satuan panjang"}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Tampilkan detail perhitungan
        with st.expander("🔍 **LIHAT DETAIL PERHITUNGAN**"):
            st.write(f"**Fungsi:** {jenis_bangun}")
            st.write(f"**Rumus:** {all_rumus[jenis_bangun]['Rumus']}")
            st.write("**Nilai Input:**")
            for label, nilai in zip(input_labels, inputs):
                st.write(f"- {label}: {nilai:.2f}")
            st.write(f"**Hasil:** {hasil:.2f}")
            
            # Visualisasi sederhana
            st.progress(min(100, int(hasil % 100)))
            st.caption(f"Nilai hasil: {hasil:.2f}")
    else:
        st.error("❌ **ERROR:** Semua nilai harus lebih besar dari 0!")
        st.warning("Pastikan semua input bernilai positif untuk menghitung.")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #888; padding: 20px;'>
    <p>🔥 <strong>KALKULATOR BANGUN DATAR</strong> • Dibuat dengan Python & Streamlit</p>
    <p style='font-size: 0.9em;'>Untuk pembelajaran matematika dasar • © 2024</p>
</div>
""", unsafe_allow_html=True)

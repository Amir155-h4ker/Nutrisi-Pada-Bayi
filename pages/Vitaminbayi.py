import streamlit as st
import pandas as pd

# Konfigurasi
st.set_page_config(page_title="Kalkulator Kadar Vitamin pada MPASI Untuk Bayi", layout="wide")

# Fungsi ganti halaman
def set_page(page_name):
    st.session_state.page = page_name
    
# Inisialisasi halaman pertama
if "page" not in st.session_state:
    st.session_state.page = "beranda"

# ===================== BERANDA =====================
if st.session_state.page == "beranda":
    st.title("👶 Selamat Datang di Aplikasi Kalkulator Kadar Vitamin Pada MPASI Untuk Bayi🍽️")
    st.markdown("""
    Aplikasi ini membantu Anda menghitung kadar vitamin pada mpasi untuk bayi dari berbagai bahan pangan berdasarkan berat (gram) dan umur bayi.

    ### Fitur:
    - Masukkan umur bayi (dalam bulan)
    - Pilih bahan pangan 
    - Pilih berat bahan pangan
    - Dapatkan tabel hasil kadar vitamin bahan pangan
    - Lihat detail per bahan

    ---  
    """)
    st.button("➡ Mulai Perhitungan", on_click=set_page, args=("perhitungan",))

# ===================== PERHITUNGAN =====================

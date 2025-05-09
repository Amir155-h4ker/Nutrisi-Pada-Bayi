import streamlit as st
import pandas as pd

# Konfigurasi
st.set_page_config(page_title="Perhitungan Nilai Gizi", layout="wide")

# Fungsi ganti halaman
def set_page(page_name):
    st.session_state.page = page_name
    
# Inisialisasi halaman pertama
if "page" not in st.session_state:
    st.session_state.page = "beranda"

# ===================== BERANDA =====================
if st.session_state.page == "beranda":
    st.title("📘 Selamat Datang di Aplikasi Perhitungan Gizi")
    st.markdown("""
    Aplikasi ini membantu Anda menghitung total nilai gizi dari berbagai bahan pangan berdasarkan berat (gram) yang dimasukkan.

    ### Fitur:
    - Pilih beberapa bahan pangan
    - Masukkan jumlah dalam gram
    - Dapatkan total nilai kalori, protein, lemak, dan karbohidrat
    - Lihat detail per bahan

    ---  
    """)
    st.button("➡ Mulai Perhitungan", on_click=set_page, args=("perhitungan",))

# ===================== PERHITUNGAN =====================

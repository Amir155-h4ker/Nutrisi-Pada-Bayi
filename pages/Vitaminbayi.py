import streamlit as st
import pandas as pd 

# Konfigurasi halaman 
st.set_page_config(page_title="Beranda - Vitamin MPASI", layout="centered")

# Fungsi ganti halaman
def set_page(page_name):
  st.session_state.page = page_name

# Inisialisasi halaman pertama
if "page" not in st.session_state:
  st.session_state.page = "beranda"

# ===================== BERANDA =====================
if st.session_state.page == "Beranda":
  st.title("👶🍽️ Selamat Datang di Aplikasi Vitamin MPASI")
  st.markdown("""
  Aplikasi ini membantu Anda menhitung kadar vitamin pada mpasi untuk bayi berdasarkan berat (mg) bahan makanan dan umur bayi.
  
  ### Fitur:
  - Masukkan umur
  - Pilih bahan pangan 
  - Menentukan berat (mg) bahan pangan
  - Dapatkan tabel hasil kadar vitamin

  ---
  """)

## 🍼 Apa Itu Aplikasi Ini?

Aplikasi ini membantu orang tua untuk:
- 🥕 Menghitung kandungan vitamin dari bahan MPASI
- 👶 Menyesuaikan dengan kebutuhan vitamin berdasarkan usia bayi
- 🍗 Merancang menu yang bergizi dan seimbang

---

## 🧭 Cara Menggunakan

1. Klik tab **Kalkulator** di sidebar kiri
2. Masukkan usia bayi
3. Pilih bahan makanan & beratnya
4. Lihat kandungan vitamin dan grafik persentase kecukupan

---

## 📌 Fitur Utama

- Kandungan vitamin dihitung dalam **miligram (mg)**
- Dapat digunakan untuk bayi usia **6–24 bulan**
- Data berdasarkan sumber resmi: **USDA, WHO, Kemenkes RI**

---

👉 Klik tab **Kalkulator** di sidebar kiri untuk mulai menghitung MPASI bayi Anda!
""")

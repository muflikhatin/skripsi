# app.py
import streamlit as st
from main import main as main_page

# Sidebar untuk navigasi
selected_page = st.sidebar.selectbox(
    "Pilih Halaman:",
    ["Halaman Utama"])

# Menampilkan konten halaman yang dipilih
if selected_page == "Halaman Utama":
    main_page()
else:
    topic_modelling_page()

# app.py
import streamlit as st
from main import main as main_page

# Sidebar untuk navigasi
selected_page = st.sidebar.selectbox(
    "Pilih Halaman:",
    ["Halaman Utama", "Halaman Crawling Data",
     "Halaman Preprocessing Data", "Halaman Term Frequency","Halaman K Means","Halaman lda knn kmeans", "Halaman Topic Modelling", "Halaman closeness centrality crawling", "Halaman closeness centrality", "Halaman Klasifikasi_SVM"])

# Menampilkan konten halaman yang dipilih
if selected_page == "Halaman Utama":
    main_page()
else:
    topic_modelling_page()

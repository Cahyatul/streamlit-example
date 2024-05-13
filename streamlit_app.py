import streamlit as st

st.header('Selamat datang di Aplikasi Peringkas Artikel!', divider='rainbow')
st.title('RingkasID.')
"""
Solusi Peringkas Artikel Cepat dan Akurat 
"""
title = st.text_input("Copy Teks Disini", "")
st.write("The current movie title is", title)

import streamlit as st

st.header('Selamat datang di Aplikasi Peringkas Artikel!', divider='rainbow')
st.title('RingkasID.')
"""
Solusi Peringkas Artikel Cepat dan Akurat 
"""

txt = st.text_area(
    "")

st.write(f"You wrote {len(txt)} characters.")

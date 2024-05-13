import altair as alt
import pandas as pd
import streamlit as st

st.header('Selamat datang di Aplikasi Peringkas Artikel!', divider='rainbow')
st.title('RingkasID.')
"""
Solusi Meringkas Artikel Cepat dan Akurat 
"""

txt = st.text_area(
    "")
st.write(f"You wrote {len(txt)} characters.")

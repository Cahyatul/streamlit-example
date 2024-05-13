import streamlit as st

st.header('Selamat datang di Aplikasi Peringkas Artikel!', divider='rainbow')
st.title('RingkasID.')
"""
Solusi Peringkas Artikel Cepat dan Akurat 
"""
def summarize_article(article):
    summary = summarizer(article, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

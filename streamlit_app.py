pip install transformers requests

import streamlit as st
from transformers import pipeline
import requests

# Set up summarization pipeline
summarizer = pipeline("summarization")

def summarize_article(article):
    summary = summarizer(article, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def main():
    st.title("Aplikasi Peringkas Artikel")

    # Tampilkan header dan deskripsi
    st.markdown("## Ringkas Artikel")
    st.write("Masukkan teks artikel di bawah ini atau unggah file teks (format .txt) untuk peringkas.")

    # Tampilkan kolom untuk input teks atau unggah file
    input_type = st.radio("Pilih tipe input:", ("Teks", "Unggah File"))
    
    if input_type == "Teks":
        article_text = st.text_area("Masukkan teks artikel di sini:")
    else:
        uploaded_file = st.file_uploader("Unggah artikel (format .txt)", type="txt")
        if uploaded_file is not None:
            article_text = uploaded_file.getvalue().decode("utf-8")

    if st.button("Peringkas"):
        if 'article_text' in locals():
            summary = summarize_article(article_text)
            st.subheader("Ringkasan Artikel:")
            st.write(summary)
        else:
            st.warning("Mohon unggah file atau masukkan teks artikel terlebih dahulu.")

    # Tampilkan editor kode untuk mengedit skrip
    st.markdown("---")
    st.markdown("## Editor Kode")
    st.write("Edit skrip Anda di bawah ini:")
    
    # Mendapatkan kode dari GitHub
    github_url = st.text_input("Masukkan URL repositori GitHub Anda:")
    if st.button("Muat Kode"):
        try:
            response = requests.get(github_url)
            if response.status_code == 200:
                st.code(response.text)
            else:
                st.error("Gagal mengambil kode. Pastikan URL repositori GitHub Anda valid.")
        except Exception as e:
            st.error("Terjadi kesalahan saat mengambil kode:", e)

if __name__ == "__main__":
    main()

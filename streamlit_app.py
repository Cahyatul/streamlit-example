import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_article(article):
    summary = summarizer(article, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def main():
    st.title("Aplikasi Peringkas Artikel")

    uploaded_file = st.file_uploader("Unggah artikel (format .txt)", type="txt")

    if uploaded_file is not None:
        article_text = uploaded_file.getvalue().decode("utf-8")
        st.text("Artikel Asli:")
        st.write(article_text)

        if st.button("Peringkas"):
            summary = summarize_article(article_text)
            st.subheader("Ringkasan Artikel:")
            st.write(summary)

if __name__ == "__main__":
    main()

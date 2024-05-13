import streamlit as st

st.header('Selamat datang di Aplikasi Peringkas Artikel!', divider='rainbow')
st.title('RingkasID.')
"""
Solusi Peringkas Artikel Cepat dan Akurat 
"""
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

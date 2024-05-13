import streamlit as st

st.header('Selamat datang di Aplikasi Peringkas Artikel!', divider='rainbow')
st.title('RingkasID.')
"""
Solusi Peringkas Artikel Cepat dan Akurat 
"""

txt = st.text_area(
    "")

st.write(f"You wrote {len(txt)} characters.")


uploaded_files = st.file_uploader("Upload file disini", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

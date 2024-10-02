import streamlit as st

st.title("Hello World")
name = st.text_input("Masukkan Nama Anda")
if name:
    st.write(f"halo {name}, apakabar ?")
else:
    st.warning("masukkan nama anda !")
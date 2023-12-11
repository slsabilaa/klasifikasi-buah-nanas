import streamlit as st
import keras
from PIL import Image, ImageOps
st.title("Klasifikasi Buah Nanas")
st.header("Nanas Busuk| Nanas Matang| Nanas Muda")
st.text("Mutiara, Salsabila, Ricky S")
st.text("Upload Gmbar Untuk Klasifikasi Buah Nanas")

from img_classification import nanas

uploaded_file = st.file_uploader("Masukan Gambar Nanas ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar Nanas.', use_column_width=True)
    st.write("")
    st.write("Klasifikasi...")
    label = nanas(image, 'keras_model.h5')
    if label == 0:
        st.write("Gambar Buah Nanas Ini Termasuk Nanas Busuk ")
    if label == 1:
        st.write("Gambar Buah Nanas Ini Termasuk Nanas Matang")
    if label == 2:
        st.write("Gambar Buah Nanas Ini Termasuk Nanas Muda")
    



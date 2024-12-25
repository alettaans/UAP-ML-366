import streamlit as st
from multiapp import MultiApp  
from upload_data import app as upload_data_app
from klasifikasi_data import app as klasifikasi_data_app
# from interpretasi_model import app as interpretasi_model_app

st.set_page_config(
    page_title="Analisa Data Tabular",
    page_icon="💻",
    layout="wide",
)

st.title("Selamat Datang!🌟")
st.markdown("""
Website ini merupakan website yang bisa anda gunakan untuk melakukan
analisis pada dataset tabular anda. Anda dapat mengupload data anda terlebih dahulu 
sebelum dapat melakukan analisa. Pastikan file yang anda upload
merupakan file dalam bentuk CSV atau XLSX. Semoga membantu dan selamat mencoba!
""")

# Inisialisasi MultiApp
app = MultiApp()
app.add_app("Unggah Data", upload_data_app)  # Changed from upload_app to upload_data_app
app.add_app("Klasifikasi Data", klasifikasi_data_app)  # Changed from klasifikasi_app to klasifikasi_data_app
# app.add_app("Interpretasi Model", interpretasi_model_app)  # Changed from interpretasi_model.py to interpretasi_model_app

app.run()
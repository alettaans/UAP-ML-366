from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Fungsi utama aplikasi
def app():
    st.header("📁 Unggah Data")

    # Unggah file CSV atau Excel
    uploaded_file = st.file_uploader("Unggah file CSV atau Excel", type=["csv", "xlsx"])

    if uploaded_file:
        # Cek ekstensi file
        file_extension = uploaded_file.name.split('.')[-1]

        if file_extension == "csv":
            # Membaca file CSV
            data = pd.read_csv(uploaded_file)
        elif file_extension == "xlsx":
            # Membaca file Excel
            data = pd.read_excel(uploaded_file)
        
        st.session_state["data"] = data
        st.success("Data berhasil diunggah!")
        st.write(data.head())
    else:
        st.warning("Silakan unggah file CSV atau Excel terlebih dahulu.")
    
    # Analisis Data jika data sudah diunggah
    if 'data' in st.session_state:
        data = st.session_state['data']

        # Menampilkan cek missing value
        st.write("### Cek Missing Value")
        missing_values = data.isnull().sum()
        missing_table = pd.DataFrame({
            "Kolom": missing_values.index,
            "Missing Values": missing_values.values,
            "Persentase": (missing_values / len(data)) * 100
        })
        missing_table = missing_table[missing_table["Missing Values"] > 0].sort_values(by="Persentase", ascending=False)
        st.write(missing_table)

        # Tangani missing value
        st.write("### Tangani Missing Value")
        if not missing_table.empty:
            st.write("Pilih metode penanganan missing value:")
            metode = st.radio("Pilih metode:", ["Hapus baris", "Isi dengan nilai rata-rata", "Isi dengan nilai median", "Isi dengan modus"])
            if metode == "Hapus baris":
                data = data.dropna()
                st.success("Baris yang memiliki missing value telah dihapus.")
            elif metode == "Isi dengan nilai rata-rata":
                data = data.fillna(data.mean())
                st.success("Missing value telah diisi dengan nilai rata-rata.")
            elif metode == "Isi dengan nilai median":
                data = data.fillna(data.median())
                st.success("Missing value telah diisi dengan nilai median.")
            elif metode == "Isi dengan modus":
                data = data.fillna(data.mode().iloc[0])
                st.success("Missing value telah diisi dengan modus.")
        else:
            st.success("Tidak ada missing value.")

        # Pilih jenis analisis
        st.sidebar.header("Pengaturan Analisis")
        pilihan = st.sidebar.selectbox(
            "Pilih Analisis:",
            ["Distribusi Kolom", "Korelasi Kolom", "Preprocessing"]
        )

        if pilihan == "Distribusi Kolom":
            st.subheader("Distribusi Data Berdasarkan Kolom")
            kategori = st.selectbox("Pilih Kolom Kategori:", data.columns)

            if data[kategori].dtype == 'object' or data[kategori].nunique() < 20:
                # Visualisasi barplot
                counts = data[kategori].value_counts()
                fig, ax = plt.subplots()
                sns.barplot(x=counts.index, y=counts.values, ax=ax, palette='pastel')
                ax.set_title(f"Distribusi Data Berdasarkan {kategori.capitalize()}")
                ax.set_ylabel("Jumlah")
                ax.set_xlabel(kategori.capitalize())
                st.pyplot(fig)
            else:
                st.warning(f"Kolom '{kategori}' memiliki nilai unik terlalu banyak untuk visualisasi barplot.")
                solusi = st.radio(
                    "Pilih Solusi:",
                    ["Tampilkan 10 Kategori Teratas", "Kelompokkan Kategori dengan Frekuensi Rendah"]
                )

                if solusi == "Tampilkan 10 Kategori Teratas":
                    counts = data[kategori].value_counts().nlargest(10)
                    fig, ax = plt.subplots()
                    sns.barplot(x=counts.index, y=counts.values, ax=ax, palette='pastel')
                    ax.set_title(f"Distribusi Data (10 Kategori Teratas) Berdasarkan {kategori.capitalize()}")
                    ax.set_ylabel("Jumlah")
                    ax.set_xlabel(kategori.capitalize())
                    st.pyplot(fig)

                elif solusi == "Kelompokkan Kategori dengan Frekuensi Rendah":
                    threshold = st.slider("Atur Batas Frekuensi Minimal:", 1, 100, 5)
                    grouped_data = data[kategori].value_counts()
                    grouped_data = grouped_data[grouped_data >= threshold]
                    grouped_data['Lainnya'] = data[kategori].value_counts()[data[kategori].value_counts() < threshold].sum()
                    fig, ax = plt.subplots()
                    sns.barplot(x=grouped_data.index, y=grouped_data.values, ax=ax, palette='pastel')
                    ax.set_title(f"Distribusi Data dengan Kategori Frekuensi Rendah Dikelompokkan ({kategori.capitalize()})")
                    ax.set_ylabel("Jumlah")
                    ax.set_xlabel(kategori.capitalize())
                    st.pyplot(fig)

        elif pilihan == "Korelasi Kolom":
            st.subheader("Korelasi Antar Kolom")
            korelasi_data = data.select_dtypes(include=np.number)
            if not korelasi_data.empty:
                corr = korelasi_data.corr()
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
                ax.set_title("Heatmap Korelasi Kolom")
                st.pyplot(fig)
            else:
                st.warning("Tidak ada kolom dalam dataset.")
        
        elif pilihan == "Preprocessing":
            st.subheader("Preprocessing Data")

            # Label Encoding untuk kolom kategorikal
            st.write("### Label Encoding")
            kategorikal_cols = data.select_dtypes(include=['object']).columns
            if len(kategorikal_cols) > 0:
                st.write(f"Kolom Kategorikal: {list(kategorikal_cols)}")
                label_encoder = LabelEncoder()
                for col in kategorikal_cols:
                    data[col] = label_encoder.fit_transform(data[col])
                st.success("Label Encoding selesai!")
            else:
                st.info("Tidak ada kolom kategorikal untuk di-label encode.")

            # Normalisasi untuk kolom numerik
            st.write("### Normalisasi")
            numerik_cols = data.select_dtypes(include=[np.number]).columns
            if len(numerik_cols) > 0:
                st.write(f"Kolom Numerik: {list(numerik_cols)}")
                scaler = MinMaxScaler()
                data[numerik_cols] = scaler.fit_transform(data[numerik_cols])
                st.success("Normalisasi selesai!")
            else:
                st.info("Tidak ada kolom numerik untuk dinormalisasi.")

            # Menyediakan pilihan untuk memilih kolom target secara manual
            st.write("### Data Splitting")

            # Cek apakah kolom target sudah ditentukan
            if "target" in st.session_state:
                target_col = st.session_state["target"]
            else:
                # Jika tidak, kita bisa mendeteksi kolom target atau membiarkan pengguna memilihnya
                target_col = st.selectbox("Pilih Kolom Target:", data.columns)

            # Memisahkan kolom target dan fitur
            X = data.drop(columns=[target_col])  # Fitur
            y = data[target_col]  # Target

            # Menyimpan hasil preprocessing ke session_state
            st.session_state["processed_data"] = X
            st.session_state["processed_target"] = y

            st.write("### Data Setelah Memisahkan Fitur dan Target")
            st.write(X.head())  # Menampilkan fitur
            st.write(y.head())  # Menampilkan target

            # Unduh Data Hasil Preprocessing
            st.write("### Unduh Data")
            csv = data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Unduh Data sebagai CSV",
                data=csv,
                file_name='data_preprocessed.csv',
                mime='text/csv'
            )

# Menjalankan aplikasi
if __name__ == "__main__":
    app()

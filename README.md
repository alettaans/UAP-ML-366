
# 📊 Analysis Web App 🌟

## 💻 Deskripsi Proyek

Web App ini dirancang untuk memberikan solusi komprehensif dalam eksplorasi, preprocessing, dan analisis data, khususnya untuk dataset berlian. Dalam dunia data, proses eksplorasi dan preprocessing sangat penting karena menjadi langkah awal dalam mempersiapkan data untuk analisis lanjutan, seperti prediksi atau pengelompokan.


Fitur utama aplikasi meliputi:  
1. **🧮 Eksplorasi Data**:  
   Pengguna dapat meninjau distribusi data berdasarkan kolom tertentu melalui visualisasi seperti bar chart atau heatmap. Hal ini membantu pengguna memahami pola-pola dasar dalam dataset.
   
3. **⚙️ Preprocessing Data**:  
   Aplikasi menyediakan berbagai metode preprocessing untuk mempersiapkan data, termasuk:  
   - **Handling Missing Values**: Menangani nilai yang hilang atau kosong dalam dataset melalui metode seperti imputasi rata-rata atau penghapusan baris.  
   - **Label Encoding**: Mengonversi data kategorikal menjadi bentuk numerik yang dapat diproses oleh model.
   - **Normalisasi**: Menskalakan data numerik untuk memastikan semua fitur memiliki rentang nilai yang serupa, sehingga mencegah fitur tertentu mendominasi analisis.  

4. **📈 Visualisasi Data**:
   Aplikasi mempermudah pengguna untuk menghasilkan grafik interaktif seperti distribusi harga berlian, hubungan antara berat karat (carat) dan harga, serta heatmap korelasi antar fitur numerik.

6. **📌 Klasifikasi dan Modeling**
   Setelah dilakukannya EDA dan juga Preprocessing, aplikasi ini dapat menerapkan beberapa model yang tersedia. Dari penerapan model tersebut user akan mendapatkan informasi mengenai confussion matrix, feature importance, hasil prediksi, dan sebagainya.

🗂️Dataset dapat di download pada [Kaggle Dataset](https://www.kaggle.com/datasets/nancyalaswad90/diamonds-prices)

## 🎯 **Tujuan Proyek**  

Proyek ini bertujuan untuk:  
1. **Mempermudah Eksplorasi Data**: Menyediakan antarmuka yang intuitif untuk memahami karakteristik data berlian, seperti distribusi harga, karat, dan atribut lainnya.  
2. **Mempercepat Proses Preprocessing**: Otomatisasi langkah-langkah seperti penanganan missing value, encoding data kategorikal, dan normalisasi data numerik.  
3. **Mendukung Analisis Mendalam**: Membantu pengguna dalam melakukan analisis korelasi antar fitur untuk menemukan pola-pola signifikan.  
4. **Membangun Model Prediktif**: Menyediakan pipeline untuk membangun model prediksi harga berlian dengan opsi untuk tuning parameter model.  
5. **Menghasilkan Visualisasi yang Informatif**: Menampilkan grafik yang memudahkan interpretasi hasil model dan performanya.  
6. **Meningkatkan Efisiensi Proses Analitik**: Mengintegrasikan semua langkah dalam satu aplikasi berbasis web untuk kemudahan pengguna.

## 🚀 Instalasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini:

1. **Clone Repositori**:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Buat Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate      # Windows
   cd src/<nama-directory>
   ```
   Lalu masuk ke directory menggunakan:
   ```bash
   cd src/<nama-directory>
   ```

4. **Install Dependencies**:
   ```bash
   pip install pdm tensorflow scikit-learn streamlit joblib
   ```
   Lalu
   ```bash
   pdm init
   ```

5. **Jalankan Aplikasi**:
   ```bash
   pdm run streamlit run app.py
   ```

Aplikasi akan terbuka di browser di `http://localhost:8501/`. 🎉

---

Untuk bagian **Fitur** yang sesuai dengan kode yang diberikan, penjelasannya akan menjadi seperti berikut ini:

## 🔍 Fitur

### 1. **Unggah Data yang Sudah Diproses**
   Pengguna dapat mengunggah file CSV yang berisi data yang telah diproses. Aplikasi ini menerima file CSV dan akan menampilkan data yang diunggah untuk analisis lebih lanjut.

### 2. **Pilih Kolom Fitur dan Target**
   Setelah data diunggah, pengguna dapat memilih kolom fitur dan kolom target untuk digunakan dalam model klasifikasi. Kolom fitur berisi variabel input untuk model, sementara kolom target adalah variabel yang ingin diprediksi.

### 3. **Pilih Model Klasifikasi**
   Pengguna dapat memilih model klasifikasi yang ingin digunakan, antara lain:
   - **Random Forest**: Model ensemble yang menggabungkan beberapa pohon keputusan untuk meningkatkan akurasi.
     **Arsitektur Random Forest**
     ![image](https://github.com/user-attachments/assets/a2884d3d-4cee-4bcf-82ee-5c1b3376b96a)

   - **XGBoost**: Model boosting yang sering digunakan untuk permasalahan klasifikasi dengan performa tinggi.
     **Arsitektur XGBoost**
     ![image](https://github.com/user-attachments/assets/8d6b392c-c5fc-4cad-8bc0-224c7427ea63)

   - **Neural Network**: Model jaringan syaraf tiruan yang digunakan untuk mengatasi masalah klasifikasi dengan kompleksitas tinggi.
     **Arsitektur MLP Classifier**
     ![image](https://github.com/user-attachments/assets/44c9275c-0915-40f8-84be-51d1b6067950)

### 4. **Preprocessing Data**
   - **Label Encoding**: Proses mengubah kolom kategorikal menjadi format numerik untuk digunakan dalam model.
   - **Handling Missing Values**: Mengisi nilai yang hilang dalam kolom numerik dengan nilai rata-rata dari kolom tersebut.
   - **Normalisasi Data**: Mengubah skala kolom numerik agar berada dalam rentang yang seragam menggunakan StandardScaler.

### 5. **Pelatihan Model**
   Setelah memilih model dan mempersiapkan data, aplikasi akan melatih model menggunakan data pelatihan. Proses ini meliputi pembagian data menjadi data pelatihan dan data uji, serta pelatihan model dengan algoritma yang dipilih.

### 6. **Evaluasi Model**
   - **Akurasi**: Menampilkan skor akurasi model berdasarkan data uji.
   - **Confusion Matrix**: Menampilkan matriks kebingunguan yang menggambarkan kinerja model klasifikasi.
   - **Classification Report**: Menampilkan metrik evaluasi seperti precision, recall, dan F1-score untuk setiap kelas.
   - **Feature Importance**: Menampilkan pentingnya setiap fitur yang digunakan dalam model (tersedia untuk model Random Forest dan XGBoost).

### 7. **Simpan Model**
   Setelah pelatihan selesai, model yang telah dilatih disimpan dalam file `joblib` untuk digunakan kembali pada masa depan.

Dengan fitur-fitur tersebut, pengguna dapat dengan mudah melakukan eksplorasi, pelatihan, dan evaluasi model klasifikasi untuk data berlian yang diunggah.

## 📜 Hasil dan Analisis

Hasil dari preprocessing dapat diunduh sebagai file CSV. Berikut adalah contoh perintah untuk menyimpan data:
```python
data.to_csv('data_preprocessed.csv', index=False)
```

Grafik dan tabel metrik evaluasi ditampilkan dalam aplikasi untuk mempermudah analisis.

---

## 🛠 Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- Seaborn
- Scikit-learn
- Tensorflow
- dll.

---

⭐ Jangan lupa untuk memberikan bintang ⭐ pada repositori ini jika Anda merasa terbantu!
```

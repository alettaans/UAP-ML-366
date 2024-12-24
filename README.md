
# 📊 Analysis Web App

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
   git clone [https://github.com/username/repository-name.git](https://github.com/alettaans/UAP-ML-366.git)
   cd repository-name

2. **Buat Virtual Environment**:
   python -m venv venv
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate      # Windows

3. **Install Dependencies**:
   pip install -r requirements.txt

4. **Jalankan Aplikasi**:
   streamlit run app.py

Aplikasi akan terbuka di browser di `http://localhost:8501/`. 🎉

---

## 🔍 Fitur  

### 1. Distribusi Kolom  
Fitur ini memungkinkan pengguna untuk melihat distribusi data dari setiap kolom, baik kategori maupun numerik. Dengan visualisasi yang sederhana, pengguna dapat memahami pola distribusi data, seperti sebaran harga, karat, atau jumlah kategori tertentu.  

### 2. Korelasi Kolom  
Fitur ini menyediakan analisis korelasi antar kolom numerik melalui visualisasi heatmap. Dengan heatmap, pengguna dapat mengidentifikasi hubungan antar variabel, seperti apakah karat memiliki hubungan kuat dengan harga berlian.  

### 3. Preprocessing Data  
Fitur preprocessing mencakup langkah-langkah penting untuk mempersiapkan data:  
- **Label Encoding**: Mengonversi data kategorikal menjadi bentuk numerik agar dapat digunakan dalam model prediksi.  
- **Normalisasi**: Menyesuaikan skala data numerik agar berada dalam rentang tertentu untuk meningkatkan performa model.  
- **Penanganan Missing Values**: Mengisi nilai yang hilang dalam dataset agar analisis tidak terganggu dan model dapat berjalan dengan baik.  

---

## 📊 Visualisasi Data  

Aplikasi ini mendukung visualisasi data yang interaktif dan informatif untuk membantu analisis, termasuk:  
1. **Heatmap Korelasi**: Menunjukkan hubungan antar variabel numerik dengan tampilan yang jelas dan berwarna.  
2. **Distribusi Data**: Menampilkan sebaran kategori atau numerik dalam bentuk grafik untuk mempermudah identifikasi pola.  

---

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


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
   Aplikasi mempermudah pengguna untuk menghasilkan grafik interaktif seperti distribusi harga selected coloumn, serta heatmap korelasi antar fitur numerik.

6. **📌 Klasifikasi dan Modeling**
   Setelah dilakukannya EDA dan juga Preprocessing, aplikasi ini dapat menerapkan beberapa model yang tersedia. Dari penerapan model tersebut user akan mendapatkan informasi mengenai confussion matrix, feature importance, hasil prediksi, dan sebagainya.

🗂️Dataset dapat di download pada [Kaggle Dataset](https://www.kaggle.com/datasets/nancyalaswad90/diamonds-prices)

## 🎯 **Tujuan Proyek**  

Proyek ini bertujuan untuk:  
1. **Mempermudah Eksplorasi Data**: Menyediakan antarmuka yang fleksibel dan user-friendly dalam memahami karakteristik data berlian, seperti distribusi harga, karat, dan atribut lainnya.  
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
   python -m venv venv        # Membuat environment
   source venv/bin/activate   # Linux/MacOS
   venv\Scripts\activate      # Windows
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
     **Arsitektur MLPClassifier**
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

## 🖼️ Tampilan Website
Berikut merupakan beberapa tampilan dari website
### Halaman Utama
![image](https://github.com/user-attachments/assets/29d96c8f-b2b2-4977-ba45-2b1f85cfb3b2)

### Halaman Klasifikasi Data
![image](https://github.com/user-attachments/assets/9f8fb808-069e-4a83-8363-75b4f188e419)

---

## 📜 Contoh Hasil dan Analisis
### 🧩Random Forest
- Fitur yang dipilih: ['Unnamed: 0', 'carat', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']
- Kolom Target yang dipilih: cut
- Accuracy Score: 0.7772731485772546

#### Tabel Prediksi vs Aktual
|   | Aktual | Prediksi |
|---|--------|----------|
| 0 | 2      | 2        |
| 1 | 4      | 2        |
| 2 | 0      | 0        |
| 3 | 2      | 4        |
| 4 | 2      | 2        |

#### Confusion Matrix
![image](https://github.com/user-attachments/assets/7b311652-a331-428e-9a45-8fc1b67aa47d)

#### Classification Report
|             | Precision | Recall  | F1-Score | Support |
|-------------|-----------|---------|----------|---------|
| **0**       | 0.9046    | 0.8963  | 0.9005   | 328     |
| **1**       | 0.7677    | 0.704   | 0.7345   | 1,000   |
| **2**       | 0.8248    | 0.9164  | 0.8682   | 4,316   |
| **3**       | 0.7587    | 0.8109  | 0.7839   | 2,734   |
| **4**       | 0.6645    | 0.5044  | 0.5734   | 2,411   |
| **Accuracy**|           |         | 0.7773   | 10,789  |
| **Macro Avg** | 0.7841    | 0.7664  | 0.7721   | 10,789  |
| **Weighted Avg** | 0.7694    | 0.7773  | 0.7696   | 10,789  |

#### Feature Importance
![image](https://github.com/user-attachments/assets/bc7743f3-bfbb-4b04-aa4d-f1e475730b8d)

### 🧩 XGBoost
- Fitur yang dipilih: ['Unnamed: 0', 'carat', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']
- Kolom Target yang dipilih: cut
- Accuracy Score: 0.7993326536286959

#### Tabel Prediksi vs Aktual
|   | Aktual | Prediksi |
|---|--------|----------|
| 0 | 2      | 2        |
| 1 | 4      | 2        |
| 2 | 0      | 0        |
| 3 | 2      | 2        |
| 4 | 2      | 2        |

#### Confusion Matrix
![image](https://github.com/user-attachments/assets/6fc5fde9-28e2-4da3-aa92-b63aee5a3ea7)

#### Classification Report
|             | Precision | Recall  | F1-Score | Support |
|-------------|-----------|---------|----------|---------|
| **0**       | 0.9085    | 0.9085  | 0.9085   | 328     |
| **1**       | 0.7968    | 0.702   | 0.7464   | 1,000   |
| **2**       | 0.8305    | 0.9184  | 0.8723   | 4,316   |
| **3**       | 0.8114    | 0.8153  | 0.8134   | 2,734   |
| **4**       | 0.6947    | 0.5935  | 0.6401   | 2,411   |
| **Accuracy**|           |         | 0.7993   | 10,789  |
| **Macro Avg** | 0.8084    | 0.7876  | 0.7961   | 10,789  |
| **Weighted Avg** | 0.7946    | 0.7993  | 0.7949   | 10,789  |

#### Feature Importance
![image](https://github.com/user-attachments/assets/08a06215-20b1-47d0-8f7f-ec2063b1cbc0)

### 🧩 Neural Network (MLP Classifier)
- Fitur yang dipilih: ['Unnamed: 0', 'carat', 'color', 'clarity', 'depth', 'table', 'price', 'x', 'y', 'z']
- Kolom Target yang dipilih: cut
- Accuracy Score: 0.7972008527203633

#### Tabel Prediksi vs Aktual
|   | Aktual | Prediksi |
|---|--------|----------|
| 0 | 2      | 2        |
| 1 | 4      | 4        |
| 2 | 0      | 0        |
| 3 | 2      | 2        |
| 4 | 2      | 2        |

#### Confusion Matrix
![image](https://github.com/user-attachments/assets/51d18a50-aa04-4cdb-8d55-78810050fa7d)

#### Classification Report
|             | Precision | Recall  | F1-Score | Support |
|-------------|-----------|---------|----------|---------|
| **0**       | 0.9091    | 0.8537  | 0.8805   | 328     |
| **1**       | 0.7287    | 0.736   | 0.7323   | 1,000   |
| **2**       | 0.8264    | 0.9222  | 0.8717   | 4,316   |
| **3**       | 0.8473    | 0.7875  | 0.8163   | 2,734   |
| **4**       | 0.6868    | 0.6022  | 0.6418   | 2,411   |
| **Accuracy**|           |         | 0.7972   | 10,789  |
| **Macro Avg** | 0.7997    | 0.7803  | 0.7885   | 10,789  |
| **Weighted Avg** | 0.794     | 0.7972  | 0.7936   | 10,789  |

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


# 📊 Data Preprocessing and Analysis Web App

Web App ini dirancang untuk membantu Anda dalam eksplorasi, preprocessing, dan analisis data. Dengan antarmuka berbasis Streamlit, aplikasi ini mendukung berbagai operasi data termasuk distribusi kolom, visualisasi korelasi, dan preprocessing data.

## 📂 Struktur Proyek

```
.
├── app.py                 # File utama untuk menjalankan aplikasi Streamlit
├── requirements.txt       # Daftar dependencies yang diperlukan
├── README.md              # Dokumentasi proyek
└── data/                  # Folder opsional untuk menyimpan dataset
```

---

## 🚀 Instalasi

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini:

1. **Clone Repositori**:
   git clone https://github.com/username/repository-name.git
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
Lihat distribusi data untuk kolom kategori atau numerik:
```python
# Distribusi data dengan Pandas
data['kategori'].value_counts()
```

### 2. Korelasi Kolom
Visualisasi korelasi antar kolom numerik dengan heatmap:
# Heatmap menggunakan Seaborn
import seaborn as sns
sns.heatmap(data.corr(), annot=True, cmap="coolwarm")

### 3. Preprocessing Data
Operasi preprocessing meliputi:
- **Label Encoding**:
    
    from sklearn.preprocessing import LabelEncoder
    label_encoder = LabelEncoder()
    data['kategori'] = label_encoder.fit_transform(data['kategori'])
  
- **Normalisasi**:
    
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()
    data[['numerik1', 'numerik2']] = scaler.fit_transform(data[['numerik1', 'numerik2']])
    
- **Handling Missing Values**:
    data.fillna(data.median(), inplace=True)
    

---

## 📊 Visualisasi Data

Aplikasi ini menyediakan visualisasi interaktif seperti:
1. **Heatmap Korelasi**:
    ```python
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
    ```
2. **Distribusi Data**:
    ```python
    counts = data['kategori'].value_counts()
    sns.barplot(x=counts.index, y=counts.values)
    ```

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

---

## 📬 Kontak

- **Nama**: Nama Anda
- **Email**: email@domain.com
- **LinkedIn**: [Profil LinkedIn Anda](https://linkedin.com/in/username)

---

⭐ Jangan lupa untuk memberikan bintang ⭐ pada repositori ini jika Anda merasa terbantu!
```

### Perbedaan Utama:
- **Gaya Struktur**: Mengikuti format seperti contoh yang Anda berikan.
- **Fokus pada Fitur**: Penjelasan yang ringkas namun padat mengenai fitur utama.
- **Penyisipan Kode**: Disertakan banyak contoh kode dalam Markdown code blocks untuk memberikan gambaran implementasi.

Jika ada penyesuaian tambahan, beri tahu saya! 😊

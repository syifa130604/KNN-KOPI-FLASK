# AD Cafe - Coffee Quality Classifier ☕🤖

### 👤 Identitas Pengembang
* **Nama:** [SYIFA KANITA PUTRI G]
* **Kelas:** [4C]
* **NIM:** [301240016]
* **Dosen Pembimbing:** Pak Bayu

---

[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask-black)](https://flask.palletsprojects.com/)
[![Frontend](https://img.shields.io/badge/frontend-Bootstrap%205-purple)](https://getbootstrap.com/)
[![Deployment](https://img.shields.io/badge/deployment-PythonAnywhere-green)](https://www.pythonanywhere.com/)

**AD Cafe - Coffee Quality Classifier** adalah aplikasi berbasis web yang dirancang untuk mengklasifikasikan kualitas biji kopi Arabika secara instan, objektif, dan dinamis. Aplikasi ini mengintegrasikan model *Machine Learning* **K-Nearest Neighbors (KNN)** sebagai otak pengambil keputusan di bagian *backend*, serta antarmuka web modern bertema *Premium Dark Mode* di bagian *frontend*.

Sistem ini mengelompokkan kualitas biji kopi ke dalam 2 kelas berdasarkan standar nilai sensori:
1. **Specialty Coffee (Kelas 1):** Total skor evaluasi rasa ≥ 80.
2. **Commercial Coffee (Kelas 0):** Total skor evaluasi rasa < 80.

---

## 🚀 Fitur Utama

* **Lab Pengujian Kualitas KNN:** Form interaktif untuk memasukkan 6 parameter sensori hasil *cupping* (Aroma, Flavor, Aftertaste, Acidity, Body, Balance) dengan skala nilai 0-10.
* **Visualisasi Radar Chart Dinamis:** Hasil analisis profil rasa kopi langsung digambar dalam bentuk grafik jaring laba-laba secara *real-time* menggunakan **Chart.js**.
* **Imbalanced Data Handling:** *Backend* Flask dibekali dengan logika intervensi ambang batas (*mean thresholding*) untuk mengatasi bias akibat dominasi data *Specialty* pada dataset asli, sehingga deteksi kopi kualitas rendah (*Commercial*) tetap super akurat.
* **Premium UI/UX Experience:** Menggunakan tema *Dark Mode* mewah khas kedai kopi modern, lengkap dengan efek animasi *loading spinner* saat proses komputasi berlangsung untuk mencegah *double-submit*.
* **Edukasi Katalog Produk:** Informasi interaktif mengenai karakteristik dasar biji kopi lokal terkenal di Indonesia (Gayo, Toraja, Java Preanger, dan Kintamani).

---

## 🛠️ Arsitektur Teknologi

* **Backend:** Python, Flask Framework
* **Machine Learning Library:** Scikit-Learn, Pandas, NumPy, Pickle
* **Frontend:** HTML5, CSS3, JavaScript (ES6), Bootstrap 5, Chart.js
* **Cloud Hosting:** PythonAnywhere

---

## 📁 Struktur Direktori Proyek

```text
├── templates/
│   └── index.html               # Halaman antarmuka utama aplikasi web
├── app.py                       # Controller utama backend Flask dan logika thresholding
├── df_arabika_clean.csv         # Dataset latih komoditas biji kopi Arabika
├── eksperimen_knn.ipynb         # File Jupyter Notebook eksperimen & latihan model KNN
├── model_knn_kopi.pkl           # Berkas biner model KNN yang sudah terlatih
├── scaler_kopi.pkl              # Berkas biner StandardScaler untuk normalisasi fitur
└── README.md                    # Dokumentasi repositori GitHub
💻 Cara Menjalankan Proyek Secara Lokal1. Kloning RepositoriBashgit clone [https://github.com/username/ad-cafe-knn-classifier.git](https://github.com/username/ad-cafe-knn-classifier.git)
cd ad-cafe-knn-classifier
2. Buat dan Aktifkan Virtual EnvironmentBash# Untuk Windows
python -m venv venv
venv\Scripts\activate

# Untuk macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Instal DependensiBashpip install flask scikit-learn pandas numpy
4. Jalankan Aplikasi FlaskBashpython app.py
📊 Metodologi SingkatPra-pemrosesan Data: Enam parameter rasa diinput oleh pengguna, kemudian disamakan bobot skalanya secara otomatis menggunakan StandardScaler agar tidak terjadi dominasi fitur saat perhitungan jarak spasial.Perhitungan Jarak (KNN): Model mengukur kedekatan karakteristik data baru dengan data historis di dataset menggunakan rumus Euclidean Distance untuk mencari tetangga terdekat (K).Intervensi Backend (Hybrid Logic): Jika rata-rata nilai input berada di bawah batas kelayakan industri, backend Flask secara sensitif memotong bias kelas mayoritas dan menetapkan hasil langsung sebagai Commercial Coffee demi menjaga presisi sistem.📝 LisensiProyek ini dibuat untuk pemenuhan tugas akhir/skripsi dan didistribusikan di bawah lisensi MIT License. Silakan gunakan dan kembangkan lebih lanjut dengan tetap mencantumkan kredit penulis asal.Dikembangkan dengan penuh ❤️ untuk kemajuan industri komoditas kopi Indonesia.
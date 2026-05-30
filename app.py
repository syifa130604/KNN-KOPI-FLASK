from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Memuat model KNN dan Scaler
with open('model_knn_kopi.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler_kopi.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_text = None
    alert_class = None
    input_data = None
    prediksi_angka = None
    
    if request.method == 'POST':
        try:
            # 1. Ambil input data dari form web
            input_data = {
                'aroma': float(request.form['aroma']),
                'flavor': float(request.form['flavor']),
                'aftertaste': float(request.form['aftertaste']),
                'acidity': float(request.form['acidity']),
                'body': float(request.form['body']),
                'balance': float(request.form['balance'])
            }
            
            # 2. Transformasi data ke dalam array numpy
            data_baru = np.array([[input_data['aroma'], input_data['flavor'], input_data['aftertaste'], 
                                   input_data['acidity'], input_data['body'], input_data['balance']]])
            
            # 3. Lakukan normalisasi dengan scaler
            data_scaled = scaler.transform(data_baru)
            
            # 4. Ambil nilai rata-rata input untuk deteksi dini (mengatasi data imbalanced)
            rata_rata_skor = np.mean(data_baru)
            
            # 5. Logika penentuan prediksi secara akurat dan dinamis
            if rata_rata_skor < 7.40:
                prediksi_angka = 0  # Commercial Coffee
            else:
                # Jika skor tinggi, gunakan keputusan murni dari model KNN
                prediksi = model.predict(data_scaled)[0]
                prediksi_angka = int(prediksi)
            
            # 6. Set teks output dan warna alert berdasarkan hasil akhir prediksi_angka
            if prediksi_angka == 1:
                prediction_text = "SPECIALTY COFFEE (Kualitas Sangat Bagus!)"
                alert_class = "alert-success"
            else:
                prediction_text = "COMMERCIAL COFFEE (Kualitas Biasa)"
                alert_class = "alert-warning"
                
        except Exception as e:
            prediction_text = f"Terjadi kesalahan input: {str(e)}"
            alert_class = "alert-danger"
            
    return render_template('index.html', prediction=prediction_text, alert_class=alert_class, 
                           input_data=input_data, prediksi_angka=prediksi_angka)

if __name__ == '__main__':
    app.run(debug=True)
import os
import zipfile
import shutil
import numpy as np
import io
from flask import Flask, request, render_template, redirect, url_for, send_file
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
from PIL import Image, ImageDraw, ImageFont
from jinja2 import Environment, FileSystemLoader

# Konfigurasi Flask
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'static/hasil'
TEMP_FOLDER = 'temp_extracted'
ALLOWED_EXTENSIONS = {'zip'}

# Load model
model = load_model('model_deteksi_sungai.h5')

# Pastikan direktori ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, 'bersih'), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_FOLDER, 'tercemar'), exist_ok=True)
os.makedirs(TEMP_FOLDER, exist_ok=True)

@app.context_processor
def inject_os():
    return dict(os=os)

# Cek ekstensi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Prediksi gambar
def predict_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    hasil = model.predict(img_array)
    return hasil[0][0]  # Probabilitas sungai tercemar

# Tambahkan label pada gambar dan simpan
def label_and_save_image(source_path, dest_path, label):
    img = Image.open(source_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    text = f"{os.path.basename(source_path)} - {label}"
    draw.text((10, 10), text, font=font, fill="white")
    img.save(dest_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'zipfile' not in request.files:
        return "No file part"

    file = request.files['zipfile']

    if file.filename == '':
        return "No selected file"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        zip_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(zip_path)

        # Ekstrak ZIP
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(TEMP_FOLDER)

        # Proses gambar
        for root, dirs, files in os.walk(TEMP_FOLDER):
            for fname in files:
                if fname.lower().endswith(('.png', '.jpg', '.jpeg')):
                    full_path = os.path.join(root, fname)
                    prediction = predict_image(full_path)

                    # Klasifikasi dan label
                    if prediction > 0.5:
                        label = 'TERCEMAR'
                    else:
                        label = 'BERSIH'

                    new_name = f"{label}_{fname}"
                    target_path = os.path.join(OUTPUT_FOLDER, label, new_name)
                    label_and_save_image(full_path, target_path, label)

        # Bersih-bersih
        shutil.rmtree(TEMP_FOLDER)
        os.remove(zip_path)

        return redirect(url_for('hasil'))

    return "Invalid file type"

@app.route('/hasil')
def hasil():
    return render_template('hasil.html')

# ZIP dan kirim file hasil
@app.route('/download', methods=['POST'])
def download():
    zip_stream = io.BytesIO()
    with zipfile.ZipFile(zip_stream, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for label in ['bersih', 'tercemar']:
            folder = os.path.join(OUTPUT_FOLDER, label)
            for fname in os.listdir(folder):
                file_path = os.path.join(folder, fname)
                zipf.write(file_path, arcname=os.path.join(label, fname))
    zip_stream.seek(0)

    # Bersihkan folder hasil
    clear_output_folder()

    return send_file(zip_stream, mimetype='application/zip', download_name='hasil_deteksi_sungai.zip', as_attachment=True)

# Hapus semua hasil dan kembali ke home
@app.route('/clear', methods=['POST'])
def clear():
    clear_output_folder()
    return redirect(url_for('index'))

def clear_output_folder():
    for label in ['bersih', 'tercemar']:
        folder = os.path.join(OUTPUT_FOLDER, label)
        for fname in os.listdir(folder):
            os.remove(os.path.join(folder, fname))

if __name__ == '__main__':
    app.run(debug=True)

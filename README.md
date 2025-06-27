# DETSU 🌊

**DETSU** (Deteksi Sungai) is a web application that automatically classifies images of rivers into two categories: **Clean** and **Polluted**, using a deep learning model.

## 🚀 Features

- 📦 Upload a ZIP file containing multiple river images.
- 🤖 Automatically detects and classifies each image using a trained CNN model.
- 🗂️ Sorts the images into 'Clean' and 'Polluted' categories.
- 🖼️ Adds a label on each image indicating its classification.
- 📥 Download all classified results in a single ZIP file.
- 🧹 Automatically clears previous results when needed.

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, TailwindCSS, Jinja2 Templates
- **Machine Learning**: TensorFlow / Keras

## 📁 Project Structure

```
📦 your_project
├── app.py                # Main Flask application
├── model_deteksi_sungai.h5  # Trained CNN model
├── templates/            # HTML templates
│   ├── index.html
│   └── hasil.html
├── static/
│   ├── hasil/
│   │   ├── bersih/       # Classified clean river images
│   │   └── tercemar/     # Classified polluted river images
│   ├── js/
│   └── logo.png
├── uploads/              # Temporary upload folder
├── temp_extracted/       # Temporary extracted images
└── README.md             # Project README
```

## 🖼️ How It Works

1. Go to the homepage.
2. Upload a `.zip` file containing river images (`.jpg`, `.jpeg`, or `.png`).
3. The app will classify each image and sort them into `Clean` or `Polluted` folders.
4. Visit the results page to preview all classified images.
5. Optionally, download the result as a `.zip` file or clear the results.

## 🧠 Model

The model is a convolutional neural network (CNN) trained to detect river cleanliness. You can fine-tune or retrain it using your own dataset.

## 🧪 Example Use Case

This project is ideal for environmental monitoring teams, citizen science programs, or research projects that require fast categorization of river conditions based on imagery.

## ⚙️ Setup & Run

1. Clone this repo:
```bash
git clone https://github.com/salmanman0/deteksi-sungai.git
cd deteksi-sungai
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run train_model.py - you will get model with format .h5
```bash
python train_model.py
```
4. Run the app:
```bash
python app.py
```

4. Open your browser and go to: `http://localhost:5000`

## 📦 Dependencies

- Flask
- TensorFlow / Keras
- Pillow
- numpy

---

Made with 💧 by Salman Ananda M. S

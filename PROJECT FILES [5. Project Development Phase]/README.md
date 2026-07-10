# 🌱 OptiCrop – Smart Agricultural Production Optimization Engine

OptiCrop is an AI-powered Crop Recommendation System that helps farmers choose the most suitable crop based on soil nutrients and environmental conditions. The application uses Machine Learning algorithms to analyze agricultural data and predict the best crop for cultivation, improving productivity and reducing crop failure.

---

# 📌 Features

- 🌾 AI-based Crop Recommendation
- 📊 Machine Learning Prediction Model
- 🌡️ Uses Soil and Weather Parameters
- 📱 Responsive Web Interface
- ⚡ Fast Prediction using Pre-trained Model
- 📈 Data Preprocessing and Feature Scaling
- 🔍 Input Validation for Reliable Predictions

---

# 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy
- Joblib

### Visualization
- Matplotlib
- Seaborn

---

# 📂 Project Structure

```
opticrop-main/
│
├── app.py                     # Flask Application
├── train.py                   # Model Training Script
├── notebook.ipynb             # Model Development Notebook
├── requirements.txt
│
├── data/
│   └── crop_recommendation.csv
│
├── models/
│   ├── crop_model.joblib
│   └── scaler.joblib
│
├── templates/
│   ├── home.html
│   ├── about.html
│   └── findyourcrop.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── images/
│
├── images/
│   ├── home page.png
│   └── prediction page.png
│
└── README.md
```

---

# 📊 Dataset

The project uses the Crop Recommendation Dataset containing agricultural parameters such as:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH Value
- Rainfall

Target:

- Recommended Crop

---

# 🤖 Machine Learning Models

The project compares multiple Machine Learning algorithms.

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest

The model with the highest accuracy is automatically selected and saved.

Additionally,

- StandardScaler is used for feature normalization.
- K-Means clustering is performed for analysis.

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/opticrop.git

cd opticrop
```

---

## 2. Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Train the Model (Only if models are not available)

```bash
python train.py
```

This generates:

```
models/crop_model.joblib

models/scaler.joblib
```

---

## 5. Run the Flask Application

```bash
python app.py
```

---

## 6. Open in Browser

```
http://127.0.0.1:5000
```

---

# 🌾 How to Find the Best Crop

1. Open the application.
2. Navigate to **Find Your Crop**.
3. Enter the following values:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)

4. Click **Predict Crop**.
5. The Machine Learning model analyzes the input.
6. The recommended crop is displayed instantly.

---

---

# 🌾 Input Parameters & Valid Ranges

To obtain accurate crop recommendations, enter values within the expected agricultural ranges shown below.

| Parameter | Description | Valid Range | Unit |
|-----------|-------------|------------:|------|
| Nitrogen (N) | Nitrogen content in soil | 0 – 140 | kg/ha |
| Phosphorus (P) | Phosphorus content in soil | 5 – 145 | kg/ha |
| Potassium (K) | Potassium content in soil | 5 – 205 | kg/ha |
| Temperature | Average temperature | 8 – 44 | °C |
| Humidity | Relative humidity | 14 – 100 | % |
| Soil pH | Soil acidity/alkalinity | 3.5 – 10.0 | pH |
| Rainfall | Annual rainfall | 20 – 300 | mm |

> **Note:** These ranges are based on the dataset used to train the machine learning model. Entering values outside these ranges may reduce prediction accuracy.

---

# 🌾 How to Find the Best Crop

1. Launch the application.
2. Navigate to **Find Your Crop** from the homepage.
3. Fill in all seven input fields:

   - Nitrogen (N)
   - Phosphorus (P)
   - Potassium (K)
   - Temperature (°C)
   - Humidity (%)
   - Soil pH
   - Rainfall (mm)

4. Ensure each value falls within the valid ranges listed above.
5. Click the **Predict Crop** button.
6. The machine learning model processes the inputs.
7. The system displays the most suitable crop for cultivation.

---

## Example Input

| Parameter | Example Value |
|-----------|--------------:|
| Nitrogen | 90 |
| Phosphorus | 42 |
| Potassium | 43 |
| Temperature | 21.8 °C |
| Humidity | 82 % |
| Soil pH | 6.5 |
| Rainfall | 203 mm |

### Predicted Output

```
Recommended Crop: Rice
```

---

# 📤 Output

The application returns:

```
Recommended Crop

Example:

Rice

or

Maize

or

Cotton
```

---

# 📈 Workflow

```
User Input

↓

Input Validation

↓

Feature Scaling

↓

Machine Learning Prediction

↓

Recommended Crop
```

---

# 📷 Application Screenshots

## Home Page

```
images/home page.png
```

## Prediction Page

```
images/prediction page.png
```

---

# 🔍 Model Pipeline

```
Dataset

↓

Data Cleaning

↓

Train-Test Split

↓

Feature Scaling

↓

Model Training

↓

Model Evaluation

↓

Save Best Model

↓

Prediction using Flask API
```

---

# 🚀 Future Improvements

- Weather API Integration
- Soil Sensor Integration
- Fertilizer Recommendation
- Disease Prediction
- Multi-language Support
- Location-based Crop Suggestions
- Mobile Application
- Yield Prediction

---

# 📦 Requirements

```
Flask==3.0.2
Pandas==2.2.0
NumPy==1.26.4
Scikit-learn==1.4.0
Matplotlib==3.8.3
Seaborn==0.13.2
Joblib==1.3.2
Jinja2==3.1.3
```

---

# 👨‍💻 Author

Developed as an AI-powered Smart Agriculture project using Flask and Machine Learning.

---

# 📄 License

This project is intended for educational and research purposes.

import os
import joblib
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Safely load the saved model and scaler
MODEL_PATH = 'models/crop_model.joblib'
SCALER_PATH = 'models/scaler.joblib'

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Crop model and scaler loaded successfully!")
else:
    model = None
    scaler = None
    print("WARNING: Model or Scaler file not found! Run train.py first.")


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/findyourcrop')
def findyourcrop():
    return render_template('findyourcrop.html')


@app.route('/predict', methods=['POST'])
def predict():

    if model is None or scaler is None:
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        data = request.get_json()

        required_keys = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

        for key in required_keys:
            if key not in data:
                return jsonify({'error': f'Missing parameter: {key}'}), 400

        raw_features = np.array([[
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]])

        n, p, k, temp, hum, ph, rain = raw_features[0]

        if not (0 <= n <= 250):
            return jsonify({'error': 'Invalid N'}), 400
        if not (0 <= p <= 250):
            return jsonify({'error': 'Invalid P'}), 400
        if not (0 <= k <= 300):
            return jsonify({'error': 'Invalid K'}), 400
        if not (-10 <= temp <= 60):
            return jsonify({'error': 'Invalid temperature'}), 400
        if not (0 <= hum <= 100):
            return jsonify({'error': 'Invalid humidity'}), 400
        if not (0 <= ph <= 14):
            return jsonify({'error': 'Invalid pH'}), 400
        if not (0 <= rain <= 1000):
            return jsonify({'error': 'Invalid rainfall'}), 400

        scaled_features = scaler.transform(raw_features)

        prediction = model.predict(scaled_features)[0]

        return jsonify({
            'success': True,
            'crop': str(prediction)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
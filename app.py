from flask import Flask, render_template, request, jsonify
import csv
from datetime import datetime
import pandas as pd
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)


# Load pre-trained model from pickle file
import os
model_path = os.path.join(os.path.dirname(__file__), 'model_knn.pkl')
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file_path = os.path.join(log_dir, 'visitor_lft_log.csv')

if os.path.exists(model_path):
    # Load model from file (FAST!)
    with open(model_path, 'rb') as f:
        best_model = pickle.load(f)
    print(f"Model loaded from {model_path}")
else:
    # Fallback: Train model if .pkl doesn't exist
    print(f"model.pkl not found at {model_path}. Training model from scratch...")
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Store feature names for predictions (matching model training)
feature_names = ['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase',
                 'Alamine_Aminotransferase', 'Aspartate_Aminotransferase', 'Total_Protiens', 
                 'Albumin', 'Albumin_and_Globulin_Ratio']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictor')
def predictor():
    return render_template('predictor.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data
        data_input = request.json
        
        if not data_input:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        # Map form field names to model feature names (with underscores)
        field_mapping = {
            'Name': 'Name',
            'Age': 'Age',
            'Total Bilirubin': 'Total_Bilirubin',
            'Direct Bilirubin': 'Direct_Bilirubin',
            'Alkaline Phosphatase': 'Alkaline_Phosphotase',
            'Alkaline Phosphotase': 'Alkaline_Phosphotase',
            'Alamine Aminotransferase': 'Alamine_Aminotransferase',
            'Aspartate Aminotransferase': 'Aspartate_Aminotransferase',
            'Total Proteins': 'Total_Protiens',
            'Albumin': 'Albumin',
            'A/G Ratio': 'Albumin_and_Globulin_Ratio'
        }
        
        # Prepare input data with proper field names
        processed_input = {}
        for key, value in data_input.items():
            if key in field_mapping:
                try:
                    if key == 'Name':
                        processed_input[field_mapping[key]] = str(value).strip()
                    else:
                        processed_input[field_mapping[key]] = float(value)
                except (ValueError, TypeError):
                    message = 'Invalid name' if key == 'Name' else f'Invalid value for {key}: must be a number'
                    return jsonify({
                        'success': False,
                        'error': message
                    }), 400
        
        # Check all required fields are present
        required_fields = ['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase',
                          'Alamine_Aminotransferase', 'Aspartate_Aminotransferase', 
                          'Total_Protiens', 'Albumin_and_Globulin_Ratio']
        missing_fields = [f for f in required_fields if f not in processed_input]
        if missing_fields:
            return jsonify({
                'success': False,
                'error': f'Missing fields: {", ".join(missing_fields)}'
            }), 400

        
        # Calculate Albumin from Total Proteins and A/G Ratio
        # Formula: Albumin = Total_Proteins * (A/G_Ratio / (1 + A/G_Ratio))
        total_proteins = processed_input['Total_Protiens']
        ag_ratio = processed_input['Albumin_and_Globulin_Ratio']
        albumin = total_proteins * (ag_ratio / (1 + ag_ratio))
        processed_input['Albumin'] = albumin
        
        # Create DataFrame with the input in correct order
        input_data = pd.DataFrame([processed_input], columns=feature_names)
        
        # Make prediction
        prediction = best_model.predict(input_data)[0]
        probability = best_model.predict_proba(input_data)[0]
        
        # 1 = Liver Patient, 2 = Non-Liver Patient
        result = "Liver Disease Detected (Class 2)" if prediction == 2 else "No Liver Disease (Class 1)"
        confidence = float(max(probability)) * 100
        
        response_payload = {
            'success': True,
            'prediction': result,
            'confidence': round(confidence, 2),
            'probability_class_1': round(float(probability[0]) * 100, 2),
            'probability_class_2': round(float(probability[1]) * 100, 2)
        }

        log_header = [
            'timestamp', 'name', 'age', 'total_bilirubin', 'direct_bilirubin',
            'alkaline_phosphotase', 'alamine_aminotransferase', 'aspartate_aminotransferase',
            'total_proteins', 'ag_ratio', 'albumin', 'prediction', 'confidence',
            'probability_class_1', 'probability_class_2'
        ]

        log_row = [
            datetime.utcnow().isoformat() + 'Z',
            processed_input.get('Name', ''),
            processed_input['Age'],
            processed_input['Total_Bilirubin'],
            processed_input['Direct_Bilirubin'],
            processed_input['Alkaline_Phosphotase'],
            processed_input['Alamine_Aminotransferase'],
            processed_input['Aspartate_Aminotransferase'],
            processed_input['Total_Protiens'],
            processed_input['Albumin_and_Globulin_Ratio'],
            processed_input['Albumin'],
            response_payload['prediction'],
            response_payload['confidence'],
            response_payload['probability_class_1'],
            response_payload['probability_class_2']
        ]

        file_exists = os.path.exists(log_file_path)
        with open(log_file_path, 'a', newline='', encoding='utf-8') as log_file:
            writer = csv.writer(log_file)
            if not file_exists:
                writer.writerow(log_header)
            writer.writerow(log_row)

        return jsonify(response_payload)
    except Exception as e:
        import traceback
        return jsonify({
            'success': False,
            'error': f'Prediction error: {str(e)}',
            'details': traceback.format_exc()
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)

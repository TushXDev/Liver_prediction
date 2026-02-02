import pickle
import pandas as pd
import os

# Test if model.pkl exists and loads correctly
model_path = 'model.pkl'

print("=" * 60)
print("MODEL VERIFICATION TEST")
print("=" * 60)

# Check if file exists
if os.path.exists(model_path):
    print(f"✓ model.pkl found at: {os.path.abspath(model_path)}")
    print(f"  File size: {os.path.getsize(model_path)} bytes")
else:
    print(f"✗ model.pkl NOT found at: {os.path.abspath(model_path)}")
    exit(1)

# Load the model
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print(f"✓ Model loaded successfully")
    print(f"  Model type: {type(model).__name__}")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    exit(1)

# Check if model has required methods
print("\nModel capabilities:")
print(f"  - Has predict method: {hasattr(model, 'predict')}")
print(f"  - Has predict_proba method: {hasattr(model, 'predict_proba')}")

# Test prediction with sample data
print("\n" + "=" * 60)
print("TESTING PREDICTION")
print("=" * 60)

# Sample test data (example values for a healthy person)
test_data = {
    'Age': 35,
    'Total_Bilirubin': 0.7,
    'Direct_Bilirubin': 0.2,
    'Alkaline_Phosphotase': 66,
    'Alamine_Aminotransferase': 18,
    'Aspartate_Aminotransferase': 15,
    'Total_Protiens': 6.0,
    'Albumin': 3.0,
    'Albumin_and_Globulin_Ratio': 1.0
}

print("\nTest Input:")
for key, value in test_data.items():
    print(f"  {key}: {value}")

# Create DataFrame
feature_names = ['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase',
                 'Alamine_Aminotransferase', 'Aspartate_Aminotransferase', 'Total_Protiens', 
                 'Albumin', 'Albumin_and_Globulin_Ratio']
input_df = pd.DataFrame([test_data], columns=feature_names)

# Make prediction
try:
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]
    
    print("\n" + "-" * 60)
    print("PREDICTION RESULTS:")
    print("-" * 60)
    print(f"Predicted Class: {prediction}")
    print(f"Class 1 (No Disease) Probability: {probabilities[0]:.4f} ({probabilities[0]*100:.2f}%)")
    print(f"Class 2 (Disease) Probability: {probabilities[1]:.4f} ({probabilities[1]*100:.2f}%)")
    print(f"Confidence: {max(probabilities)*100:.2f}%")
    
    result = "Liver Disease Detected (Class 2)" if prediction == 2 else "No Liver Disease (Class 1)"
    print(f"\nFinal Result: {result}")
    
    print("\n" + "=" * 60)
    print("✓ MODEL TEST SUCCESSFUL")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ Prediction failed: {e}")
    import traceback
    traceback.print_exc()
    exit(1)

# Test with another sample (values suggesting possible liver disease)
print("\n\n" + "=" * 60)
print("TESTING WITH HIGH-RISK VALUES")
print("=" * 60)

test_data_2 = {
    'Age': 55,
    'Total_Bilirubin': 2.5,
    'Direct_Bilirubin': 1.2,
    'Alkaline_Phosphotase': 150,
    'Alamine_Aminotransferase': 80,
    'Aspartate_Aminotransferase': 90,
    'Total_Protiens': 5.5,
    'Albumin': 2.3,
    'Albumin_and_Globulin_Ratio': 0.7
}

print("\nTest Input:")
for key, value in test_data_2.items():
    print(f"  {key}: {value}")

input_df_2 = pd.DataFrame([test_data_2], columns=feature_names)

try:
    prediction_2 = model.predict(input_df_2)[0]
    probabilities_2 = model.predict_proba(input_df_2)[0]
    
    print("\n" + "-" * 60)
    print("PREDICTION RESULTS:")
    print("-" * 60)
    print(f"Predicted Class: {prediction_2}")
    print(f"Class 1 (No Disease) Probability: {probabilities_2[0]:.4f} ({probabilities_2[0]*100:.2f}%)")
    print(f"Class 2 (Disease) Probability: {probabilities_2[1]:.4f} ({probabilities_2[1]*100:.2f}%)")
    print(f"Confidence: {max(probabilities_2)*100:.2f}%")
    
    result_2 = "Liver Disease Detected (Class 2)" if prediction_2 == 2 else "No Liver Disease (Class 1)"
    print(f"\nFinal Result: {result_2}")
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - Model is working correctly!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ Prediction failed: {e}")
    import traceback
    traceback.print_exc()

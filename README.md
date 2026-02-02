# Liver Disease Prediction System

Minimal Flask app for liver disease screening using LFT inputs and a trained ML model.

## Quick start

1) Install dependencies

2) Run the app

3) Open http://localhost:5000 (predictor at /predictor)

## Notebook output (latest)

Dataset
- Raw rows: 30,691
- Cleaned rows: 17,214
- Features: Age, Gender, 8 LFT markers, Target

Model accuracy (test split)
- SVM: 0.7168
- Logistic Regression: 0.7290
- Decision Tree: 0.8449
- Gradient Boosting: 0.8861
- KNN: 0.9506
- Random Forest: 1.0000

Best model: Random Forest

## Inputs

Age, Total Bilirubin, Direct Bilirubin, Alkaline Phosphotase, SGPT, SGOT, Total Proteins, A/G Ratio.

## Disclaimer

Educational use only. Not for medical diagnosis.

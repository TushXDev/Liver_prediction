# Liver Disease Prediction System

Minimal Flask app for liver disease screening using Liver Function Test (LFT) inputs and a trained ML model. Includes a simple UI, JSON API, and prediction request logging.

## Quick Start

1) Create and activate a virtual environment (Windows PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2) Install dependencies

```powershell
pip install -r requirements.txt
```

3) Ensure the model file exists at the project root (see Model File)

4) Run the app

```powershell
python app.py
```

5) Open http://localhost:5000 (predictor at /predictor)

## Key Achievements

- End-to-end data cleaning: reduced raw dataset from 30,691 to 17,214 rows and standardized LFT features for modeling.
- Model benchmarking: evaluated SVM, Logistic Regression, Decision Tree, Gradient Boosting, KNN, and Random Forest; best recorded accuracy shows Random Forest at 1.0000 and KNN at 0.9506.
- Production-ready inference: minimal Flask API with JSON-based `predict` endpoint returning prediction, confidence, and per-class probabilities.
- Clinical input handling: accepts common LFT markers and derives `Albumin` from Total Proteins and A/G Ratio for consistent model features.
- Request logging: writes timestamped inputs and outputs to logs/visitor_lft_log.csv for auditability and analysis.
- Deployment readiness: includes Procfile and requirements for easy hosting.
- Reproducibility: ships notebook and datasets to re-run experiments.
## How It Works

- UI: templates for home and predictor pages.
- API: Flask routes `GET /`, `GET /predictor`, and `POST /predict` in app.py.
- Model: loaded from a pickle file for fast inference.
- Logging: requests written to logs/visitor_lft_log.csv.

## API

- Endpoint: `POST /predict`
- Body: JSON with fields listed in Inputs
- Response: `{ success, prediction, confidence, probability_class_1, probability_class_2 }`

Example request (PowerShell):

```powershell
curl -Method POST -Uri http://localhost:5000/predict -ContentType 'application/json' -Body '{
	"Name": "Jane Doe",
	"Age": 35,
	"Total Bilirubin": 0.7,
	"Direct Bilirubin": 0.2,
	"Alkaline Phosphatase": 66,
	"Alkaline Phosphotase": 66,
	"Alamine Aminotransferase": 18,
	"Aspartate Aminotransferase": 15,
	"Total Proteins": 6.0,
	"A/G Ratio": 1.0
}'
```

Example response:

```json
{
	"success": true,
	"prediction": "No Liver Disease (Class 1)",
	"confidence": 96.42,
	"probability_class_1": 96.42,
	"probability_class_2": 3.58
}
```

## Inputs

Age, Total Bilirubin, Direct Bilirubin, Alkaline Phosphatase, SGPT (Alamine Aminotransferase), SGOT (Aspartate Aminotransferase), Total Proteins, A/G Ratio.

Note: `Albumin` is derived inside the API using Total Proteins and A/G Ratio.

## Model File

- The app loads the model from `model_knn.pkl` at the project root.
- If you have `model.pkl` (e.g., from tests), either rename it to `model_knn.pkl` or update `app.py` to match.
- To verify your pickle, run the included test script (expects `model.pkl` by default):

```powershell
python test_model.py
```

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

## Deployment

- Local: `python app.py` runs the server on port 5000.
- Heroku-style: Procfile uses `gunicorn app:app`.
	- Note: install `gunicorn` for deployment (`pip install gunicorn`).

## Troubleshooting

- Model file missing: ensure `model_knn.pkl` exists at the project root.
- Invalid inputs: the API responds with clear validation errors.
- Environment: use Python 3.10+ and install from `requirements.txt`.

## Disclaimer

Educational use only. Not for medical diagnosis.



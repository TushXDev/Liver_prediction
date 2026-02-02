# Model Results (Latest Notebook Output)

## Dataset

- Raw rows: 30,691
- Cleaned rows: 17,214
- Features used for training: Age, Total Bilirubin, Direct Bilirubin, Alkaline Phosphotase, SGPT, SGOT, Total Proteins, Albumin, A/G Ratio
- Target: `Dataset` (1/2)

## Model accuracy (test split)

| Model | Accuracy |
| --- | ---: |
| SVM | 0.7168 |
| Logistic Regression | 0.7290 |
| Decision Tree | 0.8449 |
| Gradient Boosting | 0.8861 |
| KNN | 0.9506 |
| Random Forest | 1.0000 |

Best model: Random Forest

## Logistic Regression report

Confusion matrix:

```
[[2312  156]
 [ 777  198]]
```

Classification summary:

- Class 1: precision 0.75, recall 0.94, f1 0.83 (support 2468)
- Class 2: precision 0.56, recall 0.20, f1 0.30 (support 975)
- Accuracy: 0.7290

## KNN report

- Accuracy: 0.9506
- Class 1: precision 0.97, recall 0.96, f1 0.97
- Class 2: precision 0.91, recall 0.92, f1 0.91

## Decision Tree report

- Accuracy: 0.8449
- Class 1: precision 0.97, recall 0.81, f1 0.88
- Class 2: precision 0.66, recall 0.93, f1 0.77

## Gradient Boosting report

- Accuracy: 0.8861
- Class 1: precision 0.88, recall 0.98, f1 0.93
- Class 2: precision 0.93, recall 0.65, f1 0.76

## Random Forest report

- Accuracy: 1.0000
- Class 1: precision 1.00, recall 1.00, f1 1.00
- Class 2: precision 1.00, recall 1.00, f1 1.00

## Notes

Results are from the latest notebook run. This project is for educational use only.

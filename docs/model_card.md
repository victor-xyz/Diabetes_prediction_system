# Model Card: Diabetes Risk Prediction

## Purpose

An educational machine-learning demonstration for binary classification using patient health variables. The model estimates the probability associated with the positive outcome in the training dataset.

## Model

Final model: Logistic Regression with StandardScaler preprocessing.

Input features: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, and Age.

Target: Outcome.

## Evaluation setup

- Dataset: Pima Indians Diabetes dataset
- Records: 768
- Test size: 20%
- Random state: 42
- Training records: 614
- Test records: 154
- Cross-validation: 5-fold accuracy

## Held-out test results

| Metric | Result |
|---|---:|
| Accuracy | 75.33% |
| Precision | 64.91% |
| Recall | 67.27% |
| F1-score | 66.07% |
| ROC-AUC | 81.47% |

Confusion matrix: [[79, 20], [18, 37]].

Mean 5-fold cross-validation accuracy: approximately 76.06%.

## Interpretation

The output is a model-estimated probability, not a diagnosis. Logistic Regression coefficients describe the model's learned relationship with the log-odds after scaling; they should not be interpreted as clinical thresholds or causal effects.

## Limitations

The dataset is relatively small and has demographic and geographic limitations. Performance on other populations, healthcare systems, measurement procedures, or prevalence levels may differ. The model has not been clinically validated for deployment.

## Intended use

Educational demonstration, machine-learning study, and portfolio presentation.

## Not intended for

Clinical diagnosis, treatment decisions, triage, or autonomous healthcare decision-making.

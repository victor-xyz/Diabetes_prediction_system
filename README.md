# Diabetes Risk Prediction System

A machine-learning-based system for predicting the likelihood of diabetes risk using patient health data.

## Project

**A MACHINE-LEARNING-BASED SYSTEM FOR PREDICTING THE LIKELIHOOD OF DIABETES RISK USING PATIENT HEALTH DATA**

Final-year Computer Science project, University of Benin.

## What this project demonstrates

This project covers an end-to-end supervised machine-learning workflow:

- Data preparation and feature selection
- Train/test splitting
- Feature scaling with StandardScaler
- Logistic Regression for binary classification
- Probability-based prediction
- Cross-validation
- Evaluation with multiple classification metrics
- Interactive deployment with Streamlit
- Interpretation of model limitations and responsible-use considerations

## Dataset

The project uses the **Pima Indians Diabetes dataset**, containing 768 records and eight predictive features.

Features:

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-hour serum insulin |
| BMI | Body mass index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Age in years |

Target: **Outcome**

The dataset is used for educational and research purposes. It should not be treated as clinically representative of all populations.

## Modelling approach

The final classifier is Logistic Regression with feature scaling.

The data was divided into:

- Training set: 614 records
- Test set: 154 records
- Test size: 20%
- Random state: 42

Logistic Regression was selected because the task is binary classification and the model provides probability estimates and interpretable coefficients.

## Evaluation results

Results from the final held-out test evaluation:

| Metric | Result |
|---|---:|
| Accuracy | 75.33% |
| Precision | 64.91% |
| Recall | 67.27% |
| F1-score | 66.07% |
| ROC-AUC | 81.47% |

### Confusion matrix

| | Predicted 0 | Predicted 1 |
|---|---:|---:|
| Actual 0 | 79 | 20 |
| Actual 1 | 18 | 37 |

Mean 5-fold cross-validation accuracy was approximately **76.06%**.

The complete evaluation notes are available in [docs/results.md](docs/results.md), while the model card is available in [docs/model_card.md](docs/model_card.md).

## Application

The original project includes a Streamlit interface that accepts the eight model inputs and returns an estimated probability associated with the positive outcome.

The prediction is a model output and **not a medical diagnosis**.

The deployment source is being organised separately from the research documentation so that the repository remains easy to inspect.

## Repository structure

```text
Diabetes_prediction_system/
├── docs/
│   ├── model_card.md
│   └── results.md
├── src/
│   └── train_model.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Limitations

- The dataset is relatively small.
- The source dataset has demographic and geographic limitations.
- Performance may differ on other populations and clinical settings.
- Dataset quality and missing-value treatment can affect model performance.
- The model has not been clinically validated.
- A single machine-learning model does not capture every clinically relevant factor.

## Future work

Potential extensions include:

- Comparison with additional classifiers
- Ensemble modelling
- Hyperparameter tuning
- External validation
- Improved missing-value treatment
- Explainable AI techniques
- Larger and more representative datasets
- Clinical validation before any real-world deployment

## Portfolio relevance

This project demonstrates practical experience with **Python, machine learning, data preprocessing, model evaluation, probability-based classification, Streamlit, technical documentation, and responsible AI considerations**.

It complements the other portfolio projects in this profile covering AI evaluation, multimodal annotation, and Python data analysis.

## Author

**Benjamin Victor Omeyimi**

B.Sc. Computer Science, University of Benin

Interests: Machine Learning, Artificial Intelligence, Python, AI evaluation, healthcare technology, and reliable AI systems.

## Disclaimer

**This project is for educational and research purposes only. It is not a medical diagnostic tool and should not be used to make clinical decisions.**

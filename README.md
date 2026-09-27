# Diabetes Risk Prediction System

A machine-learning-based system for predicting the likelihood of diabetes risk from patient health data.

## Project

**A MACHINE-LEARNING-BASED SYSTEM FOR PREDICTING THE LIKELIHOOD OF DIABETES RISK USING PATIENT HEALTH DATA**

This project was developed as a final-year Computer Science project at the University of Benin.

## Overview

The system uses supervised machine learning to learn the relationship between clinical and demographic variables and an observed diabetes outcome.

The implementation includes:

- Data preprocessing
- Feature scaling
- Logistic Regression
- Model evaluation
- Cross-validation
- Probability-based prediction
- A Streamlit interface for interactive use

## Input Features

The model uses eight input variables:

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

The target variable is **Outcome**, representing the observed diabetes classification in the dataset.

## Dataset

The project uses the Pima Indians Diabetes dataset, containing 768 records and eight predictive features.

The dataset is used for educational and research purposes. It should not be interpreted as a clinically representative population for all patients or healthcare settings.

## Model Development

The data was divided using:

- Test size: 20%
- Random state: 42
- Training records: 614
- Test records: 154

Feature scaling was applied before training the final Logistic Regression model.

## Final Test Results

The scaled Logistic Regression model produced the following results on the held-out test set:

| Metric | Result |
|---|---:|
| Accuracy | 75.33% |
| Precision | 64.91% |
| Recall | 67.27% |
| F1-score | 66.07% |
| ROC-AUC | 81.47% |

### Confusion Matrix

```text
                Predicted
                0      1
Actual  0      79     20
        1      18     37
```

The model also achieved a mean cross-validation accuracy of approximately **76.06%**.

## Why Logistic Regression?

Logistic Regression was selected because the task is binary classification and the model provides interpretable coefficients and probability estimates.

Feature scaling was used to place numerical variables on comparable scales during optimisation.

## Prediction Output

The Streamlit application accepts patient health measurements and returns an estimated probability associated with the positive diabetes outcome.

The probability should be interpreted as a model output, not as a medical diagnosis.

## Limitations

- The dataset is relatively small.
- The source dataset has demographic and geographic limitations.
- Model performance may differ on other populations and clinical settings.
- The system does not replace professional medical assessment.
- Missing-value handling and dataset quality can affect model performance.
- A single model does not capture every clinically relevant factor.

## Future Work

Potential extensions include:

- Comparing additional classification algorithms
- Ensemble modelling
- More extensive hyperparameter tuning
- External validation
- Improved missing-value treatment
- Explainable AI techniques
- Larger and more representative datasets
- Clinical validation before any real-world deployment

## Application

The project includes a Streamlit interface designed to make the trained model accessible through a simple interactive workflow.

## Author

**Benjamin Victor Omeyimi**

B.Sc. Computer Science, University of Benin

Interests: Machine Learning, Artificial Intelligence, Python, AI evaluation, healthcare technology, and reliable AI systems.

## Disclaimer

**This project is for educational and research purposes only. It is not a medical diagnostic tool and should not be used to make clinical decisions.**

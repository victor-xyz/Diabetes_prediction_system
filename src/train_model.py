"""Train and evaluate the diabetes risk prediction model."""
from pathlib import Path
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler

DATA_PATH = Path("data/diabetes.csv")
MODEL_DIR = Path("models")
FEATURES = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
TARGET = "Outcome"

def main():
    df = pd.read_csv(DATA_PATH)
    X, y = df[FEATURES], df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    y_prob = model.predict_proba(X_test_scaled)[:, 1]
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.5f}")
    print(f"Precision: {precision_score(y_test, y_pred):.5f}")
    print(f"Recall: {recall_score(y_test, y_pred):.5f}")
    print(f"F1-score: {f1_score(y_test, y_pred):.5f}")
    print(f"ROC-AUC: {roc_auc_score(y_test, y_prob):.5f}")
    print("Confusion matrix:")
    print(confusion_matrix(y_test, y_pred))
    cv_scores = cross_val_score(model, scaler.fit_transform(X), y, cv=5, scoring="accuracy")
    print(f"5-fold CV accuracy: {cv_scores.mean():.5f}")
    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump({"model": model, "scaler": scaler, "features": FEATURES}, MODEL_DIR / "diabetes_logistic_regression.joblib")

if __name__ == "__main__":
    main()

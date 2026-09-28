import streamlit as st
import pandas as pd
import joblib

# ============================================================
# Load trained model
# ============================================================

model = joblib.load("scaled_diabetes_model.pkl")


# ============================================================
# Page configuration
# ============================================================

st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="centered"
)


# ============================================================
# Custom styling
# ============================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
    background-color: #070B12;
        color: #F8FAFC;
    }

    /* Main content */
    .block-container {
        max-width: 1000px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Main title */
    .main-title {
        text-align: center;
        color: #F8FAFC;
        font-size: 2.4rem;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }

    .subtitle {
        text-align: center;
        color: #CBD5E1;
        font-size: 1rem;
        margin-bottom: 2rem;
    }

    /* Section headings */
    .section-title {
        color: #F8FAFC;
        font-size: 1.25rem;
        font-weight: 600;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    /* Information card */
    .info-card {
    background-color: #0D141F;
        border: 1px solid #26364D;
        border-radius: 12px;
        padding: 1rem 1.2rem;
        margin-bottom: 1.5rem;
        color: #CBD5E1;
    }

    /* Disclaimer */
    .disclaimer {
    background-color: #0D141F;
        border-left: 4px solid #3B82F6;
        border-radius: 8px;
        padding: 0.9rem 1rem;
        color: #CBD5E1;
        font-size: 0.9rem;
        margin-bottom: 1.5rem;
    }

    /* Result cards */
    .result-high {
        background-color: #3B1518;
        border: 1px solid #EF4444;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        margin-top: 1rem;
    }

    .result-low {
        background-color: #10251B;
        border: 1px solid #22C55E;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        margin-top: 1rem;
    }

    .result-borderline {
        background-color: #29200C;
        border: 1px solid #F59E0B;
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
        margin-top: 1rem;
    }

    .result-label {
        color: #94A3B8;
        font-size: 0.9rem;
        margin-bottom: 0.3rem;
    }

    .result-text {
        color: #F8FAFC;
        font-size: 1.25rem;
        font-weight: 600;
    }

    /* Metric */
    .probability-label {
        text-align: center;
        color: #94A3B8;
        font-size: 0.9rem;
        margin-top: 1.2rem;
    }

    .probability-value {
        text-align: center;
        color: #F8FAFC;
        font-size: 2rem;
        font-weight: 700;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748B;
        font-size: 0.8rem;
        margin-top: 2rem;
    }
/* Dark input fields */
.stNumberInput input {
    background-color: #0D141F !important;
    color: #F8FAFC !important;
}

/* Dark input containers */
.stNumberInput > div > div {
    background-color: #0D141F;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# Header
# ============================================================

st.markdown(
    '<div class="main-title">🩺 Diabetes Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine-learning based clinical decision-support prototype'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="info-card">'
    'This system uses a trained Logistic Regression model to estimate '
    'the probability of diabetes based on selected patient clinical '
    'measurements.'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="disclaimer">'
    '<strong>Important:</strong> This system is an academic decision-support '
    'prototype and does not provide a medical diagnosis. Results should be '
    'interpreted by a qualified healthcare professional.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# Patient information
# ============================================================

st.markdown(
    '<div class="section-title">Patient Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    pregnancies = st.number_input(
        "Pregnancies",
        min_value=0,
        max_value=20,
        value=1
    )

    glucose = st.number_input(
        "Glucose Level",
        min_value=0,
        max_value=300,
        value=120
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=0,
        max_value=200,
        value=70
    )

    skin_thickness = st.number_input(
        "Skin Thickness",
        min_value=0,
        max_value=100,
        value=20
    )


with col2:

    insulin = st.number_input(
        "Insulin",
        min_value=0,
        max_value=900,
        value=80
    )

    bmi = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0
    )

    diabetes_pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.5
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )


# ============================================================
# Prediction
# ============================================================

st.divider()

predict_button = st.button(
    "🔍 Predict Diabetes",
    type="primary",
    use_container_width=True
)

if predict_button:

    # --------------------------------------------------------
    # Input validation
    # --------------------------------------------------------

    if glucose <= 0:
        st.warning("Please enter a valid glucose level greater than 0.")

    elif bmi <= 0:
        st.warning("Please enter a valid BMI greater than 0.")

    elif blood_pressure <= 0:
        st.warning(
            "Please enter a valid blood pressure value greater than 0."
        )

    elif age <= 0:
        st.warning("Please enter a valid age greater than 0.")

    else:

        # ----------------------------------------------------
        # Prepare patient data
        # ----------------------------------------------------

        input_data = pd.DataFrame([[
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age
        ]], columns=[
            "Pregnancies",
            "Glucose",
            "BloodPressure",
            "SkinThickness",
            "Insulin",
            "BMI",
            "DiabetesPedigreeFunction",
            "Age"
        ])

        # ----------------------------------------------------
        # Model prediction
        # ----------------------------------------------------

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        # ----------------------------------------------------
        # Prediction result
        # ----------------------------------------------------

        st.divider()

        st.markdown(
            '<div class="section-title">Prediction Result</div>',
            unsafe_allow_html=True
        )

        # Borderline range around the 0.50 threshold
        if 0.45 <= probability <= 0.55:

            st.markdown(
                '<div class="result-borderline">'
                '<div class="result-label">Model Classification</div>'
                '<div class="result-text">'
                '⚠ Borderline Prediction'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

        elif prediction == 1:

            st.markdown(
                '<div class="result-high">'
                '<div class="result-label">Model Classification</div>'
                '<div class="result-text">'
                '● The model predicts that the patient may have diabetes.'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                '<div class="result-low">'
                '<div class="result-label">Model Classification</div>'
                '<div class="result-text">'
                '● The model predicts that the patient is unlikely to have diabetes.'
                '</div>'
                '</div>',
                unsafe_allow_html=True
            )

        st.markdown(
            '<div class="probability-label">'
            'Estimated Model Probability'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="probability-value">'
            f'{probability:.2%}'
            f'</div>',
            unsafe_allow_html=True
        )

        st.caption(
            "The probability represents the model's estimated probability "
            "for the positive diabetes class."
        )


# ============================================================
# Model information
# ============================================================

st.divider()

st.markdown(
    '<div class="section-title">Model Information</div>',
    unsafe_allow_html=True
)

st.write(
    "The system uses a Logistic Regression model with feature "
    "standardization. Logistic Regression was selected after comparing "
    "its performance with Decision Tree and Random Forest models."
)

metric_col1, metric_col2, metric_col3 = st.columns(3)

with metric_col1:
    st.metric("Accuracy", "75.32%")

with metric_col2:
    st.metric("F1-score", "66.07%")

with metric_col3:
    st.metric("ROC-AUC", "0.815")

st.caption(
    "Evaluation was performed on a held-out test set of 154 samples. "
    "The reported metrics are model evaluation results and should not "
    "be interpreted as clinical performance guarantees."
)


# ============================================================
# Footer
# ============================================================

st.markdown(
    '<div class="footer">'
    'Diabetes Prediction System • Machine Learning Project'
    '</div>',
    unsafe_allow_html=True
)
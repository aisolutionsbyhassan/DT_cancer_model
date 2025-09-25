import streamlit as st
import joblib
import numpy as np

# ------------------------
# Load model
# ------------------------
@st.cache_resource
def load_model():
    return joblib.load("cancer.pkl")

model = load_model()

# ------------------------
# Page Config
# ------------------------
st.set_page_config(
    page_title="Breast Cancer Predictor",
    page_icon="🎗️",
    layout="wide"
)

# ------------------------
# App Title
# ------------------------
st.title("🎗️ Breast Cancer Prediction App")
st.markdown(
    """
    This app predicts whether a breast cancer case is **Benign (non-cancerous)**  
    or **Malignant (cancerous)** based on patient data.  
    Please provide the required input values below.
    """
)

# ------------------------
# Sidebar for inputs
# ------------------------
st.sidebar.header("🔹 Input Patient Data")

feature_names = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
    'compactness_mean', 'concavity_mean', 'concave points_mean', 'symmetry_mean',
    'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se',
    'smoothness_se', 'compactness_se', 'concavity_se', 'concave points_se',
    'symmetry_se', 'fractal_dimension_se', 'radius_worst', 'texture_worst',
    'perimeter_worst', 'area_worst', 'smoothness_worst', 'compactness_worst',
    'concavity_worst', 'concave points_worst', 'symmetry_worst', 'fractal_dimension_worst'
]

# Split inputs into two columns for better look
input_data = []
col1, col2 = st.sidebar.columns(2)
for i, feature in enumerate(feature_names):
    if i % 2 == 0:
        val = col1.number_input(f"{feature}", value=0.0, format="%.4f")
    else:
        val = col2.number_input(f"{feature}", value=0.0, format="%.4f")
    input_data.append(val)

features = np.array([input_data])

# ------------------------
# Prediction Button
# ------------------------
st.markdown("---")
if st.button("🔍 Predict", use_container_width=True):
    prediction = model.predict(features)
    if prediction[0] == "B":   # Benign
        st.success("✅ The prediction is: **Benign (Non-Cancerous)**")
        st.balloons()
    else:
        st.error("⚠️ The prediction is: **Malignant (Cancerous)**")
        st.snow()

# ------------------------
# Footer
# ------------------------
st.markdown(
    """
    ---
    💡 *This app is for educational/demo purposes only.  
    It should not be used as a substitute for professional medical advice.*
    """
)


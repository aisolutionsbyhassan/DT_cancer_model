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

# ✅ Use only the 6 selected features
feature_names = [
    'concave points_mean',
    'radius_worst',
    'concavity_worst',
    'texture_worst',
    'perimeter_worst',
    'perimeter_se'
]

# Two-column input layout for better design
input_data = []
col1, col2 = st.sidebar.columns(2)

for i, feature in enumerate(feature_names):
    if i % 2 == 0:
        val = col1.number_input(f"{feature}", value=0.0, format="%.4f")
    else:
        val = col2.number_input(f"{feature}", value=0.0, format="%.4f")
    input_data.append(val)

# Convert input into numpy array
features = np.array([input_data])

# ------------------------
# Prediction Button
# ------------------------
st.markdown("---")
if st.button("🔍 Predict", use_container_width=True):
    prediction = model.predict(features)

    # Model was trained with LabelEncoder (0 = Benign, 1 = Malignant)
    if prediction[0] == 0:
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



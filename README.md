# 🎗️ Breast Cancer Prediction Web App  

A machine learning project that predicts whether a tumor is **Benign (non-cancerous)** or **Malignant (cancerous)** using the Breast Cancer dataset.  
This project includes a trained ML model, a Jupyter Notebook for training & analysis, and a **Streamlit web application** for easy predictions.  

## 🌐 Try the Web App  
You can try the live app here: [Breast Cancer Prediction Web App](https://aisolutionsbyhassan-dt-cancer-model-app-nmapwc.streamlit.app/)  

## 📌 Features  
- End-to-end machine learning pipeline: **data preprocessing, visualization, feature selection, model training & evaluation, and deployment with Streamlit**  
- **Feature selection applied** → reduced from 30 to **6 most important features**, while maintaining high accuracy (Train ≈ 97.55%, Test ≈ 97.36%)  
- User-friendly **web app interface**  
- Clear prediction results: ✅ Benign (Non-Cancerous) or ⚠️ Malignant (Cancerous)  

## 📊 Model Performance  
- **Classifier Used:** Decision Tree  
- **Selected Features (Top 6 by importance):**  
  - concave points_mean  
  - radius_worst  
  - concavity_worst  
  - texture_worst  
  - perimeter_worst  
  - perimeter_se  
- **Accuracy:**  
  - Train Accuracy: **97.55%**  
  - Test Accuracy: **97.36%**  

## 📂 Project Structure  

📁 DT_cancer_model  
┣ 📜 app.py → Streamlit app  
┣ 📜 cancer.ipynb → Jupyter Notebook (EDA, feature selection & model training)  
┣ 📜 cancer.pkl → Trained ML model  
┣ 📜 data.csv → Dataset used  
┣ 📜 requirements.txt → Dependencies  
┗ 📜 README.md → Project documentation  

---

💡 *This project is for educational/demo purposes only.  
It should not be used as a substitute for professional medical advice.*  




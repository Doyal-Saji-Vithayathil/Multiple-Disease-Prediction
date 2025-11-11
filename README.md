# 🧠 Multiple Disease Prediction Web App

A **Streamlit-based machine learning web application** that predicts multiple diseases from user-inputted symptoms and medical parameters. The app supports **multi-disease prediction** using an **XGBoost model** and provides **individual predictors** for diseases such as Diabetes, Heart Disease, Parkinson’s, and more.  

The system also generates **detailed PDF reports** including patient details, disease descriptions, precautions, and doctor recommendations.

---

## 🚀 Key Features

✅ **Multi-Disease Prediction:**  
Predicts the most likely disease from a list of symptoms using an XGBoost model trained on medical datasets.

✅ **Specific Disease Predictors:**  
Dedicated modules for predicting:
- Diabetes  
- Heart Disease  
- Parkinson’s Disease  
- Liver Disease  
- Hepatitis  
- Jaundice  
- Lung Cancer  
- Chronic Kidney Disease  
- Breast Cancer  

✅ **Patient Management:**  
Choose from pre-existing patient records or manually input data.

✅ **📄 PDF Report Generation:**  
Generate a downloadable medical report containing:
- Patient details  
- Prediction results  
- Disease description  
- Precautions  
- Recommended doctors  

✅ **👨‍⚕️ Doctor Recommendations:**  
Displays contact details for specialist doctors based on the disease type.

✅ **🧭 User-Friendly Interface:**  
Interactive, easy-to-use Streamlit web interface for quick input and results visualization.

---

## 🧩 Technology Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | Streamlit (Python web framework) |
| **Backend** | Python |
| **Machine Learning** | XGBoost, Scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **PDF Generation** | FPDF |
| **Model Serialization** | Joblib |

---

## ⚙️ How It Works

### 🧬 Multi-Disease Prediction
1. User selects symptoms from a multiselect dropdown.  
2. Symptoms are encoded into a binary array using helper functions.  
3. The **XGBoost model** predicts the most probable disease.  
4. The app displays:
   - Disease name  
   - Description  
   - Precautions  
   - Recommended doctor details  

### ❤️ Specific Disease Predictions
Each disease page accepts specific parameters:
- **Diabetes:** Glucose, BMI, Age, Insulin, etc.  
- **Heart Disease:** Blood Pressure, Cholesterol, Age, etc.  
- **Liver Disease:** Enzyme levels, Protein counts, etc.  

Predictions are **binary (Positive/Negative)** with visual indicators.

### 📄 PDF Report Generation
- Generated via **FPDF** library  
- Includes patient info, disease prediction, precautions, and doctor details  
- Downloadable directly from the Streamlit UI  

---

## 🧠 Machine Learning Details

| Type | Model | Description |
|------|--------|-------------|
| **Multi-Disease** | XGBoost | Trained on symptom–disease mappings |
| **Specific Diseases** | SVM, Random Forest, etc. | Separate ML models per disease |
| **Data Sources** | Multiple CSV files | Include symptoms, parameters, and outcomes |

---

## 🧰 Installation & Setup

### Prerequisites
- Python 3.8+
- Pip (Python package manager)

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/<your-username>/Multiple-Disease-Prediction.git

# Navigate into the project directory
cd Multiple-Disease-Prediction

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
Then open your browser and visit:
👉 http://localhost:8501/

🔄 Data Flow

User inputs symptoms or medical parameters

Data is preprocessed into numerical format

Model performs prediction

App fetches details (description, precautions, doctor info)

Results displayed + optional PDF generation

🩺 Doctor Recommendation System

Each predicted disease maps to a specialist doctor list with:

Doctor Name

Hospital/Clinic

Contact Info

These are shown directly in the app and attached to the generated PDF.

🔮 Future Enhancements

🚧 Planned Upgrades:

Add more diseases and datasets

Implement user authentication and patient history tracking

Integrate real-time doctor consultations via API

Add model retraining and continuous learning

Connect with medical data APIs for richer insights

📚 Example Use Case

Select your symptoms from the dropdown.

Click “Predict Disease”.

View your disease prediction and doctor recommendations.

Download your medical report as a PDF.

🧑‍💻 Author

👨‍💻 Doyal Saji Vithayathil
B.Tech Computer Science Student
📍 India

🪪 License

This project is open-source under the MIT License — feel free to use and improve it.

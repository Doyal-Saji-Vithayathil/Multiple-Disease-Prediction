import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
from streamlit_option_menu import option_menu
import pickle
from PIL import Image
import numpy as np
import plotly.figure_factory as ff
import streamlit as st
from code.DiseaseModel import DiseaseModel
from code.helper import prepare_symptoms_array
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
from fpdf import FPDF
import base64
import datetime

# loading the models
diabetes_model = joblib.load("models/diabetes_model.sav")
heart_model = joblib.load("models/heart_disease_model.sav")
parkinson_model = joblib.load("models/parkinsons_model.sav")
# Load the lung cancer prediction model
lung_cancer_model = joblib.load('models/lung_cancer_model.sav')

# Load the pre-trained model
breast_cancer_model = joblib.load('models/breast_cancer.sav')

# Load the pre-trained model
chronic_disease_model = joblib.load('models/chronic_model.sav')

# Load the hepatitis prediction model
hepatitis_model = joblib.load('models/hepititisc_model.sav')

# Load the liver model for Liver disease prediction
liver_model = joblib.load('models/liver_model.sav')

# Load the liver model for jaundice prediction
jaundice_model = joblib.load('models/liver_model.sav') 

# Load the lung cancer prediction model
lung_cancer_model = joblib.load('models/lung_cancer_model.sav')

# Doctor Info Lookup
patients_data = [
    {"name": "Ankit Sharma", "age": 28, "gender": "Male", "symptoms": ["itching", "skin_rash", "nodal_skin_eruptions", "dischromic _patches"]},
    {"name": "Priya Mehta", "age": 35, "gender": "Female", "symptoms": ["continuous_sneezing", "shivering", "chills", "watering_from_eyes"]},
    {"name": "Rohan Kapoor", "age": 42, "gender": "Male", "symptoms": ["stomach_pain", "acidity", "ulcers_on_tongue", "vomiting", "cough", "chest_pain"]},
    {"name": "Sneha Verma", "age": 30, "gender": "Female", "symptoms": ["itching", "vomiting", "yellowish_skin", "nausea", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes"]}
]

def get_doctor_details(specialty):
    details = {
        "heart": """Dr. Arjun Menon\nCardiology Specialist\nApollo Hospitals, Bengaluru\nPhone: +91-98765-43210\nEmail: arjun.menon@apollohospitals.com""",
        "parkinson": """Dr. Meera Iyer\nSenior Neurologist - Movement Disorders\nNIMHANS, Bengaluru\nPhone: +91-99887-65432\nEmail: meera.iyer@nimhans.ac.in""",
        "lung_cancer": """Dr. Rajesh Sharma\nThoracic Oncologist\nTata Memorial Hospital, Mumbai\nPhone: +91-91234-56789\nEmail: rajesh.sharma@tmh.org.in""",
        "liver": """Dr. Kavita Nair\nLiver Specialist\nManipal Hospitals, Hyderabad\nPhone: +91-92345-67890\nEmail: kavita.nair@manipalhospitals.com""",
        "hepatitis": """Dr. Sandeep Varma\nHepatitis & Liver Infection Expert\nFortis Hospital, Delhi\nPhone: +91-93456-78901\nEmail: sandeep.varma@fortishealthcare.com""",
        "jaundice": """Dr. Anjali Deshmukh\nSenior Consultant, Internal Medicine\nMax Healthcare, Pune\nPhone: +91-94567-12345\nEmail: anjali.deshmukh@maxhealthcare.com""",
        "kidney": """Dr. Naveen Reddy\nKidney Specialist\nAster Hospitals, Kochi\nPhone: +91-97654-32109\nEmail: naveen.reddy@asterhospitals.com""",
        "breast_cancer": """Dr. Neha Kapoor\nSurgical Oncologist - Breast Cancer\nAIIMS, New Delhi\nPhone: +91-90123-45678\nEmail: neha.kapoor@aiims.edu""",
        "diabetes": """Dr. Ritu Joshi\nDiabetes & Hormone Specialist\nMedanta - The Medicity, Gurugram\nPhone: +91-90909-80808\nEmail: ritu.joshi@medanta.org"""
    }
    return details.get(specialty, "Doctor information not available.")

def generate_pdf_report(name, disease, result, doctor_details):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Disease Diagnosis Report", ln=True, align="C")
    pdf.ln(10)

    # Patient Info
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Patient Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Predicted Disease: {disease}", ln=True)
    pdf.cell(200, 10, txt=f"Diagnosis Result: {result}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Recommended Doctor Info:", ln=True)

    pdf.set_font("Arial", size=12)
    for line in doctor_details.split('\n'):
        pdf.cell(200, 10, txt=line.strip(), ln=True)

    # Save to memory
    pdf_output = pdf.output(dest='S').encode('latin1')
    b64 = base64.b64encode(pdf_output).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="diagnosis_report.pdf">📄 Download Report as PDF</a>'
    return href


def show_doctor_info(specialty):
    if specialty == "heart":
        st.markdown("### Recommended Cardiologist 💓")
        st.markdown("""
        **Dr. Arjun Menon**  
        Cardiology Specialist  
        **Apollo Hospitals, Bengaluru**  
        📞 +91-98765-43210  
        📧 arjun.menon@apollohospitals.com  
        🌐 [Visit Website](https://www.apollohospitals.com/)
        """)
    
    elif specialty == "parkinson":
        st.markdown("### Recommended Neurologist 🧠")
        st.markdown("""
        **Dr. Meera Iyer**  
        Senior Neurologist – Movement Disorders  
        **NIMHANS, Bengaluru**  
        📞 +91-99887-65432  
        📧 meera.iyer@nimhans.ac.in  
        🌐 [Visit NIMHANS](https://nimhans.ac.in/)
        """)
    
    elif specialty == "lung_cancer":
        st.markdown("### Recommended Oncologist 🫁")
        st.markdown("""
        **Dr. Rajesh Sharma**  
        Thoracic Oncologist  
        **Tata Memorial Hospital, Mumbai**  
        📞 +91-91234-56789  
        📧 rajesh.sharma@tmh.org.in  
        🌐 [Visit TMH](https://tmc.gov.in/)
        """)
    
    elif specialty == "liver":
        st.markdown("### Recommended Hepatologist 🧬")
        st.markdown("""
        **Dr. Kavita Nair**  
        Liver Specialist  
        **Manipal Hospitals, Hyderabad**  
        📞 +91-92345-67890  
        📧 kavita.nair@manipalhospitals.com  
        🌐 [Visit Manipal](https://www.manipalhospitals.com/)
        """)
    
    elif specialty == "hepatitis":
        st.markdown("### Recommended Infectious Disease Specialist 🦠")
        st.markdown("""
        **Dr. Sandeep Varma**  
        Hepatitis & Liver Infection Expert  
        **Fortis Hospital, Delhi**  
        📞 +91-93456-78901  
        📧 sandeep.varma@fortishealthcare.com  
        🌐 [Visit Fortis](https://www.fortishealthcare.com/)
        """)
    
    elif specialty == "jaundice":
        st.markdown("### Recommended General Physician 🌡️")
        st.markdown("""
        **Dr. Anjali Deshmukh**  
        Senior Consultant, Internal Medicine  
        **Max Healthcare, Pune**  
        📞 +91-94567-12345  
        📧 anjali.deshmukh@maxhealthcare.com  
        🌐 [Visit Max](https://www.maxhealthcare.in/)
        """)
    
    elif specialty == "kidney":
        st.markdown("### Recommended Nephrologist 🧫")
        st.markdown("""
        **Dr. Naveen Reddy**  
        Kidney Specialist  
        **Aster Hospitals, Kochi**  
        📞 +91-97654-32109  
        📧 naveen.reddy@asterhospitals.com  
        🌐 [Visit Aster](https://www.asterhospitals.in/)
        """)
    
    elif specialty == "breast_cancer":
        st.markdown("### Recommended Oncologist (Breast Cancer) 🎗️")
        st.markdown("""
        **Dr. Neha Kapoor**  
        Surgical Oncologist – Breast Cancer  
        **AIIMS, New Delhi**  
        📞 +91-90123-45678  
        📧 neha.kapoor@aiims.edu  
        🌐 [Visit AIIMS](https://www.aiims.edu/)
        """)
    
    elif specialty == "diabetes":
        st.markdown("### Recommended Endocrinologist 🩸")
        st.markdown("""
        **Dr. Ritu Joshi**  
        Diabetes & Hormone Specialist  
        **Medanta – The Medicity, Gurugram**  
        📞 +91-90909-80808  
        📧 ritu.joshi@medanta.org  
        🌐 [Visit Medanta](https://www.medanta.org/)
        """)

    
    elif specialty.lower() == "fungal infection":
        st.markdown("### Recommended Dermatologist 🧴")
        st.markdown("""
        **Dr. Meera Kapoor**  
        Dermatology Specialist  
        **Fortis Hospital, Mumbai**  
        📞 +91-91234-56789  
        📧 meera.kapoor@fortishealth.com  
        🌐 [Visit Website](https://www.fortishealthcare.com/)
        """)
    elif specialty.lower() == "allergy":
        st.markdown("### Recommended Allergist 🤧")
        st.markdown("""
        **Dr. Rakesh Sharma**  
        Allergy & Immunology Specialist  
        **Max Healthcare, Delhi**  
        📞 +91-99887-66554  
        📧 rakesh.sharma@maxhealthcare.com  
        🌐 [Visit Website](https://www.maxhealthcare.in/)
        """)
    elif specialty.lower() == "gerd":
        st.markdown("### Recommended Gastroenterologist 🍽️")
        st.markdown("""
        **Dr. Priya Nair**  
        Gastroenterology Specialist  
        **Manipal Hospitals, Bengaluru**  
        📞 +91-98765-12345  
        📧 priya.nair@manipalhospitals.com  
        🌐 [Visit Website](https://www.manipalhospitals.com/)
        """)
    elif specialty.lower() == "chronic cholestasis":
        st.markdown("### Recommended Hepatologist 🏥")
        st.markdown("""
        **Dr. Sameer Joshi**  
        Liver & Hepatology Specialist  
        **Medanta, Gurugram**  
        📞 +91-87654-32109  
        📧 sameer.joshi@medanta.org  
        🌐 [Visit Website](https://www.medanta.org/)
        """)
    elif specialty.lower() == "drug reaction":
        st.markdown("### Recommended Clinical Pharmacologist 💊")
        st.markdown("""
        **Dr. Sneha Verma**  
        Clinical Pharmacology Specialist  
        **AIIMS, Delhi**  
        📞 +91-90000-11122  
        📧 sneha.verma@aiims.edu  
        🌐 [Visit Website](https://www.aiims.edu/)
        """)
    elif specialty.lower() == "peptic ulcer diseae":
        st.markdown("### Recommended Gastroenterologist 🍽️")
        st.markdown("""
        **Dr. Priya Nair**  
        Gastroenterology Specialist  
        **Manipal Hospitals, Bengaluru**  
        📞 +91-98765-12345  
        📧 priya.nair@manipalhospitals.com  
        🌐 [Visit Website](https://www.manipalhospitals.com/)
        """)
    elif specialty.lower() == "aids":
        st.markdown("### Recommended Infectious Disease Specialist 🦠")
        st.markdown("""
        **Dr. Anil Deshmukh**  
        Infectious Disease Specialist  
        **Jaslok Hospital, Mumbai**  
        📞 +91-99888-22334  
        📧 anil.deshmukh@jaslokhospital.net  
        🌐 [Visit Website](https://www.jaslokhospital.net/)
        """)
   
    elif specialty.lower() == "gastroenteritis":
        st.markdown("### Recommended Gastroenterologist 🍽️")
        st.markdown("""
        **Dr. Priya Nair**  
        Gastroenterology Specialist  
        **Manipal Hospitals, Bengaluru**  
        📞 +91-98765-12345  
        📧 priya.nair@manipalhospitals.com  
        🌐 [Visit Website](https://www.manipalhospitals.com/)
        """)
    elif specialty.lower() == "bronchial asthma":
        st.markdown("### Recommended Pulmonologist 🌬️")
        st.markdown("""
        **Dr. Rajeev Kumar**  
        Pulmonology Specialist  
        **Fortis Hospital, Delhi**  
        📞 +91-92233-44556  
        📧 rajeev.kumar@fortishealth.com  
        🌐 [Visit Website](https://www.fortishealthcare.com/)
        """)
    elif specialty.lower() == "hypertension":
        st.markdown("### Recommended Cardiologist 💓")
        st.markdown("""
        **Dr. Arjun Menon**  
        Cardiology Specialist  
        **Apollo Hospitals, Bengaluru**  
        📞 +91-98765-43210  
        📧 arjun.menon@apollohospitals.com  
        🌐 [Visit Website](https://www.apollohospitals.com/)
        """)
    elif specialty.lower() == "migraine":
        st.markdown("### Recommended Neurologist 🧠")
        st.markdown("""
        **Dr. Neha Sood**  
        Neurology Specialist  
        **Max Healthcare, Delhi**  
        📞 +91-91122-33445  
        📧 neha.sood@maxhealthcare.com  
        🌐 [Visit Website](https://www.maxhealthcare.in/)
        """)
    elif specialty.lower() == "cervical spondylosis":
        st.markdown("### Recommended Orthopedic Specialist 🦴")
        st.markdown("""
        **Dr. Vikram Singh**  
        Orthopedics Specialist  
        **Medanta, Gurugram**  
        📞 +91-90012-34567  
        📧 vikram.singh@medanta.org  
        🌐 [Visit Website](https://www.medanta.org/)
        """)
    elif specialty.lower() == "paralysis (brain hemorrhage)":
        st.markdown("### Recommended Neurologist 🧠")
        st.markdown("""
        **Dr. Neha Sood**  
        Neurology Specialist  
        **Max Healthcare, Delhi**  
        📞 +91-91122-33445  
        📧 neha.sood@maxhealthcare.com  
        🌐 [Visit Website](https://www.maxhealthcare.in/)
        """)
    
    elif specialty.lower() == "malaria":
        st.markdown("### Recommended General Physician 🩺")
        st.markdown("""
        **Dr. Sunita Gupta**  
        General Medicine  
        **AIIMS, Delhi**  
        📞 +91-98767-89012  
        📧 sunita.gupta@aiims.edu  
        🌐 [Visit Website](https://www.aiims.edu/)
        """)
    elif specialty.lower() == "chicken pox":
        st.markdown("### Recommended Infectious Disease Specialist 🦠")
        st.markdown("""
        **Dr. Anil Deshmukh**  
        Infectious Disease Specialist  
        **Jaslok Hospital, Mumbai**  
        📞 +91-99888-22334  
        📧 anil.deshmukh@jaslokhospital.net  
        🌐 [Visit Website](https://www.jaslokhospital.net/)
        """)
    elif specialty.lower() == "dengue":
        st.markdown("### Recommended General Physician 🩺")
        st.markdown("""
        **Dr. Sunita Gupta**  
        General Medicine  
        **AIIMS, Delhi**  
        📞 +91-98767-89012  
        📧 sunita.gupta@aiims.edu  
        🌐 [Visit Website](https://www.aiims.edu/)
        """)
    elif specialty.lower() == "typhoid":
        st.markdown("### Recommended General Physician 🩺")
        st.markdown("""
        **Dr. Sunita Gupta**  
        General Medicine  
        **AIIMS, Delhi**  
        📞 +91-98767-89012  
        📧 sunita.gupta@aiims.edu  
        🌐 [Visit Website](https://www.aiims.edu/)
        """)
    elif specialty.lower() == "hepatitis a":
        st.markdown("### Recommended Hepatologist 🏥")
        st.markdown("""
        **Dr. Sameer Joshi**  
        Liver & Hepatology Specialist  
        **Medanta, Gurugram**  
        📞 +91-87654-32109  
        📧 sameer.joshi@medanta.org  
        🌐 [Visit Website](https://www.medanta.org/)
        """)
    elif specialty.lower() == "hepatitis b":
        st.markdown("### Recommended Hepatologist 🏥")
        st.markdown("""
        **Dr. Sameer Joshi**  
        Liver & Hepatology Specialist  
        **Medanta, Gurugram**  
        📞 +91-87654-32109  
        📧 sameer.joshi@medanta.org  
        🌐 [Visit Website](https://www.medanta.org/)
        """)
    elif specialty.lower() == "hepatitis c":
        st.markdown("### Recommended Hepatologist 🏥")
        st.markdown("""
        **Dr. Sameer Joshi**  
        Liver & Hepatology Specialist  
        **Medanta, Gurugram**  
        📞 +91-87654-32109  
        📧 sameer.joshi@medanta.org  
        🌐 [Visit Website](https://www.medanta.org/)
        """)
    elif specialty.lower() == "hepatitis d":
        st.markdown("### Recommended Hepatologist 🏥")
        st.markdown("""
        **Dr. Sameer Joshi**  
        Liver & Hepatology Specialist  
        **Medanta, Gurugram**  
        📞 +91-87654-32109  
        📧 sameer.joshi@medanta.org  
        🌐 [Visit Website](https://www.medanta.org/)
        """)
    elif specialty.lower() == "hepatitis e":
        st.markdown("### Recommended Hepatologist 🏥")
        st.markdown("""
        **Dr. Sameer Joshi**  
        Liver & Hepatology Specialist  
        **Medanta, Gurugram**  
        📞 +91-87654-32109  
        📧 sameer.joshi@medanta.org  
        🌐 [Visit Website](https://www.medanta.org/)
        """)
    elif specialty.lower() == "alcoholic hepatitis":
        st.markdown("### Recommended Hepatologist 🏥")
        st.markdown("""
        **Dr. Sameer Joshi**  
        Liver & Hepatology Specialist  
        **Medanta, Gurugram**  
        📞 +91-87654-32109  
        📧 sameer.joshi@medanta.org  
        🌐 [Visit Website](https://www.medanta.org/)
        """)
    elif specialty.lower() == "tuberculosis":
        st.markdown("### Recommended Pulmonologist 🌬️")
        st.markdown("""
        **Dr. Rajeev Kumar**  
        Pulmonology Specialist  
        **Fortis Hospital, Delhi**  
        📞 +91-92233-44556  
        📧 rajeev.kumar@fortishealth.com  
        🌐 [Visit Website](https://www.fortishealthcare.com/)
        """)
    elif specialty.lower() == "common cold":
        st.markdown("### Recommended General Physician 🩺")
        st.markdown("""
        **Dr. Sunita Gupta**  
        General Medicine  
        **AIIMS, Delhi**  
        📞 +91-98767-89012  
        📧 sunita.gupta@aiims.edu  
        🌐 [Visit Website](https://www.aiims.edu/)
        """)
    elif specialty.lower() == "pneumonia":
        st.markdown("### Recommended Pulmonologist 🌬️")
        st.markdown("""
        **Dr. Rajeev Kumar**  
        Pulmonology Specialist  
        **Fortis Hospital, Delhi**  
        📞 +91-92233-44556  
        📧 rajeev.kumar@fortishealth.com  
        🌐 [Visit Website](https://www.fortishealthcare.com/)
        """)
    elif specialty.lower() == "dimorphic hemmorhoids(piles)":
        st.markdown("### Recommended General Surgeon 🏥")
        st.markdown("""
        **Dr. Nitin Desai**  
        General Surgery Specialist  
        **Apollo Hospitals, Mumbai**  
        📞 +91-98876-54321  
        📧 nitin.desai@apollohospitals.com  
        🌐 [Visit Website](https://www.apollohospitals.com/)
        """)
    elif specialty.lower() == "heart attack":
        st.markdown("### Recommended Cardiologist 💓")
        st.markdown("""
        **Dr. Arjun Menon**  
        Cardiology Specialist  
        **Apollo Hospitals, Bengaluru**  
        📞 +91-98765-43210  
        📧 arjun.menon@apollohospitals.com  
        🌐 [Visit Website](https://www.apollohospitals.com/)
        """)
    elif specialty.lower() == "varicose veins":
        st.markdown("### Recommended Vascular Surgeon 🩸")
        st.markdown("""
        **Dr. Shalini Bhatt**  
        Vascular Surgery Specialist  
        **Fortis Hospital, Delhi**  
        📞 +91-91123-45678  
        📧 shalini.bhatt@fortishealth.com  
        🌐 [Visit Website](https://www.fortishealthcare.com/)
        """)
    elif specialty.lower() == "hypothyroidism":
        st.markdown("### Recommended Endocrinologist 🩺")
        st.markdown("""
        **Dr. Kavita Rao**  
        Endocrinology Specialist  
        **Apollo Hospitals, Chennai**  
        📞 +91-98765-43211  
        📧 kavita.rao@apollohospitals.com  
        🌐 [Visit Website](https://www.apollohospitals.com/)
        """)
    elif specialty.lower() == "hyperthyroidism":
        st.markdown("### Recommended Endocrinologist 🩺")
        st.markdown("""
        **Dr. Kavita Rao**  
        Endocrinology Specialist  
        **Apollo Hospitals, Chennai**  
        📞 +91-98765-43211  
        📧 kavita.rao@apollohospitals.com  
        🌐 [Visit Website](https://www.apollohospitals.com/)
        """)
    elif specialty.lower() == "hypoglycemia":
        st.markdown("### Recommended Endocrinologist 🩺")
        st.markdown("""
        **Dr. Kavita Rao**  
        Endocrinology Specialist  
        **Apollo Hospitals, Chennai**  
        📞 +91-98765-43211  
        📧 kavita.rao@apollohospitals.com  
        🌐 [Visit Website](https://www.apollohospitals.com/)
        """)
    elif specialty.lower() == "osteoarthristis":
        st.markdown("### Recommended Orthopedic Specialist 🦴")
        st.markdown("""
        **Dr. Vikram Singh**  
        Orthopedics Specialist  
        **Medanta, Gurugram**  
        📞 +91-90012-34567  
        📧 vikram.singh@medanta.org  
        🌐 [Visit Website](https://www.medanta.org/)
        """)
    elif specialty.lower() == "arthritis":
        st.markdown("### Recommended Rheumatologist 🦴")
        st.markdown("""
        **Dr. Alka Jain**  
        Rheumatology Specialist  
        **Fortis Hospital, Mumbai**  
        📞 +91-98876-54322  
        📧 alka.jain@fortishealth.com  
        🌐 [Visit Website](https://www.fortishealthcare.com/)
        """)
    elif specialty.lower() == "(vertigo) paroymsal positional vertigo":
        st.markdown("### Recommended Neurologist 🧠")
        st.markdown("""
        **Dr. Neha Sood**  
        Neurology Specialist  
        **Max Healthcare, Delhi**  
        📞 +91-91122-33445  
        📧 neha.sood@maxhealthcare.com  
        🌐 [Visit Website](https://www.maxhealthcare.in/)
        """)
    elif specialty.lower() == "acne":
        st.markdown("### Recommended Dermatologist 🧴")
        st.markdown("""
        **Dr. Meera Kapoor**  
        Dermatology Specialist  
        **Fortis Hospital, Mumbai**  
        📞 +91-91234-56789  
        📧 meera.kapoor@fortishealth.com  
        🌐 [Visit Website](https://www.fortishealthcare.com/)
        """)
    elif specialty.lower() == "urinary tract infection":
        st.markdown("### Recommended Urologist 🚻")
        st.markdown("""
        **Dr. Suresh Patel**  
        Urology Specialist  
        **Apollo Hospitals, Ahmedabad**  
        📞 +91-98765-11223  
        📧 suresh.patel@apollohospitals.com  
        🌐 [Visit Website](https://www.apollohospitals.com/)
        """)
    elif specialty.lower() == "psoriasis":
        st.markdown("### Recommended Dermatologist 🧴")
        st.markdown("""
        **Dr. Meera Kapoor**  
        Dermatology Specialist  
        **Fortis Hospital, Mumbai**  
        📞 +91-91234-56789  
        📧 meera.kapoor@fortishealth.com  
        🌐 [Visit Website](https://www.fortishealthcare.com/)
        """)
    elif specialty.lower() == "impetigo":
        st.markdown("### Recommended Dermatologist 🧴")
        st.markdown("""
        **Dr. Meera Kapoor**  
        Dermatology Specialist  
        **Fortis Hospital, Mumbai**  
        📞 +91-91234-56789  
        📧 meera.kapoor@fortishealth.com  
        🌐 [Visit Website](https://www.fortishealthcare.com/)
        """)
    else:
        st.markdown("### Recommended General Physician 🩺")
        st.markdown("""
        **Dr. Sunita Gupta**  
        General Medicine  
        **AIIMS, Delhi**  
        📞 +91-98767-89012  
        📧 sunita.gupta@aiims.edu  
        🌐 [Visit Website](https://www.aiims.edu/)
        """)

    


# sidebar
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction', [
        'Disease Prediction',
        'Diabetes Prediction',
        'Heart disease Prediction',
        'Parkison Prediction',
        'Liver Prediction',
        'Hepatitis Prediction',
        'Jaundice Prediction',
        'Lung Cancer Prediction',
        'Chronic Kidney Prediction',
        'Breast Cancer Prediction',

    ],
        icons=['activity','droplet','heart-pulse','person-walking','droplet-half','emoji-dizzy','emoji-frown','lungs','droplet','gender-female'], default_index=0)




# multiple disease prediction
if selected == 'Disease Prediction': 
    # Create disease class and load ML model
    disease_model = DiseaseModel()
    disease_model.load_xgboost('model/xgboost_model.json')

    # Title
    st.write('# Disease Prediction')
       # Patient selection dropdown
    patient_names = ["Manual Entry"] + [p["name"] for p in patients_data]
    selected_patient = st.selectbox("Select a Patient", patient_names)

    
    if selected_patient == "Manual Entry":
        symptoms = st.multiselect('What are your symptoms?', options=disease_model.all_symptoms)      
        
        
        
    else:
        patient = next(p for p in patients_data if p["name"] == selected_patient)
        st.write(f"**Name:** {patient['name']}")
        st.write(f"**Age:** {patient['age']}")
        st.write(f"**Gender:** {patient['gender']}")
        st.write(f"**Symptoms:** {', '.join(patient['symptoms'])}")
        symptoms = patient['symptoms']

    X = prepare_symptoms_array(symptoms)
   


    # Trigger XGBoost model
    if st.button('Predict'): 
        if not symptoms:
            st.warning('Please select at least one symptom to predict.')

        else:   
        # Run the model with the python script
        
            prediction, prob = disease_model.predict(X)
            st.write(f'## Disease: {prediction} with {prob*100:.2f}% probability')


            tab1, tab2,tab3= st.tabs(["Description", "Precautions","Doctor Recommendation"])

            with tab1:
                st.write(disease_model.describe_predicted_disease())

            with tab2:
                precautions = disease_model.predicted_disease_precautions()
                for i in range(4):
                    st.write(f'{i+1}. {precautions[i]}')
            with tab3:
                show_doctor_info(prediction)                       
                


# Diabetes prediction page
if selected == 'Diabetes Prediction':  # pagetitle
    st.title("Diabetes disease prediction")
    image = Image.open('d3.jpg')
    st.image(image, caption='diabetes disease prediction')
    # columns
    # no inputs from the user
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input("Number of Pregnancies")
    with col2:
        Glucose = st.number_input("Glucose level")
    with col3:
        BloodPressure = st.number_input("Blood pressure  value")
    with col1:

        SkinThickness = st.number_input("Sckinthickness value")

    with col2:

        Insulin = st.number_input("Insulin value ")
    with col3:
        BMI = st.number_input("BMI value")
    with col1:
        DiabetesPedigreefunction = st.number_input(
            "Diabetes pedigree function value")
    with col2:

        Age = st.number_input("AGE")

    # code for prediction
    diabetes_dig = ''

    # button
    if st.button("Diabetes test result"):
        diabetes_prediction=[[]]
        diabetes_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreefunction, Age]])

        # after the prediction is done if the value in the list at index is 0 is 1 then the person is diabetic
        if diabetes_prediction[0] == 1:
            diabetes_dig = "we are really sorry to say but it seems like you are Diabetic."
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            show_doctor_info("diabetes")
            # PDF report
            doctor_info = get_doctor_details("diabetes")
            pdf_link = generate_pdf_report(name, "Diabetes", "Positive", doctor_info)
            st.markdown(pdf_link, unsafe_allow_html=True)

        else:
            diabetes_dig = 'Congratulation,You are not diabetic'
            image = Image.open('negative.jpg')
            st.image(image, caption='')
        st.success(name+'   ' + diabetes_dig)            



# Heart prediction page
if selected == 'Heart disease Prediction':
    st.title("Heart disease prediction")
    image = Image.open('heart2.jpg')
    st.image(image, caption='heart failuire')
    # age	sex	cp	trestbps	chol	fbs	restecg	thalach	exang	oldpeak	slope	ca	thal	target
    # columns
    # no inputs from the user
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age")
    with col2:
        sex=0
        display = ("male", "female")
        options = list(range(len(display)))
        value = st.selectbox("Gender", options, format_func=lambda x: display[x])
        if value == "male":
            sex = 1
        elif value == "female":
            sex = 0
    with col3:
        cp=0
        display = ("typical angina","atypical angina","non — anginal pain","asymptotic")
        options = list(range(len(display)))
        value = st.selectbox("Chest_Pain Type", options, format_func=lambda x: display[x])
        if value == "typical angina":
            cp = 0
        elif value == "atypical angina":
            cp = 1
        elif value == "non — anginal pain":
            cp = 2
        elif value == "asymptotic":
            cp = 3
    with col1:
        trestbps = st.number_input("Resting Blood Pressure")

    with col2:

        chol = st.number_input("Serum Cholestrol")
    
    with col3:
        restecg=0
        display = ("normal","having ST-T wave abnormality","left ventricular hyperthrophy")
        options = list(range(len(display)))
        value = st.selectbox("Resting ECG", options, format_func=lambda x: display[x])
        if value == "normal":
            restecg = 0
        elif value == "having ST-T wave abnormality":
            restecg = 1
        elif value == "left ventricular hyperthrophy":
            restecg = 2

    with col1:
        exang=0
        thalach = st.number_input("Max Heart Rate Achieved")
   
    with col2:
        oldpeak = st.number_input("ST depression induced by exercise relative to rest")
    with col3:
        slope=0
        display = ("upsloping","flat","downsloping")
        options = list(range(len(display)))
        value = st.selectbox("Peak exercise ST segment", options, format_func=lambda x: display[x])
        if value == "upsloping":
            slope = 0
        elif value == "flat":
            slope = 1
        elif value == "downsloping":
            slope = 2
    with col1:
        ca = st.number_input("Number of major vessels (0–3) colored by flourosopy")
    with col2:
        thal=0
        display = ("normal","fixed defect","reversible defect")
        options = list(range(len(display)))
        value = st.selectbox("thalassemia", options, format_func=lambda x: display[x])
        if value == "normal":
            thal = 0
        elif value == "fixed defect":
            thal = 1
        elif value == "reversible defect":
            thal = 2
    with col3:
        agree = st.checkbox('Exercise induced angina')
        if agree:
            exang = 1
        else:
            exang=0
    with col1:
        agree1 = st.checkbox('fasting blood sugar > 120mg/dl')
        if agree1:
            fbs = 1
        else:
            fbs=0
    # code for prediction
    heart_dig = ''
    

    # button
    if st.button("Heart test result"):
        heart_prediction=[[]]
        # change the parameters according to the model
        
        # b=np.array(a, dtype=float)
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_dig = 'we are really sorry to say but it seems like you have Heart Disease. '
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            show_doctor_info("heart") 
        else:
            heart_dig = "Congratulation, You don't have Heart Disease."
            image = Image.open('negative.jpg')
            st.image(image, caption='')
        st.success(name +'  ' + heart_dig)



if selected == 'Parkison Prediction':
    st.title("Parkison prediction")
    image = Image.open('p1.jpg')
    st.image(image, caption='parkinsons disease')
  # parameters
#    name	MDVP:Fo(Hz)	MDVP:Fhi(Hz)	MDVP:Flo(Hz)	MDVP:Jitter(%)	MDVP:Jitter(Abs)	MDVP:RAP	MDVP:PPQ	Jitter:DDP	MDVP:Shimmer	MDVP:Shimmer(dB)	Shimmer:APQ3	Shimmer:APQ5	MDVP:APQ	Shimmer:DDA	NHR	HNR	status	RPDE	DFA	spread1	spread2	D2	PPE
   # change the variables according to the dataset used in the model
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP = st.number_input("MDVP:Fo(Hz)")
    with col2:
        MDVPFIZ = st.number_input("MDVP:Fhi(Hz)")
    with col3:
        MDVPFLO = st.number_input("MDVP:Flo(Hz)")
    with col1:
        MDVPJITTER = st.number_input("MDVP:Jitter(%)")
    with col2:
        MDVPJitterAbs = st.number_input("MDVP:Jitter(Abs)")
    with col3:
        MDVPRAP = st.number_input("MDVP:RAP")

    with col2:

        MDVPPPQ = st.number_input("MDVP:PPQ ")
    with col3:
        JitterDDP = st.number_input("Jitter:DDP")
    with col1:
        MDVPShimmer = st.number_input("MDVP:Shimmer")
    with col2:
        MDVPShimmer_dB = st.number_input("MDVP:Shimmer(dB)")
    with col3:
        Shimmer_APQ3 = st.number_input("Shimmer:APQ3")
    with col1:
        ShimmerAPQ5 = st.number_input("Shimmer:APQ5")
    with col2:
        MDVP_APQ = st.number_input("MDVP:APQ")
    with col3:
        ShimmerDDA = st.number_input("Shimmer:DDA")
    with col1:
        NHR = st.number_input("NHR")
    with col2:
        HNR = st.number_input("HNR")
  
    with col2:
        RPDE = st.number_input("RPDE")
    with col3:
        DFA = st.number_input("DFA")
    with col1:
        spread1 = st.number_input("spread1")
    with col1:
        spread2 = st.number_input("spread2")
    with col3:
        D2 = st.number_input("D2")
    with col1:
        PPE = st.number_input("PPE")

    # code for prediction
    parkinson_dig = ''
    
    # button
    if st.button("Parkinson test result"):
        parkinson_prediction=[[]]
        # change the parameters according to the model
        parkinson_prediction = parkinson_model.predict([[MDVP, MDVPFIZ, MDVPFLO, MDVPJITTER, MDVPJitterAbs, MDVPRAP, MDVPPPQ, JitterDDP, MDVPShimmer,MDVPShimmer_dB, Shimmer_APQ3, ShimmerAPQ5, MDVP_APQ, ShimmerDDA, NHR, HNR,  RPDE, DFA, spread1, spread2, D2, PPE]])

        if parkinson_prediction[0] == 1:
            parkinson_dig = 'we are really sorry to say but it seems like you have Parkinson disease'
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            show_doctor_info("parkinson")

        else:
            parkinson_dig = "Congratulation , You don't have Parkinson disease"
            image = Image.open('negative.jpg')
            st.image(image, caption='')
        st.success(name+'  ' + parkinson_dig)



# Load the dataset
lung_cancer_data = pd.read_csv('data/lung_cancer.csv')

# Convert 'M' to 0 and 'F' to 1 in the 'GENDER' column
lung_cancer_data['GENDER'] = lung_cancer_data['GENDER'].map({'M': 'Male', 'F': 'Female'})

# Lung Cancer prediction page
if selected == 'Lung Cancer Prediction':
    st.title("Lung Cancer Prediction")
    image = Image.open('h.png')
    st.image(image, caption='Lung Cancer Prediction')

    # Columns
    # No inputs from the user
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender:", lung_cancer_data['GENDER'].unique())
    with col2:
        age = st.number_input("Age")
    with col3:
        smoking = st.selectbox("Smoking:", ['NO', 'YES'])
    with col1:
        yellow_fingers = st.selectbox("Yellow Fingers:", ['NO', 'YES'])

    with col2:
        anxiety = st.selectbox("Anxiety:", ['NO', 'YES'])
    with col3:
        peer_pressure = st.selectbox("Peer Pressure:", ['NO', 'YES'])
    with col1:
        chronic_disease = st.selectbox("Chronic Disease:", ['NO', 'YES'])

    with col2:
        fatigue = st.selectbox("Fatigue:", ['NO', 'YES'])
    with col3:
        allergy = st.selectbox("Allergy:", ['NO', 'YES'])
    with col1:
        wheezing = st.selectbox("Wheezing:", ['NO', 'YES'])

    with col2:
        alcohol_consuming = st.selectbox("Alcohol Consuming:", ['NO', 'YES'])
    with col3:
        coughing = st.selectbox("Coughing:", ['NO', 'YES'])
    with col1:
        shortness_of_breath = st.selectbox("Shortness of Breath:", ['NO', 'YES'])

    with col2:
        swallowing_difficulty = st.selectbox("Swallowing Difficulty:", ['NO', 'YES'])
    with col3:
        chest_pain = st.selectbox("Chest Pain:", ['NO', 'YES'])

    # Code for prediction
    cancer_result = ''

    # Button
    if st.button("Predict Lung Cancer"):
        # Create a DataFrame with user inputs
        user_data = pd.DataFrame({
            'GENDER': [gender],
            'AGE': [age],
            'SMOKING': [smoking],
            'YELLOW_FINGERS': [yellow_fingers],
            'ANXIETY': [anxiety],
            'PEER_PRESSURE': [peer_pressure],
            'CHRONICDISEASE': [chronic_disease],
            'FATIGUE': [fatigue],
            'ALLERGY': [allergy],
            'WHEEZING': [wheezing],
            'ALCOHOLCONSUMING': [alcohol_consuming],
            'COUGHING': [coughing],
            'SHORTNESSOFBREATH': [shortness_of_breath],
            'SWALLOWINGDIFFICULTY': [swallowing_difficulty],
            'CHESTPAIN': [chest_pain]
        })

        # Map string values to numeric
        user_data.replace({'NO': 1, 'YES': 2}, inplace=True)

        # Strip leading and trailing whitespaces from column names
        user_data.columns = user_data.columns.str.strip()

        # Convert columns to numeric where necessary
        numeric_columns = ['AGE', 'FATIGUE', 'ALLERGY', 'ALCOHOLCONSUMING', 'COUGHING', 'SHORTNESSOFBREATH']
        user_data[numeric_columns] = user_data[numeric_columns].apply(pd.to_numeric, errors='coerce')

        # Perform prediction
        cancer_prediction = lung_cancer_model.predict(user_data)

        # Display result
        if cancer_prediction[0] == 'YES':
            cancer_result = "The model predicts that there is a risk of Lung Cancer."
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            show_doctor_info("lung_cancer")
            
        else:
            cancer_result = "The model predicts no significant risk of Lung Cancer."
            image = Image.open('negative.jpg')
            st.image(image, caption='')

        st.success(name + ' ' + cancer_result)




# Liver prediction page
if selected == 'Liver Prediction':  # pagetitle
    st.title("Liver disease prediction")
    image = Image.open('liver.jpg')
    st.image(image, caption='Liver disease prediction.')
    # columns
    # no inputs from the user
# st.write(info.astype(int).info())
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        Sex=0
        display = ("male", "female")
        options = list(range(len(display)))
        value = st.selectbox("Gender", options, format_func=lambda x: display[x])
        if value == "male":
            Sex = 0
        elif value == "female":
            Sex = 1
    with col2:
        age = st.number_input("Entre your age") # 2 
    with col3:
        Total_Bilirubin = st.number_input("Entre your Total_Bilirubin") # 3
    with col1:
        Direct_Bilirubin = st.number_input("Entre your Direct_Bilirubin")# 4

    with col2:
        Alkaline_Phosphotase = st.number_input("Entre your Alkaline_Phosphotase") # 5
    with col3:
        Alamine_Aminotransferase = st.number_input("Entre your Alamine_Aminotransferase") # 6
    with col1:
        Aspartate_Aminotransferase = st.number_input("Entre your Aspartate_Aminotransferase") # 7
    with col2:
        Total_Protiens = st.number_input("Entre your Total_Protiens")# 8
    with col3:
        Albumin = st.number_input("Entre your Albumin") # 9
    with col1:
        Albumin_and_Globulin_Ratio = st.number_input("Entre your Albumin_and_Globulin_Ratio") # 10 
    # code for prediction
    liver_dig = ''

    # button
    if st.button("Liver test result"):
        liver_prediction=[[]]
        liver_prediction = liver_model.predict([[Sex,age,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])

        # after the prediction is done if the value in the list at index is 0 is 1 then the person is diabetic
        if liver_prediction[0] == 1:
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            liver_dig = "we are really sorry to say but it seems like you have liver disease."
            show_doctor_info("liver")
        else:
            image = Image.open('negative.jpg')
            st.image(image, caption='')
            liver_dig = "Congratulation , You don't have liver disease."
        st.success(name+'  ' + liver_dig)




# Hepatitis prediction page
if selected == 'Hepatitis Prediction':
    st.title("Hepatitis Prediction")
    image = Image.open('h.png')
    st.image(image, caption='Hepatitis Prediction')

    # Columns
    # No inputs from the user
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Enter your age")  # 2
    with col2:
        sex = st.selectbox("Gender", ["Male", "Female"])
        sex = 1 if sex == "Male" else 2
    with col3:
        total_bilirubin = st.number_input("Enter your Total Bilirubin")  # 3

    with col1:
        direct_bilirubin = st.number_input("Enter your Direct Bilirubin")  # 4
    with col2:
        alkaline_phosphatase = st.number_input("Enter your Alkaline Phosphatase")  # 5
    with col3:
        alamine_aminotransferase = st.number_input("Enter your Alamine Aminotransferase")  # 6

    with col1:
        aspartate_aminotransferase = st.number_input("Enter your Aspartate Aminotransferase")  # 7
    with col2:
        total_proteins = st.number_input("Enter your Total Proteins")  # 8
    with col3:
        albumin = st.number_input("Enter your Albumin")  # 9

    with col1:
        albumin_and_globulin_ratio = st.number_input("Enter your Albumin and Globulin Ratio")  # 10

    with col2:
        your_ggt_value = st.number_input("Enter your GGT value")  # Add this line
    with col3:
        your_prot_value = st.number_input("Enter your PROT value")  # Add this line

    # Code for prediction
    hepatitis_result = ''

    # Button
    if st.button("Predict Hepatitis"):
        # Create a DataFrame with user inputs
        user_data = pd.DataFrame({
            'Age': [age],
            'Sex': [sex],
            'ALB': [total_bilirubin],  # Correct the feature name
            'ALP': [direct_bilirubin],  # Correct the feature name
            'ALT': [alkaline_phosphatase],  # Correct the feature name
            'AST': [alamine_aminotransferase],
            'BIL': [aspartate_aminotransferase],  # Correct the feature name
            'CHE': [total_proteins],  # Correct the feature name
            'CHOL': [albumin],  # Correct the feature name
            'CREA': [albumin_and_globulin_ratio],  # Correct the feature name
            'GGT': [your_ggt_value],  # Replace 'your_ggt_value' with the actual value
            'PROT': [your_prot_value]  # Replace 'your_prot_value' with the actual value
        })

        # Perform prediction
        hepatitis_prediction = hepatitis_model.predict(user_data)
        # Display result
        if hepatitis_prediction[0] == 1:
            hepatitis_result = "We are really sorry to say but it seems like you have Hepatitis."
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            show_doctor_info("hepatitis")
        else:
            hepatitis_result = 'Congratulations, you do not have Hepatitis.'
            image = Image.open('negative.jpg')
            st.image(image, caption='')

        st.success(name + ' ' + hepatitis_result)




# jaundice prediction page
if selected == 'Jaundice Prediction':  # pagetitle
    st.title("Jaundice disease prediction")
    image = Image.open('j.jpg')
    st.image(image, caption='Jaundice disease prediction')
    # columns
    # no inputs from the user
# st.write(info.astype(int).info())
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Entre your age   ") # 2 
    with col2:
        Sex=0
        display = ("male", "female")
        options = list(range(len(display)))
        value = st.selectbox("Gender", options, format_func=lambda x: display[x])
        if value == "male":
            Sex = 0
        elif value == "female":
            Sex = 1
    with col3:
        Total_Bilirubin = st.number_input("Entre your Total_Bilirubin") # 3
    with col1:
        Direct_Bilirubin = st.number_input("Entre your Direct_Bilirubin")# 4

    with col2:
        Alkaline_Phosphotase = st.number_input("Entre your Alkaline_Phosphotase") # 5
    with col3:
        Alamine_Aminotransferase = st.number_input("Entre your Alamine_Aminotransferase") # 6
    with col1:
        Total_Protiens = st.number_input("Entre your Total_Protiens")# 8
    with col2:
        Albumin = st.number_input("Entre your Albumin") # 9 
    # code for prediction
    jaundice_dig = ''

    # button
    if st.button("Jaundice test result"):
        jaundice_prediction=[[]]
        jaundice_prediction = jaundice_model.predict([[age,Sex,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Total_Protiens,Albumin]])

        # after the prediction is done if the value in the list at index is 0 is 1 then the person is diabetic
        if jaundice_prediction[0] == 1:
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            jaundice_dig = "we are really sorry to say but it seems like you have Jaundice."
            show_doctor_info("jaundice")
        else:
            image = Image.open('negative.jpg')
            st.image(image, caption='')
            jaundice_dig = "Congratulation , You don't have Jaundice."
        st.success(name+'  ' + jaundice_dig)





from sklearn.preprocessing import LabelEncoder
import joblib


# Chronic Kidney Disease Prediction Page
if selected == 'Chronic Kidney Prediction':
    st.title("Chronic Kidney Disease Prediction")
    # Add the image for Chronic Kidney Disease prediction if needed
    name = st.text_input("Name:")
    # Columns
    # No inputs from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Enter your age", 1, 100, 25)  # 2
    with col2:
        bp = st.slider("Enter your Blood Pressure", 50, 200, 120)  # Add your own ranges
    with col3:
        sg = st.slider("Enter your Specific Gravity", 1.0, 1.05, 1.02)  # Add your own ranges

    with col1:
        al = st.slider("Enter your Albumin", 0, 5, 0)  # Add your own ranges
    with col2:
        su = st.slider("Enter your Sugar", 0, 5, 0)  # Add your own ranges
    with col3:
        rbc = st.selectbox("Red Blood Cells", ["Normal", "Abnormal"])
        rbc = 1 if rbc == "Normal" else 0

    with col1:
        pc = st.selectbox("Pus Cells", ["Normal", "Abnormal"])
        pc = 1 if pc == "Normal" else 0
    with col2:
        pcc = st.selectbox("Pus Cell Clumps", ["Present", "Not Present"])
        pcc = 1 if pcc == "Present" else 0
    with col3:
        ba = st.selectbox("Bacteria", ["Present", "Not Present"])
        ba = 1 if ba == "Present" else 0

    with col1:
        bgr = st.slider("Enter your Blood Glucose Random", 50, 200, 120)  # Add your own ranges
    with col2:
        bu = st.slider("Enter your Blood Urea", 10, 200, 60)  # Add your own ranges
    with col3:
        sc = st.slider("Enter your Serum Creatinine", 0, 10, 3)  # Add your own ranges

    with col1:
        sod = st.slider("Enter your Sodium", 100, 200, 140)  # Add your own ranges
    with col2:
        pot = st.slider("Enter your Potassium", 2, 7, 4)  # Add your own ranges
    with col3:
        hemo = st.slider("Enter your Hemoglobin", 3, 17, 12)  # Add your own ranges

    with col1:
        pcv = st.slider("Enter your Packed Cell Volume", 20, 60, 40)  # Add your own ranges
    with col2:
        wc = st.slider("Enter your White Blood Cell Count", 2000, 20000, 10000)  # Add your own ranges
    with col3:
        rc = st.slider("Enter your Red Blood Cell Count", 2, 8, 4)  # Add your own ranges

    with col1:
        htn = st.selectbox("Hypertension", ["Yes", "No"])
        htn = 1 if htn == "Yes" else 0
    with col2:
        dm = st.selectbox("Diabetes Mellitus", ["Yes", "No"])
        dm = 1 if dm == "Yes" else 0
    with col3:
        cad = st.selectbox("Coronary Artery Disease", ["Yes", "No"])
        cad = 1 if cad == "Yes" else 0

    with col1:
        appet = st.selectbox("Appetite", ["Good", "Poor"])
        appet = 1 if appet == "Good" else 0
    with col2:
        pe = st.selectbox("Pedal Edema", ["Yes", "No"])
        pe = 1 if pe == "Yes" else 0
    with col3:
        ane = st.selectbox("Anemia", ["Yes", "No"])
        ane = 1 if ane == "Yes" else 0

    # Code for prediction
    kidney_result = ''

    # Button
    if st.button("Predict Chronic Kidney Disease"):
        # Create a DataFrame with user inputs
        user_input = pd.DataFrame({
            'age': [age],
            'bp': [bp],
            'sg': [sg],
            'al': [al],
            'su': [su],
            'rbc': [rbc],
            'pc': [pc],
            'pcc': [pcc],
            'ba': [ba],
            'bgr': [bgr],
            'bu': [bu],
            'sc': [sc],
            'sod': [sod],
            'pot': [pot],
            'hemo': [hemo],
            'pcv': [pcv],
            'wc': [wc],
            'rc': [rc],
            'htn': [htn],
            'dm': [dm],
            'cad': [cad],
            'appet': [appet],
            'pe': [pe],
            'ane': [ane]
        })

        # Perform prediction
        kidney_prediction = chronic_disease_model.predict(user_input)
        # Display result
        if kidney_prediction[0] == 1:
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            kidney_prediction_dig = "we are really sorry to say but it seems like you have kidney disease."
            show_doctor_info("kidney")
        else:
            image = Image.open('negative.jpg')
            st.image(image, caption='')
            kidney_prediction_dig = "Congratulation , You don't have kidney disease."
        st.success(name+'  ' + kidney_prediction_dig)



# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    st.title("Breast Cancer Prediction")
    name = st.text_input("Name:")
    # Columns
    # No inputs from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.slider("Enter your Radius Mean", 6.0, 30.0, 15.0)
        texture_mean = st.slider("Enter your Texture Mean", 9.0, 40.0, 20.0)
        perimeter_mean = st.slider("Enter your Perimeter Mean", 43.0, 190.0, 90.0)

    with col2:
        area_mean = st.slider("Enter your Area Mean", 143.0, 2501.0, 750.0)
        smoothness_mean = st.slider("Enter your Smoothness Mean", 0.05, 0.25, 0.1)
        compactness_mean = st.slider("Enter your Compactness Mean", 0.02, 0.3, 0.15)

    with col3:
        concavity_mean = st.slider("Enter your Concavity Mean", 0.0, 0.5, 0.2)
        concave_points_mean = st.slider("Enter your Concave Points Mean", 0.0, 0.2, 0.1)
        symmetry_mean = st.slider("Enter your Symmetry Mean", 0.1, 1.0, 0.5)

    with col1:
        fractal_dimension_mean = st.slider("Enter your Fractal Dimension Mean", 0.01, 0.1, 0.05)
        radius_se = st.slider("Enter your Radius SE", 0.1, 3.0, 1.0)
        texture_se = st.slider("Enter your Texture SE", 0.2, 2.0, 1.0)

    with col2:
        perimeter_se = st.slider("Enter your Perimeter SE", 1.0, 30.0, 10.0)
        area_se = st.slider("Enter your Area SE", 6.0, 500.0, 150.0)
        smoothness_se = st.slider("Enter your Smoothness SE", 0.001, 0.03, 0.01)

    with col3:
        compactness_se = st.slider("Enter your Compactness SE", 0.002, 0.2, 0.1)
        concavity_se = st.slider("Enter your Concavity SE", 0.0, 0.05, 0.02)
        concave_points_se = st.slider("Enter your Concave Points SE", 0.0, 0.03, 0.01)

    with col1:
        symmetry_se = st.slider("Enter your Symmetry SE", 0.1, 1.0, 0.5)
        fractal_dimension_se = st.slider("Enter your Fractal Dimension SE", 0.01, 0.1, 0.05)

    with col2:
        radius_worst = st.slider("Enter your Radius Worst", 7.0, 40.0, 20.0)
        texture_worst = st.slider("Enter your Texture Worst", 12.0, 50.0, 25.0)
        perimeter_worst = st.slider("Enter your Perimeter Worst", 50.0, 250.0, 120.0)

    with col3:
        area_worst = st.slider("Enter your Area Worst", 185.0, 4250.0, 1500.0)
        smoothness_worst = st.slider("Enter your Smoothness Worst", 0.07, 0.3, 0.15)
        compactness_worst = st.slider("Enter your Compactness Worst", 0.03, 0.6, 0.3)

    with col1:
        concavity_worst = st.slider("Enter your Concavity Worst", 0.0, 0.8, 0.4)
        concave_points_worst = st.slider("Enter your Concave Points Worst", 0.0, 0.2, 0.1)
        symmetry_worst = st.slider("Enter your Symmetry Worst", 0.1, 1.0, 0.5)

    with col2:
        fractal_dimension_worst = st.slider("Enter your Fractal Dimension Worst", 0.01, 0.2, 0.1)

        # Code for prediction
    breast_cancer_result = ''

    # Button
    if st.button("Predict Breast Cancer"):
        # Create a DataFrame with user inputs
        user_input = pd.DataFrame({
            'radius_mean': [radius_mean],
            'texture_mean': [texture_mean],
            'perimeter_mean': [perimeter_mean],
            'area_mean': [area_mean],
            'smoothness_mean': [smoothness_mean],
            'compactness_mean': [compactness_mean],
            'concavity_mean': [concavity_mean],
            'concave points_mean': [concave_points_mean],  # Update this line
            'symmetry_mean': [symmetry_mean],
            'fractal_dimension_mean': [fractal_dimension_mean],
            'radius_se': [radius_se],
            'texture_se': [texture_se],
            'perimeter_se': [perimeter_se],
            'area_se': [area_se],
            'smoothness_se': [smoothness_se],
            'compactness_se': [compactness_se],
            'concavity_se': [concavity_se],
            'concave points_se': [concave_points_se],  # Update this line
            'symmetry_se': [symmetry_se],
            'fractal_dimension_se': [fractal_dimension_se],
            'radius_worst': [radius_worst],
            'texture_worst': [texture_worst],
            'perimeter_worst': [perimeter_worst],
            'area_worst': [area_worst],
            'smoothness_worst': [smoothness_worst],
            'compactness_worst': [compactness_worst],
            'concavity_worst': [concavity_worst],
            'concave points_worst': [concave_points_worst],  # Update this line
            'symmetry_worst': [symmetry_worst],
            'fractal_dimension_worst': [fractal_dimension_worst],
        })

        # Perform prediction
        breast_cancer_prediction = breast_cancer_model.predict(user_input)
        # Display result
        if breast_cancer_prediction[0] == 1:
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            breast_cancer_result = "The model predicts that you have Breast Cancer."
            show_doctor_info("breast_cancer")
        else:
            image = Image.open('negative.jpg')
            st.image(image, caption='')
            breast_cancer_result = "The model predicts that you don't have Breast Cancer."

        st.success(breast_cancer_result)

import streamlit as st

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
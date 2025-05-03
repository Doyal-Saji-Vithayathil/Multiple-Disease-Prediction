import streamlit as st

def get_doctor_details(specialty):
    details = {
        "heart": """Dr. Arjun Menon
Cardiology Specialist
Apollo Hospitals, Bengaluru
Phone: +91-98765-43210
Email: arjun.menon@apollohospitals.com
Website: https://www.apollohospitals.com/""",

        "parkinson": """Dr. Meera Iyer
Senior Neurologist – Movement Disorders
NIMHANS, Bengaluru
Phone: +91-99887-65432
Email: meera.iyer@nimhans.ac.in
Website: https://nimhans.ac.in/""",

        "lung_cancer": """Dr. Rajesh Sharma
Thoracic Oncologist
Tata Memorial Hospital, Mumbai
Phone: +91-91234-56789
Email: rajesh.sharma@tmh.org.in
Website: https://tmc.gov.in/""",

        "liver": """Dr. Kavita Nair
Liver Specialist
Manipal Hospitals, Hyderabad
Phone: +91-92345-67890
Email: kavita.nair@manipalhospitals.com
Website: https://www.manipalhospitals.com/""",

        "hepatitis": """Dr. Sandeep Varma
Hepatitis & Liver Infection Expert
Fortis Hospital, Delhi
Phone: +91-93456-78901
Email: sandeep.varma@fortishealthcare.com
Website: https://www.fortishealthcare.com/""",

        "jaundice": """Dr. Anjali Deshmukh
Senior Consultant, Internal Medicine
Max Healthcare, Pune
Phone: +91-94567-12345
Email: anjali.deshmukh@maxhealthcare.com
Website: https://www.maxhealthcare.in/""",

        "kidney": """Dr. Naveen Reddy
Kidney Specialist
Aster Hospitals, Kochi
Phone: +91-97654-32109
Email: naveen.reddy@asterhospitals.com
Website: https://www.asterhospitals.in/""",

        "breast_cancer": """Dr. Neha Kapoor
Surgical Oncologist – Breast Cancer
AIIMS, New Delhi
Phone: +91-90123-45678
Email: neha.kapoor@aiims.edu
Website: https://www.aiims.edu/""",

        "diabetes": """Dr. Ritu Joshi
Diabetes & Hormone Specialist
Medanta – The Medicity, Gurugram
Phone: +91-90909-80808
Email: ritu.joshi@medanta.org
Website: https://www.medanta.org/""",

        "fungal infection": """Dr. Meera Kapoor
Dermatology Specialist
Fortis Hospital, Mumbai
Phone: +91-91234-56789
Email: meera.kapoor@fortishealth.com
Website: https://www.fortishealthcare.com/""",

        "allergy": """Dr. Rakesh Sharma
Allergy & Immunology Specialist
Max Healthcare, Delhi
Phone: +91-99887-66554
Email: rakesh.sharma@maxhealthcare.com
Website: https://www.maxhealthcare.in/""",

        "gerd": """Dr. Priya Nair
Gastroenterology Specialist
Manipal Hospitals, Bengaluru
Phone: +91-98765-12345
Email: priya.nair@manipalhospitals.com
Website: https://www.manipalhospitals.com/""",

        "chronic cholestasis": """Dr. Sameer Joshi
Liver & Hepatology Specialist
Medanta, Gurugram
Phone: +91-87654-32109
Email: sameer.joshi@medanta.org
Website: https://www.medanta.org/""",

        "drug reaction": """Dr. Sneha Verma
Clinical Pharmacology Specialist
AIIMS, Delhi
Phone: +91-90000-11122
Email: sneha.verma@aiims.edu
Website: https://www.aiims.edu/""",

        "peptic ulcer diseae": """Dr. Priya Nair
Gastroenterology Specialist
Manipal Hospitals, Bengaluru
Phone: +91-98765-12345
Email: priya.nair@manipalhospitals.com
Website: https://www.manipalhospitals.com/""",

        "aids": """Dr. Anil Deshmukh
Infectious Disease Specialist
Jaslok Hospital, Mumbai
Phone: +91-99888-22334
Email: anil.deshmukh@jaslokhospital.net
Website: https://www.jaslokhospital.net/""",

        "gastroenteritis": """Dr. Priya Nair
Gastroenterology Specialist
Manipal Hospitals, Bengaluru
Phone: +91-98765-12345
Email: priya.nair@manipalhospitals.com
Website: https://www.manipalhospitals.com/""",

        "bronchial asthma": """Dr. Rajeev Kumar
Pulmonology Specialist
Fortis Hospital, Delhi
Phone: +91-92233-44556
Email: rajeev.kumar@fortishealth.com
Website: https://www.fortishealthcare.com/""",

        "hypertension": """Dr. Arjun Menon
Cardiology Specialist
Apollo Hospitals, Bengaluru
Phone: +91-98765-43210
Email: arjun.menon@apollohospitals.com
Website: https://www.apollohospitals.com/""",

        "migraine": """Dr. Neha Sood
Neurology Specialist
Max Healthcare, Delhi
Phone: +91-91122-33445
Email: neha.sood@maxhealthcare.com
Website: https://www.maxhealthcare.in/""",

        "cervical spondylosis": """Dr. Vikram Singh
Orthopedics Specialist
Medanta, Gurugram
Phone: +91-90012-34567
Email: vikram.singh@medanta.org
Website: https://www.medanta.org/""",

        "paralysis (brain hemorrhage)": """Dr. Neha Sood
Neurology Specialist
Max Healthcare, Delhi
Phone: +91-91122-33445
Email: neha.sood@maxhealthcare.com
Website: https://www.maxhealthcare.in/""",

        "malaria": """Dr. Sunita Gupta
General Medicine
AIIMS, Delhi
Phone: +91-98767-89012
Email: sunita.gupta@aiims.edu
Website: https://www.aiims.edu/""",

        "chicken pox": """Dr. Anil Deshmukh
Infectious Disease Specialist
Jaslok Hospital, Mumbai
Phone: +91-99888-22334
Email: anil.deshmukh@jaslokhospital.net
Website: https://www.jaslokhospital.net/""",

        "dengue": """Dr. Sunita Gupta
General Medicine
AIIMS, Delhi
Phone: +91-98767-89012
Email: sunita.gupta@aiims.edu
Website: https://www.aiims.edu/""",

        "typhoid": """Dr. Sunita Gupta
General Medicine
AIIMS, Delhi
Phone: +91-98767-89012
Email: sunita.gupta@aiims.edu
Website: https://www.aiims.edu/""",

        "hepatitis a": """Dr. Sameer Joshi
Liver & Hepatology Specialist
Medanta, Gurugram
Phone: +91-87654-32109
Email: sameer.joshi@medanta.org
Website: https://www.medanta.org/""",

        "hepatitis b": """Dr. Sameer Joshi
Liver & Hepatology Specialist
Medanta, Gurugram
Phone: +91-87654-32109
Email: sameer.joshi@medanta.org
Website: https://www.medanta.org/""",

        "hepatitis c": """Dr. Sameer Joshi
Liver & Hepatology Specialist
Medanta, Gurugram
Phone: +91-87654-32109
Email: sameer.joshi@medanta.org
Website: https://www.medanta.org/""",

        "hepatitis d": """Dr. Sameer Joshi
Liver & Hepatology Specialist
Medanta, Gurugram
Phone: +91-87654-32109
Email: sameer.joshi@medanta.org
Website: https://www.medanta.org/""",

        "hepatitis e": """Dr. Sameer Joshi
Liver & Hepatology Specialist
Medanta, Gurugram
Phone: +91-87654-32109
Email: sameer.joshi@medanta.org
Website: https://www.medanta.org/""",

        "alcoholic hepatitis": """Dr. Sameer Joshi
Liver & Hepatology Specialist
Medanta, Gurugram
Phone: +91-87654-32109
Email: sameer.joshi@medanta.org
Website: https://www.medanta.org/""",

        "tuberculosis": """Dr. Rajeev Kumar
Pulmonology Specialist
Fortis Hospital, Delhi
Phone: +91-92233-44556
Email: rajeev.kumar@fortishealth.com
Website: https://www.fortishealthcare.com/""",

        "common cold": """Dr. Sunita Gupta
General Medicine
AIIMS, Delhi
Phone: +91-98767-89012
Email: sunita.gupta@aiims.edu
Website: https://www.aiims.edu/""",

        "pneumonia": """Dr. Rajeev Kumar
Pulmonology Specialist
Fortis Hospital, Delhi
Phone: +91-92233-44556
Email: rajeev.kumar@fortishealth.com
Website: https://www.fortishealthcare.com/""",

        "dimorphic hemmorhoids(piles)": """Dr. Nitin Desai
General Surgery Specialist
Apollo Hospitals, Mumbai
Phone: +91-98876-54321
Email: nitin.desai@apollohospitals.com
Website: https://www.apollohospitals.com/""",

        "heart attack": """Dr. Arjun Menon
Cardiology Specialist
Apollo Hospitals, Bengaluru
Phone: +91-98765-43210
Email: arjun.menon@apollohospitals.com
Website: https://www.apollohospitals.com/""",

        "varicose veins": """Dr. Shalini Bhatt
Vascular Surgery Specialist
Fortis Hospital, Delhi
Phone: +91-91123-45678
Email: shalini.bhatt@fortishealth.com
Website: https://www.fortishealthcare.com/""",

        "hypothyroidism": """Dr. Kavita Rao
Endocrinology Specialist
Apollo Hospitals, Chennai
Phone: +91-98765-43211
Email: kavita.rao@apollohospitals.com
Website: https://www.apollohospitals.com/""",

        "hyperthyroidism": """Dr. Kavita Rao
Endocrinology Specialist
Apollo Hospitals, Chennai
Phone: +91-98765-43211
Email: kavita.rao@apollohospitals.com
Website: https://www.apollohospitals.com/""",

        "hypoglycemia": """Dr. Kavita Rao
Endocrinology Specialist
Apollo Hospitals, Chennai
Phone: +91-98765-43211
Email: kavita.rao@apollohospitals.com
Website: https://www.apollohospitals.com/""",

        "osteoarthristis": """Dr. Vikram Singh
Orthopedics Specialist
Medanta, Gurugram
Phone: +91-90012-34567
Email: vikram.singh@medanta.org
Website: https://www.medanta.org/""",

        "arthritis": """Dr. Alka Jain
Rheumatology Specialist
Fortis Hospital, Mumbai
Phone: +91-98876-54322
Email: alka.jain@fortishealth.com
Website: https://www.fortishealthcare.com/""",

        "(vertigo) paroymsal positional vertigo": """Dr. Neha Sood
Neurology Specialist
Max Healthcare, Delhi
Phone: +91-91122-33445
Email: neha.sood@maxhealthcare.com
Website: https://www.maxhealthcare.in/""",

        "acne": """Dr. Meera Kapoor
Dermatology Specialist
Fortis Hospital, Mumbai
Phone: +91-91234-56789
Email: meera.kapoor@fortishealth.com
Website: https://www.fortishealthcare.com/""",

        "urinary tract infection": """Dr. Suresh Patel
Urology Specialist
Apollo Hospitals, Ahmedabad
Phone: +91-98765-11223
Email: suresh.patel@apollohospitals.com
Website: https://www.apollohospitals.com/""",

        "psoriasis": """Dr. Meera Kapoor
Dermatology Specialist
Fortis Hospital, Mumbai
Phone: +91-91234-56789
Email: meera.kapoor@fortishealth.com
Website: https://www.fortishealthcare.com/""",

        "impetigo": """Dr. Meera Kapoor
Dermatology Specialist
Fortis Hospital, Mumbai
Phone: +91-91234-56789
Email: meera.kapoor@fortishealth.com
Website: https://www.fortishealthcare.com/""",
    }
    return details.get(specialty.lower(), "Doctor information not available.")



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
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image
from code.DiseaseModel import DiseaseModel
from code.helper import prepare_symptoms_array
from components.doctors_details import get_doctor_details, show_doctor_info
from components.generate_pdf import generate_pdf_report
from components.patient_details import patients_data
from components.generate_pdf import create_pdf
import joblib


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
        icons=['activity','droplet','heart-pulse','person','droplet-half','emoji-dizzy','emoji-frown','lungs','droplet','gender-female'], default_index=0)


# multiple disease prediction
if selected == 'Disease Prediction':
    # Create disease class and load ML model
    disease_model = DiseaseModel()
    disease_model.load_xgboost('model/xgboost_model.json')

    if "pdf_ready" not in st.session_state:
        st.session_state.pdf_ready = False
    if "pdf_bytes" not in st.session_state:
        st.session_state.pdf_bytes = None
    if "selected_patient_data" not in st.session_state:
        st.session_state.selected_patient_data = None
    if "manual_patient_details" not in st.session_state:
        st.session_state.manual_patient_details = {"name": "", "age": 0, "gender": ""}
    if "prediction" not in st.session_state:
        st.session_state.prediction = None
    if "prob" not in st.session_state:
        st.session_state.prob = None
    if "precautions" not in st.session_state:
        st.session_state.precautions = None


    # Title
    st.write('# Disease Prediction')
       # Patient selection dropdown
    st.write('Enter Symptoms or Select a Patient from the Records')
    method=["Manual Entry","Select from Patients"]
    selected_method = st.selectbox("Select Method", method)


    if selected_method == "Manual Entry":
        st.subheader("Patient Details for Report")
        name = st.text_input("Name", value=st.session_state.manual_patient_details["name"])
        age = st.number_input("Age", min_value=0, max_value=120, value=st.session_state.manual_patient_details["age"])
        gender = st.radio("Gender", options=["Male", "Female", "Other"], index=["Male", "Female", "Other"].index(st.session_state.manual_patient_details["gender"]) if st.session_state.manual_patient_details["gender"] else 0)
        st.session_state.manual_patient_details = {"name": name, "age": age, "gender": gender}

        symptoms = st.multiselect('What are your symptoms?', options=disease_model.all_symptoms)
        st.session_state.selected_patient_data = None # Clear patient data if manual entry is selected

        ready = name.strip() and age > 0 and gender and len(symptoms) > 0

        

        if st.session_state.get("pdf_ready", False) and st.session_state.get("pdf_bytes") is not None:
            st.download_button(
                label="Download PDF Report",
                data=st.session_state.pdf_bytes,
                file_name="medical_report.pdf",
                mime="application/octet-stream",
                key="manual_download"
            )


    else:
        patient_names = [p["name"] for p in patients_data]
        selected_patient_name = st.selectbox("Select a Patient", patient_names)
        patient = next(p for p in patients_data if p["name"] == selected_patient_name)
        st.session_state.selected_patient_data = patient # Store patient data in session state
        st.write(f"**Name:** {patient['name']}")
        st.write(f"**Age:** {patient['age']}")
        st.write(f"**Gender:** {patient['gender']}")
        st.write(f"**Symptoms:** {', '.join(patient['symptoms'])}")
        symptoms = patient['symptoms']
        st.session_state.manual_patient_details = {"name": "", "age": 0, "gender": ""} # Clear manual data if patient is selected


    X = prepare_symptoms_array(symptoms)


    # Trigger XGBoost model
    if st.button('Predict'):
        if not symptoms:
            st.warning('Please select at least one symptom to predict.')

        else:
        # Run the model with the python script

            prediction, prob = disease_model.predict(X)
            st.session_state.prediction = prediction # Store prediction in session state
            st.session_state.prob = prob # Store probability in session state
            st.write(f'## Disease: {prediction} with {prob*100:.2f}% probability')


            tab1, tab2,tab3,tab4= st.tabs(["Description", "Precautions","Doctor Recommendation","Report Download"])

            with tab1:
                st.write(disease_model.describe_predicted_disease())

            with tab2:
                precautions = disease_model.predicted_disease_precautions()
                st.session_state.precautions = precautions # Store precautions in session state
                for i in range(4):
                    st.write(f'{i+1}. {precautions[i]}')
            with tab3:
                show_doctor_info(prediction)

            with tab4:
                st.write("Download Report")

                # Removed manual entry download button from here as it's now in the manual entry section

                if selected_method == "Select from Patients" and st.session_state.selected_patient_data:
                    # Patient selection mode
                    patient_for_pdf = st.session_state.selected_patient_data
                    ready = patient_for_pdf["name"].strip() and patient_for_pdf["age"] > 0 and patient_for_pdf["gender"] and len(patient_for_pdf["symptoms"]) > 0
                    if ready:
                        st.download_button(
                            label="Download PDF Report",
                            data=create_pdf(
                                patient_for_pdf,
                                prediction, # Use local prediction here as it's within the Predict button scope
                                prob,       # Use local prob here as it's within the Predict button scope
                                disease_model.describe_predicted_disease(),
                                precautions, # Use local precautions here as it's within the Predict button scope
                                get_doctor_details(prediction) # Use local prediction here
                            ),
                            file_name="medical_report.pdf",
                            mime="application/octet-stream",
                            key="patient_download"
                        )
                else:
                    with st.form(key="manual_pdf_form"):
                        submitted = st.form_submit_button("Prepare PDF")
                        if submitted:
                            if not ready:
                                st.error("Please fill all fields and select at least one symptom.")
                            elif st.session_state.prediction is None or st.session_state.prob is None or st.session_state.precautions is None:
                                st.error("Please run the prediction first by clicking the 'Predict' button.")
                        else:
                            st.session_state.pdf_bytes = create_pdf(
                                {
                                    "name": name,
                                    "age": age,
                                    "gender": gender,
                                    "symptoms": symptoms
                                },
                            st.session_state.prediction,
                            st.session_state.prob,
                            disease_model.describe_predicted_disease(),
                            st.session_state.precautions,
                            get_doctor_details(st.session_state.prediction)
                        )
                        st.session_state.pdf_ready = True
                        




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
            doctor_info = get_doctor_details("diabetes")
            #pdf report
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
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_dig = 'we are really sorry to say but it seems like you have Heart Disease. '
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            show_doctor_info("heart")
             #pdf report
            doctor_info = get_doctor_details("heart")
            pdf_link = generate_pdf_report(name, "Diabetes", "Positive", doctor_info)
            st.markdown(pdf_link, unsafe_allow_html=True)

        else:
            diabetes_dig = 'Congratulation,You are not diabetic'
            image = Image.open('negative.jpg')
            st.image(image, caption='')
        st.success(name+'   ' + diabetes_dig)



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
    if st.button("Lung Cancer Test Result"):
        # Prepare input data for prediction
        input_data = pd.DataFrame({
            'GENDER': [1 if gender == 'Female' else 0],
            'AGE': [age],
            'SMOKING': [2 if smoking == 'YES' else 1],
            'YELLOW_FINGERS': [2 if yellow_fingers == 'YES' else 1],
            'ANXIETY': [2 if anxiety == 'YES' else 1],
            'PEER_PRESSURE': [2 if peer_pressure == 'YES' else 1],
            'CHRONIC DISEASE': [2 if chronic_disease == 'YES' else 1],
            'FATIGUE ': [2 if fatigue == 'YES' else 1],
            'ALLERGY ': [2 if allergy == 'YES' else 1],
            'WHEEZING': [2 if wheezing == 'YES' else 1],
            'ALCOHOL CONSUMING': [2 if alcohol_consuming == 'YES' else 1],
            'COUGHING': [2 if coughing == 'YES' else 1],
            'SHORTNESS OF BREATH': [2 if shortness_of_breath == 'YES' else 1],
            'SWALLOWING DIFFICULTY': [2 if swallowing_difficulty == 'YES' else 1],
            'CHEST PAIN': [2 if chest_pain == 'YES' else 1]
        })

        # Make prediction
        lung_cancer_prediction = lung_cancer_model.predict(input_data)

        # Display result
        if lung_cancer_prediction[0] == 2:
            cancer_result = 'we are really sorry to say but it seems like you have Lung Cancer.'
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            show_doctor_info("lung cancer")
            #pdf report
            doctor_info = get_doctor_details("lung_cancer")
            pdf_link = generate_pdf_report(name, "Lung Cancer", "Positive", doctor_info)
            st.markdown(pdf_link, unsafe_allow_html=True)
        else:
            cancer_result = "Congratulation, You don't have Lung Cancer."
            image = Image.open('negative.jpg')
            st.image(image, caption='')
        st.success(name + '  ' + cancer_result)


# Chronic Kidney Disease Prediction page
if selected == 'Chronic Kidney Prediction':
    st.title("Chronic Kidney Disease Prediction")
    image = Image.open('j.jpg')
    st.image(image, caption='Chronic Kidney Disease Prediction')

    # Load the pre-trained model
    # chronic_disease_model = joblib.load('chronic_model.sav')

    # Columns for input fields
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age')
    with col2:
        bp = st.number_input('Blood Pressure')
    with col3:
        sg = st.number_input('Specific Gravity')
    with col1:
        al = st.number_input('Albumin')
    with col2:
        su = st.number_input('Sugar')
    with col3:
        rbc = st.number_input('Red Blood Cells')
    with col1:
        pc = st.number_input('Pus Cell')
    with col2:
        pcc = st.number_input('Pus Cell Clumps')
    with col3:
        ba = st.number_input('Bacteria')
    with col1:
        bgr = st.number_input('Blood Glucose Random')
    with col2:
        bu = st.number_input('Blood Urea')
    with col3:
        sc = st.number_input('Serum Creatinine')
    with col1:
        sod = st.number_input('Sodium')
    with col2:
        pot = st.number_input('Potassium')
    with col3:
        hemo = st.number_input('Hemoglobin')
    with col1:
        pcv = st.number_input('Packed Cell Volume')
    with col2:
        wc = st.number_input('White Blood Cell Count')
    with col3:
        rc = st.number_input('Red Blood Cell Count')
    with col1:
        htn = st.number_input('Hypertension')
    with col2:
        dm = st.number_input('Diabetes Mellitus')
    with col3:
        cad = st.number_input('Coronary Artery Disease')
    with col1:
        appet = st.number_input('Appetite')
    with col2:
        pe = st.number_input('Pedal Edema')
    with col3:
        ane = st.number_input('Anemia')

    # Code for Prediction
    chronic_disease_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Chronic Kidney Disease Test Result'):
        chronic_disease_prediction = chronic_disease_model.predict([[age, bp, sg, al, su, rbc, pc, pcc, ba, bgr, bu, sc, sod, pot, hemo, pcv, wc, rc, htn, dm, cad, appet, pe, ane]])

        if chronic_disease_prediction[0] == 1:
            chronic_disease_diagnosis = 'we are really sorry to say but it seems like you have Chronic Kidney Disease.'
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            show_doctor_info("chronic kidney disease")
            #pdf report
            doctor_info = get_doctor_details("chronic kidney disease")
            pdf_link = generate_pdf_report(name, "Chronic Kidney Disease", "Positive", doctor_info)
            st.markdown(pdf_link, unsafe_allow_html=True)
        else:
            chronic_disease_diagnosis = 'Congratulation, You do not have Chronic Kidney Disease.'
            image = Image.open('negative.jpg')
            st.image(image, caption='')
        st.success(name + '  ' + chronic_disease_diagnosis)


# Breast Cancer Prediction page
if selected == 'Breast Cancer Prediction':
    st.title("Breast Cancer Prediction")
    image = Image.open('h.png')
    st.image(image, caption='Breast Cancer Prediction')

    # Load the pre-trained model
    # breast_cancer_model = joblib.load('breast_cancer.sav')

    # Columns for input fields
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        mean_radius = st.number_input('mean radius')
    with col2:
        mean_texture = st.number_input('mean texture')
    with col3:
        mean_perimeter = st.number_input('mean perimeter')
    with col1:
        mean_area = st.number_input('mean area')
    with col2:
        mean_smoothness = st.number_input('mean smoothness')
    with col3:
        mean_compactness = st.number_input('mean compactness')
    with col1:
        mean_concavity = st.number_input('mean concavity')
    with col2:
        mean_concave_points = st.number_input('mean concave points')
    with col3:
        mean_symmetry = st.number_input('mean symmetry')
    with col1:
        mean_fractal_dimension = st.number_input('mean fractal dimension')
    with col2:
        radius_error = st.number_input('radius error')
    with col3:
        texture_error = st.number_input('texture error')
    with col1:
        perimeter_error = st.number_input('perimeter error')
    with col2:
        area_error = st.number_input('area error')
    with col3:
        smoothness_error = st.number_input('smoothness error')
    with col1:
        compactness_error = st.number_input('compactness error')
    with col2:
        concavity_error = st.number_input('concavity error')
    with col3:
        concave_points_error = st.number_input('concave points error')
    with col1:
        symmetry_error = st.number_input('symmetry error')
    with col2:
        fractal_dimension_error = st.number_input('fractal dimension error')
    with col3:
        worst_radius = st.number_input('worst radius')
    with col1:
        worst_texture = st.number_input('worst texture')
    with col2:
        worst_perimeter = st.number_input('worst perimeter')
    with col3:
        worst_area = st.number_input('worst area')
    with col1:
        worst_smoothness = st.number_input('worst smoothness')
    with col2:
        worst_compactness = st.number_input('worst compactness')
    with col3:
        worst_concavity = st.number_input('worst concavity')
    with col1:
        worst_concave_points = st.number_input('worst concave points')
    with col2:
        worst_symmetry = st.number_input('worst symmetry')
    with col3:
        worst_fractal_dimension = st.number_input('worst fractal dimension')

    # Code for Prediction
    breast_cancer_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = breast_cancer_model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness, mean_compactness, mean_concavity, mean_concave_points, mean_symmetry, mean_fractal_dimension, radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, worst_radius, worst_texture, worst_perimeter, worst_area, worst_smoothness, worst_compactness, worst_concavity, worst_concave_points, worst_symmetry, worst_fractal_dimension]])

        if breast_cancer_prediction[0] == 0:
            breast_cancer_diagnosis = 'we are really sorry to say but it seems like you have Breast Cancer.'
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            show_doctor_info("breast_cancer")
            #pdf report
            doctor_info = get_doctor_details("breast cancer")
            pdf_link = generate_pdf_report(name, "Breast Cancer", "Positive", doctor_info)
            st.markdown(pdf_link, unsafe_allow_html=True)
        else:
            breast_cancer_diagnosis = 'Congratulation, You do not have Breast Cancer.'
            image = Image.open('negative.jpg')
            st.image(image, caption='')
        st.success(name + '  ' + breast_cancer_diagnosis)

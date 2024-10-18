import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('web_app/prediction_model.pkl')

# Define the function for prediction
def predict_performance(features):
    # Convert input features to a DataFrame (1 row with all features)
    input_data = pd.DataFrame([features], columns=[
        'SS3_avg_attendance', 'SS2_avg_attendance', 'SS1_avg_attendance', 
        'SS1_First_Term', 'SS1_Third_Term', 'SS1_Second_Term', 
        'SS2_Second_Term', 'SS2_First_Term', 'SS2_Third_Term', 
        'SS3_First_Term', 'Avg_Daily_Study_Hours', 'Education_Level', 
        'Marriage_Status', 'Socioeconomic_Status', 
        'Private_Home_Tutor', 'Access_to_Technology'
    ])
    
    # Make the prediction
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit interface for Prediction
st.title('Student Performance Grade Prediction')

# Education level mapping
education_mapping = {
    'Primary School': 0,
    'Secondary School': 1,
    'NCE': 2,
    'HND': 3,
    'BSc': 4,
    'MSc': 5,
    'PhD': 6
}

# Marriage Status Mapping
marriage_mapping = {
    'Married': 1,
    'Single': 2,
    'Divorced': 0,
    'Separated': 3
}

# Private Home Tutor Mapping
private_tutor_mapping = {
    'Yes': 1,
    'No': 0
}

# Socioeconomic Status Mapping
socioeconomic_mapping = {
    'High': 2,
    'Medium': 1,
    'Low': 0
}

# Access to Technology Mapping
access_technology_mapping = {
    'Yes': 1,
    'No': 0
}

# Layout using columns
st.header("Attendance Scores")
col1, col2 = st.columns(2)

with col1:
    SS1_avg_attendance = st.number_input('SS1 Average Attendance', min_value=0.0, max_value=100.0, step=0.1)
    SS2_avg_attendance = st.number_input('SS2 Average Attendance', min_value=0.0, max_value=100.0, step=0.1)
    
with col2:
    SS3_avg_attendance = st.number_input('SS3 Average Attendance', min_value=0.0, max_value=100.0, step=0.1)

st.header("Past Performance")
col3, col4 = st.columns(2)

with col3:
    SS1_First_Term = st.number_input('SS1 First Term Score', min_value=0.0, max_value=100.0, step=0.1)
    SS1_Second_Term = st.number_input('SS1 Second Term Score', min_value=0.0, max_value=100.0, step=0.1)
    SS1_Third_Term = st.number_input('SS1 Third Term Score', min_value=0.0, max_value=100.0, step=0.1)
    SS3_First_Term = st.number_input('SS3 First Term Score', min_value=0.0, max_value=100.0, step=0.1)

with col4:
    SS2_First_Term = st.number_input('SS2 First Term Score', min_value=0.0, max_value=100.0, step=0.1)
    SS2_Second_Term = st.number_input('SS2 Second Term Score', min_value=0.0, max_value=100.0, step=0.1)
    SS2_Third_Term = st.number_input('SS2 Third Term Score', min_value=0.0, max_value=100.0, step=0.1)

st.header("Other Factors")
col5, col6 = st.columns(2)

with col5:
    Avg_Daily_Study_Hours = st.number_input('Average Daily Study Hours', min_value=0.0, max_value=24.0, step=0.1)
    selected_education = st.selectbox('Parental Education Level', list(education_mapping.keys()))
    selected_marriage_status = st.selectbox('Parental Marriage Status', list(marriage_mapping.keys()))

with col6:
    selected_socioeconomic_status = st.selectbox('Socioeconomic Status', list(socioeconomic_mapping.keys()))
    selected_private_tutor = st.selectbox('Private Home Tutor', list(private_tutor_mapping.keys()))
    selected_access_to_technology = st.selectbox('Access to Technology', list(access_technology_mapping.keys()))

# Mapping selected options to numerical values
Education_Level = education_mapping[selected_education]
Marriage_Status = marriage_mapping[selected_marriage_status]
Private_Home_Tutor = private_tutor_mapping[selected_private_tutor]
Socioeconomic_Status = socioeconomic_mapping[selected_socioeconomic_status]
Access_to_Technology = access_technology_mapping[selected_access_to_technology]

# Grade mapping
grade_mapping = {
    0: 'F9',
    1: 'E8',
    2: 'D7',
    3: 'C6',
    4: 'C5',
    5: 'C4',
    6: 'B3',
    7: 'B2',
    8: 'A1'
}

# Function to map prediction to grade and pass/fail status
def get_grade_and_status(prediction):
    grade = grade_mapping[prediction]
    status = "PASS" if prediction > 0 else "FAIL"
    return grade, status

# When the user clicks the "Predict" button
if st.button('Predict Performance Grade'):
    features = [
        SS3_avg_attendance, SS2_avg_attendance, SS1_avg_attendance,
        SS1_First_Term, SS1_Second_Term, SS1_Third_Term, 
        SS2_Second_Term, SS2_First_Term, SS2_Third_Term, 
        SS3_First_Term, Avg_Daily_Study_Hours, Education_Level, 
        Marriage_Status, Socioeconomic_Status, Private_Home_Tutor, 
        Access_to_Technology
    ]
    
    # Get the prediction from the model
    prediction = predict_performance(features)

    # Get the grade and status (Pass/Fail)
    grade, status = get_grade_and_status(prediction)
    
    # Display the result
    st.success(f'The predicted performance grade is: {grade} ({status})')

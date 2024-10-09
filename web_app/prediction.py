import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('https://github.com/aayomide/kaizen-hack/blob/main/web_app/prediction_model.pkl')

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

# Collecting user input features for prediction
SS3_avg_attendance = st.number_input('SS3 Average Attendance', min_value=0.0, max_value=100.0, step=0.1)
SS2_avg_attendance = st.number_input('SS2 Average Attendance', min_value=0.0, max_value=100.0, step=0.1)
SS1_avg_attendance = st.number_input('SS1 Average Attendance', min_value=0.0, max_value=100.0, step=0.1)
SS1_First_Term = st.number_input('SS1 First Term Score', min_value=0.0, max_value=100.0, step=0.1)
SS1_Second_Term = st.number_input('SS1 Second Term Score', min_value=0.0, max_value=100.0, step=0.1)
SS1_Third_Term = st.number_input('SS1 Third Term Score', min_value=0.0, max_value=100.0, step=0.1)
SS2_First_Term = st.number_input('SS2 First Term Score', min_value=0.0, max_value=100.0, step=0.1)
SS2_Second_Term = st.number_input('SS2 Second Term Score', min_value=0.0, max_value=100.0, step=0.1)
SS2_Third_Term = st.number_input('SS2 Third Term Score', min_value=0.0, max_value=100.0, step=0.1)
SS3_First_Term = st.number_input('SS3 First Term Score', min_value=0.0, max_value=100.0, step=0.1)
Avg_Daily_Study_Hours = st.number_input('Average Daily Study Hours', min_value=0.0, max_value=24.0, step=0.1)
Education_Level = st.selectbox('Education Level', [1, 2, 3])  # 1 = Primary, 2 = Secondary, 3 = Tertiary
Marriage_Status = st.selectbox('Marriage Status', [0, 1])  # 0 = Single, 1 = Married
Socioeconomic_Status = st.selectbox('Socioeconomic Status', [1, 2, 3])  # 1 = Low, 2 = Middle, 3 = High
Private_Home_Tutor = st.selectbox('Private Home Tutor', [0, 1])  # 0 = No, 1 = Yes
Access_to_Technology = st.selectbox('Access to Technology', [0, 1])  # 0 = No, 1 = Yes

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

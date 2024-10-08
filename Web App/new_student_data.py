import streamlit as st
import pandas as pd
from datetime import datetime

# Data collection interface
st.title('New Student DataForm')

# Collect basic student data
first_name = st.text_input("Student First Name")
last_name = st.text_input("Student Last Name")
age = st.number_input("Age", min_value=5, max_value=25, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
date_of_birth = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1), max_value=datetime.today())
school = st.text_input("Former School Name")
address = st.text_input("Home address")
religion = st.selectbox("Religion", ["Muslim", "Christian", "Other"])
state_of_origin = st.selectbox("State of Origin", ["Abia", "Adamawa", "Akwa Ibom", "Anambra", "Bauchi", "Bayelsa", "Benue", "Borno", "Cross River", "Delta", "Ebonyi", "Edo", "Ekiti", "Enugu", "Gombe", "Imo", "Jigawa", "Kaduna", "Kano", "Katsina", "Kebbi", "Kogi", "Kwara", "Lagos", "Nasarawa", "Niger", "Ogun", "Ondo", "Osun", "Oyo", "Plateau", "Rivers", "Sokoto", "Taraba", "Yobe", "Zamfara", "FCT (Abuja)"]),
nationality = st.text_input("Nationality")
parent_name = st.text_input("Parent Name")
current_grade = st.selectbox("Current Class", ["SS1", "SS2", "SS3"])


# When the user clicks the "Save Data" button
if st.button("Save Data"):
    student_data = {
        "first": first_name,
        "last": last_name,
        "Age": age,
        "Gender": gender,
        "Date of Birth": date_of_birth,
        "School": school,
        "Address": address,
        "Religion": religion,
        "State of Origin": state_of_origin,
        "Nationality": nationality,
        "Parent Name": parent_name,
        "Current Grade": current_grade,
    }
    
    # Convert to DataFrame
    df = pd.DataFrame([student_data])
    
    # Save to CSV (append mode, no header)
    df.to_csv("data/student_data.csv", mode='a', header=False, index=False)
    
    st.success(f"Data for {first_name, last_name} has been saved.")

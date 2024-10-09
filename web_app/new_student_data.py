import streamlit as st
import pandas as pd
from datetime import datetime
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get BigQuery project and table IDs from environment variables
# project_id = os.getenv("BIGQUERY_PROJECT_ID")
# table_id = os.getenv("BQ_STUDENTS_TABLE_ID")

project_id = 'datafest-kaizen-437821'
exam_scores_table_id = 'datafest-kaizen-437821.kaizen_school_dataset.dim_students_raw'

# Initialize BigQuery client
client = bigquery.Client(project=project_id)

# Streamlit form: Data collection interface
st.title("Student Data Form")

with st.form("student_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    age = st.number_input("Age", min_value=15, max_value=18, step=1)
    department = st.selectbox("Department", ['Science & Mathematics', 'Technology', 'Humanities', 'Commercial'])
    subjects = st.multiselect("Subjects", [
        'English Studies', 'Mathematics', 'Civic Education', 'Data Processing', 'Garment Making', 
        'Mechanics', 'Bookkeeping', 'Marketing', 'Biology', 'Chemistry', 'Physics', 
        'Further Mathematics', 'Agricultural Science', 'Computer Science', 'Economics',
        'CRS/IRS', 'History', 'Geography', 'Government', 'Literature-in-English', 'French',
        'Technical Drawing', 'Food & Nutrition', 'Accounting', 'Commerce'
    ])
    access_to_tech = st.selectbox("Access to Technology", ['Yes', 'No'])
    extracurricular = st.selectbox("Extracurricular Activities", ['Yes', 'No'])
    home_tutor = st.selectbox("Private Home Tutor", ['Yes', 'No'])
    avg_study_hours = st.slider("Average Daily Study Hours", min_value=1.0, max_value=5.0, step=0.1)
    
    submitted = st.form_submit_button("Submit")

    # Error handling for missing fields
    if submitted:
        if not first_name or not last_name or not subjects:
            st.error("Please make sure all required fields are filled out, including Subjects.")
        else:
            # Prepare data for BigQuery
            rows_to_insert = [{
                "First_Name": first_name,
                "Last_Name": last_name,
                "Age": age,
                "Department": department,
                "Subjects": subjects,  # Assuming subjects are passed as a list/array
                "Access_to_Technology": access_to_tech,
                "Extracurricular_Activities": extracurricular,
                "Private_Home_Tutor": home_tutor,
                "Avg_Daily_Study_Hours": avg_study_hours
            }]
            
            try:
                errors = client.insert_rows_json(table_id, rows_to_insert)  # Returns errors list
                
                if not errors:
                    st.success(f"Student data successfully uploaded.")
                else:
                    st.error(f"Failed to insert data: {errors}")
            
            except GoogleAPIError as e:
                st.error(f"An error occurred while communicating with database: {e.message}")
            
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")

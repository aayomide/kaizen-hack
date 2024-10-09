import streamlit as st
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get BigQuery project and table IDs from environment variables
project_id = os.getenv("BIGQUERY_PROJECT_ID")
exam_scores_table_id = os.getenv("BQ_PERFORMANCE_TABLE_ID")

# Error handling for environment variables
if not project_id or not exam_scores_table_id:
    st.error("BigQuery environment variables (BIGQUERY_PROJECT_ID or BIGQUERY_EXAM_SCORES_TABLE_ID) are not set. Please check your environment setup.")
else:
    try:
        # Initialize BigQuery client
        client = bigquery.Client(project=project_id)
    except Exception as e:
        st.error(f"Failed to initialize BigQuery client: {str(e)}")

    # Streamlit form: Data collection interface for Student Exam Scores
    st.title("Student Exam Scores Form")

    with st.form("exam_scores_form"):
        student_id = st.text_input("Student ID", placeholder="e.g., STD001")
        subject_name = st.selectbox("Subject Name", [
            'English Studies', 'Mathematics', 'Civic Education', 'Data Processing', 'Garment Making', 
            'Mechanics', 'Bookkeeping', 'Marketing', 'Biology', 'Chemistry', 'Physics', 
            'Further Mathematics', 'Agricultural Science', 'Computer Science', 'Economics',
            'CRS/IRS', 'History', 'Geography', 'Government', 'Literature-in-English', 'French',
            'Technical Drawing', 'Food & Nutrition', 'Accounting', 'Commerce'
        ])
        year = st.selectbox("Year", ['SS1', 'SS2', 'SS3'])
        term = st.selectbox("Term", ['First Term', 'Second Term', 'Third Term'])
        score = st.number_input("Score", min_value=0, max_value=100, step=1)
        grade = st.selectbox("Grade", ['A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9'])

        submitted = st.form_submit_button("Submit")

        # Error handling for missing fields
        if submitted:
            if not student_id:
                st.error("Please make sure Student ID is filled out.")
            else:
                # Prepare data for BigQuery
                rows_to_insert = [{
                    "Student_ID": student_id,
                    "Subject_Name": subject_name,
                    "Year": year,
                    "Term": term,
                    "Score": score,
                    "Grade": grade
                }]

                try:
                    # Insert data into BigQuery
                    errors = client.insert_rows_json(exam_scores_table_id, rows_to_insert)  # Returns errors list

                    if not errors:
                        st.success(f"Exam scores successfully uploaded.")
                    else:
                        st.error(f"Failed to insert data: {errors}")

                except GoogleAPIError as e:
                    st.error(f"An error occurred while communicating with BigQuery: {e.message}")
                
                except Exception as e:
                    st.error(f"An unexpected error occurred: {str(e)}")

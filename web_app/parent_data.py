import streamlit as st
import pandas as pd
from google.cloud import bigquery
from google.api_core.exceptions import GoogleAPIError
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get BigQuery project and table IDs from environment variables
# project_id = os.getenv("BIGQUERY_PROJECT_ID")
# table_id = os.getenv("BQ_PARENTS_TABLE_ID")
project_id = 'datafest-kaizen-437821'
table_id = 'datafest-kaizen-437821.kaizen_school_dataset.dim_parents_raw'

# Initialize BigQuery client
client = bigquery.Client(project=project_id)

# Streamlit form: Data collection interface for Parents
st.title("Parents Data Form")


# Create a form to input parent data
# Create a form to input parent data
with st.form("parent_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    education_level = st.selectbox("Education Level", [
        'Primary School', 'Secondary School', 'NCE', 'HND', 'BSc', 'MSc', 'PhD'
    ])
    occupation = st.selectbox("Occupation", [
        'Teacher', 'Engineer', 'Trader', 'Civil Servant', 'Doctor', 'Farmer'
    ])
    
    # Socioeconomic Status based on occupation
    if occupation in ['Engineer', 'Doctor']:
        socioeconomic_status = 'High'
    elif occupation in ['Civil Servant', 'Teacher']:
        socioeconomic_status = 'Middle'
    else:
        socioeconomic_status = 'Low'
        
    marriage_status = st.selectbox("Marriage Status", ['Married', 'Divorced', 'Single'])
    
    # Submit form button
    submitted = st.form_submit_button("Submit")

    # Error handling for missing fields
    if submitted:
        if not first_name or not last_name:
            st.error("Please make sure First Name and Last Name are filled out.")
        else:
            # Prepare data for BigQuery
            rows_to_insert = [{
                "First_Name": first_name,
                "Last_Name": last_name,
                "Education_Level": education_level,
                "Occupation": occupation,
                "Socioeconomic_Status": socioeconomic_status,
                "Marriage_Status": marriage_status
            }]

            try:
                # Insert data into BigQuery
                errors = client.insert_rows_json(table_id, rows_to_insert)  # Returns errors list

                if not errors:
                    st.success(f"Parent data successfully uploaded.")
                else:
                    st.error(f"Failed to insert data: {errors}")

            except GoogleAPIError as e:
                st.error(f"An error occurred while communicating with BigQuery: {e.message}")
            
            except Exception as e:
                st.error(f"An unexpected error occurred: {str(e)}")
        


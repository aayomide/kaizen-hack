from google.cloud import bigquery
import pandas as pd
import pyarrow
print(pyarrow.__version__)  

# Set up your BigQuery client
client = bigquery.Client()

# Define the dataset ID
dataset_id = "datafest-kaizen-437821.kaizen_school_dataset"

# Load CSVs into Pandas DataFrames
students_df = pd.read_csv('C:/Users/pc/Documents/projects/datafesthack/data/students_data_final.csv')
subjects_df = pd.read_csv('C:/Users/pc/Documents/projects/datafesthack/data/subjects_final.csv')
performance_df = pd.read_csv('C:/Users/pc/Documents/projects/datafesthack/data/student_performance_final.csv')
attendance_df = pd.read_csv('C:/Users/pc/Documents/projects/datafesthack/data/attendance_final.csv')
parents_df = pd.read_csv('C:/Users/pc/Documents/projects/datafesthack/data/parents_final.csv')
teachers_df = pd.read_csv('C:/Users/pc/Documents/projects/datafesthack/data/teachers_final.csv')

# Function to load a DataFrame into BigQuery
def load_table_to_bq(df, table_name):
    table_id = f"{dataset_id}.{table_name}"
    job = client.load_table_from_dataframe(df, table_id)
    job.result()  # Wait for the job to complete
    print(f"Loaded {df.shape[0]} rows into {table_id}")

# Load each table
load_table_to_bq(students_df, 'dim_students')
load_table_to_bq(subjects_df, 'dim_subjects')
load_table_to_bq(performance_df, 'fact_student_performance')
load_table_to_bq(attendance_df, 'fact_attendance')
load_table_to_bq(parents_df, 'dim_parents')
load_table_to_bq(teachers_df, 'dim_teachers')

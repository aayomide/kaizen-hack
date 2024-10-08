import streamlit as st
import pandas as pd
from datetime import datetime

# Data collection interface
st.title('Data Update')

# Collect basic student data
student_name = st.text_input("Student Name (Surname first)")
attendance = st.number_input("Average Attendance (in percentage)", min_value=0, max_value=100, step=1)
extracurricular = st.text_input("Extracurricular Activities")
term = st.selectbox("Term", ["First", "Second", "Third"])
current_class = st.selectbox("Current Class", ["SS1", "SS2", "SS3"])

# List of subjects
subjects = [
    "English Studies", "Mathematics", "Civic Education", "Data Processing", 
    "Garment Making", "Mechanics", "Bookkeeping", "Marketing", "Computer Science", 
    "Literature-in-English", "Physics", "Chemistry", "Food & Nutrition", 
    "Economics", "Technical Drawing", "Further Mathematics", "Government", 
    "Commerce", "Biology", "Accounting", "Geography", "French", "History", 
    "Agricultural Science", "CRS/IRS", "None"
]

# Collect scores for 8 subjects
subject_scores = {}
st.header("Enter Scores for 9 Subjects")

for i in range(1, 10):
    subject = st.selectbox(f"Subject {i}", subjects, key=f"subject_{i}")
    score = st.number_input(f"Score for {subject}", min_value=0, max_value=100, step=1, key=f"score_{i}")
    subject_scores[subject] = score

# When the user clicks the "Save Data" button
if st.button("Save Data"):
    curr_student_data = {
        "Name": student_name,
        "Attendance": attendance,
        "Extracurricular": extracurricular,
        "Term": term,
        "Current_Class": current_class
    }
    
    # Add subjects and scores to student data
    for subject, score in subject_scores.items():
        curr_student_data[subject] = score
    
    # Convert to DataFrame
    df = pd.DataFrame([curr_student_data])
    
    # Save to CSV (append mode, no header)
    df.to_csv("data/curr_student_data.csv", mode='a', header=False, index=False)
    
    st.success(f"Data for {student_name} has been saved.")

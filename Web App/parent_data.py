import streamlit as st
import pandas as pd

# Data collection interface
st.title('Parent DataForm')

# Collect basic student data
parent_name = st.text_input("Parent/Guardian Name")
occupation = st.text_input("Occupation")
relationship = st.text_input("Relationship with Student")
Religion = st.selectbox("Parent/Guardian Religion", ["Muslim", "Christian", "Other"])
education_level = st.selectbox("Highest Educational Level", ["Bsc", "Phd", "secondary school", "primary school", "NCE", "HND", "MSc"])
Marriage_Status = st.selectbox("Marriage Status", ["Married", "Single", "Divorced", "Separated"])
address = st.text_input("Home address")
phone = st.text_input("Phone Number")

# When the user clicks the "Save Data" button
if st.button("Save Data"):
    parent_data = {
        "Name": parent_name,
        "Ocuupation": occupation,
        "relationship": relationship,
        "Educational_level": education_level,
        "Marriage_Status": Marriage_Status,
        "Religion": Religion,
        "Address": address,
        "phone": phone
    }
    
    # Convert to DataFrame
    df = pd.DataFrame([parent_data])
    
    # Save to CSV (append mode, no header)
    df.to_csv("data/parent_data.csv", mode='a', header=False, index=False)
    
    st.success(f"Data for {parent_name} has been saved.")

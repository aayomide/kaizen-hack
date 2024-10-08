import streamlit as st


# --- PAGE SETUP ---
project_1_page = st.Page(
    "prediction.py",
    title="Prediction",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "new_student_data.py",
    title="Student Data Collection",
    icon= ":material/edit_document:",
)

project_3_page = st.Page(
    "parent_data.py",
    title="Parent Data Collection",
     icon=":material/family_restroom:",
)

project_4_page = st.Page(
    "current_student_data_update.py",
    title="Updating Data For Students",
     icon=":material/edit:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Menu": [project_1_page, project_2_page, project_3_page, project_4_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("Made by TEAM KAIZEN")


# --- RUN NAVIGATION ---
pg.run()
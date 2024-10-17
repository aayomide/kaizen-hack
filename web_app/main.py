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

# Add button with a link to Power BI
st.sidebar.markdown("""
    <div style="margin-bottom: 20px;">
        <a href="https://app.powerbi.com/view?r=eyJrIjoiMTU0ZGMxOGEtMTViOC00OTE0LTg5NjEtNDU5YzAwOTllYzQ5IiwidCI6IjI1Y2UwMjYxLWJiZDYtNDljZC1hMWUyLTU0MjYwODg2ZDE1OSJ9" target="_blank">
            <button style="padding: 10px 20px; background-color: #083c5d; color: white; border: none; border-radius: 5px; width: 100%;">
                Analytics
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("Made by TEAM KAIZEN")


# --- RUN NAVIGATION ---
pg.run()

# TEAM KAIZEN: DataFestAfrica Hackathon 2024 Submission

## Project: Improving Academic Outcomes for Secondary Education

### 🛠️ Project Background
We were contracted as consultants by a school in Lagos Nigeria to build a data-driven solution that can proactively enhance student performance in upcoming exams. Our project provides an end-to-end data solution, from data collection to model development, aimed at helping students score above average in their final exams.

# <a href="https://kaizen-school-app.streamlit.app/" style="color: red;" target="_blank>LIVE PROJECT</a> 

## 📊 Key Components

### 1. Data Aggregation & Analysis
- **Data**: Contains CSV files with student, parent, and performance data.
- **Images**: Contains visualizations such as correlation matrices and feature distributions.
- **Notebooks**:
  - `Data_Analysis.ipynb`: Analyzes student performance data.
  - `data aggregator.ipynb`: Aggregates data from different sources.

### 2. Data Folder
- Stores raw and cleaned data used in the analysis and model building.

### 3. Web App
- `Prediction_Model.ipynb`: Jupyter notebook used to train and evaluate the predictive model.
- `main.py`: Backend logic for the web application.
- `prediction_model.pkl`: Serialized machine learning model.
- `new_student_data.py`, `parent_data.py`, `prediction.py`: Scripts for handling new data input and predictions.
- `requirements.txt`: Python dependencies for running the application.

### 4. Scripts
- `data_generation_script.py`: Generates synthetic student data to simulate a real-world scenario.
- `ingest_to_bq.py`: Script for ingesting data into BigQuery for advanced analysis.
- `sample_script.py`: Example script for data manipulation and analysis.

### 5. TEAM KAIZEN Pdf
- Contains complete project process for data collection, analysis, and model development to predict student performance in final exams.
- Includes information on tools used like Python, Power BI, and Streamlit
- Outlines process taken to build a data pipeline, predictive model, and web application for real-time insights and recommendations for educational stakeholders.
- Provides recommendations to enhance student success.

---

## 👣 Process

### 1. Data Collection
We collected and simulated various data points including:
- Student academic history (grades, attendance, exam scores)
- Parent information (education level
- Teacher and subject data

### 2. Data Structuring
We designed a robust schema for data collection, storage, and analysis. The data is stored in CSV format and used for model training and evaluation.

### 3. Data Analysis
Using Python's data analysis libraries (Pandas, Matplotlib, Seaborn), we explored key trends and factors affecting student performance. Insights gained from this analysis were used to improve our predictive model.

### 4. Model Development
We developed an optimized machine learning model that predicts whether a student is likely to pass or fail their upcoming exams. The model considers various factors such as:
- Attendance
- Academic history
- Parental involvement

### 5. Recommendations
Based on the analysis, we provided recommendations to the school's stakeholders to improve student performance. These include:
- Increasing parental involvement in academics
- Regular attendance monitoring
- Early intervention for struggling students

---
## App Demo

![Project Demo](kaizen_demo.gif)

---

## 💻 How to Run the Project
### Install Dependencies: Run the following command to install the necessary packages:
```bash
pip install -r requirements.txt
```

### Run the Web Application: Navigate to the web_app directory and run the app:
```bash
streamlit run main.py
```
Jupyter Notebooks: Open and run the Jupyter notebooks for data analysis and model training.

---

## 📈 Deliverables
### Data Collection Plan: Includes attendance, performance, parent, and teacher data.
### Data Warehouse Schema: We designed a structured database for storing and analyzing school-related activities.
### Predictive Models: Machine learning model that predicts student outcomes.
### Recommendations: Actionable insights for improving student performance.

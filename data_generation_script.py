import random
import pandas as pd


# List of Nigerian first and last names
first_names = [
    "Chinedu", "Amina", "Tunde", "Ifeanyi", "Funke",
    "Emeka", "Zainab", "Bayo", "Kemi", "Ibrahim",
    "Uchenna", "Sola", "Ngozi", "Ayoola", "Femi",
    "Adaobi", "Chijioke", "Halima", "Kelechi", "Ijeoma",
    "Segun", "Nneka", "Musa", "Oluchi", "Aishat"
]

# List of 25 random Nigerian last names
last_names = [
    "Okonkwo", "Balogun", "Eze", "Adeyemi", "Nwosu",
    "Ibrahim", "Adebayo", "Obi", "Okafor", "Abubakar",
    "Ogundipe", "Olatunji", "Onwudiwe", "Mohammed", "Ojo",
    "Yusuf", "Umeh", "Alabi", "Ibe", "Ayodele",
    "Ogbonna", "Danjuma", "Okeke", "Adedoyin", "Nwachukwu"
]


# Departments
departments = ['Science & Mathematics', 'Technology', 'Humanities', 'Commercial']

# Compulsory core subjects
core_subjects = ['English Studies', 'Mathematics', 'Civic Education']
trade_subjects = ['Data Processing', 'Garment Making', 'Mechanics', 'Bookkeeping', 'Marketing']

# Elective subjects based on department
science_electives = ['Biology', 'Chemistry', 'Physics', 'Further Mathematics', 'Agricultural Science', 'Computer Science', 'Economics']
humanities_electives = ['CRS/IRS', 'History', 'Geography', 'Government', 'Literature-in-English', 'French', 'Economics']
technology_electives = ['Technical Drawing', 'Food & Nutrition', 'Chemistry', 'Physics', 'Further Mathematics', 'Agricultural Science', 'Computer Science', 'Economics', 'Geography']
commercial_electives = ['Accounting', 'Commerce', 'Economics', 'Geography', 'Agricultural Science', 'Government', 'Further Mathematics']

# Combine all subjects
all_subjects = list(set(core_subjects + trade_subjects + science_electives + humanities_electives + technology_electives + commercial_electives))

# Teacher qualifications
teacher_qualifications = ['Bsc', 'Msc', 'B. Engr', 'B. Ed', 'NCE Holder', 'SSCE Certificate']

# Terms
terms = ['First Term', 'Second Term', 'Third Term']

n_students = 160  # Number of students
n_teachers = len(all_subjects)  # Number of teachers 

# Function to generate random student data
def generate_students(num_students):
    students = []
    for i in range(num_students):
        student_id = f"STD{i+1:03d}"
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        age = random.randint(15, 18)
        department = random.choice(departments)
        parent_id = f"PR{random.randint(1, num_students):03d}"
        access_to_technology = random.choice(['Yes', 'No'])
        extracurricular_activities = random.choice(['Yes', 'No'])
        private_home_tutor = random.choice(['Yes', 'No'])
        avg_daily_study_hours = round(random.uniform(1.0, 5.0), 1)

        # Select elective subjects based on the student's department
        if department == 'Science & Mathematics':
            electives = random.sample(science_electives, random.randint(4, 5))
        elif department == 'Technology':
            electives = random.sample(technology_electives, random.randint(4, 5))
        elif department == 'Humanities':
            electives = random.sample(humanities_electives, random.randint(4, 5))
        else:  # Commercial
            electives = random.sample(commercial_electives, random.randint(4, 5))

        # Core subjects + electives
        subjects = core_subjects + electives + [random.choice(trade_subjects)]

        students.append({
            'ID': student_id,
            'First_Name': first_name,
            'Last_Name': last_name,
            'Age': age,
            'Department': department,
            'Subjects': subjects,
            'Parent_ID': parent_id,  # Foreign key to parent data
            'Access_to_Technology': access_to_technology,
            'Extracurricular_Activities': extracurricular_activities,
            'Private_Home_Tutor': private_home_tutor,
            'Avg_Daily_Study_Hours': avg_daily_study_hours
        })
    return students

# Generate subjects table
def generate_subjects():
    subject_id = 1
    subjects = []
    
    # Core subjects
    for subject in core_subjects + trade_subjects:
        subjects.append({
            'ID': f"SUB{subject_id:03d}",
            'Subject_Name': subject,
            'Subject_Type': 'Core' if subject in core_subjects else 'Trade',
            'Class_Level': 'SSS3'
        })
        subject_id += 1
    
    # Electives (based on all departments)
    all_electives = list(set(science_electives + humanities_electives + technology_electives + commercial_electives))
    for subject in all_electives:
        subjects.append({
            'ID': f"SUB{subject_id:03d}",
            'Subject_Name': subject,
            'Subject_Type': 'Elective',
            'Class_Level': 'SSS3'
        })
        subject_id += 1
    
    return subjects

# Function to generate performance data across terms and years (SS1, SS2, SS3)
def generate_performance(students):
    performance_data = []
    grades = ['A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9']
    
    performance_id = 1
    for student in students:
        student_id = student['ID']
        for subject in student['Subjects']:
            # Simulate performance across years (SS1, SS2, SS3) and terms (First, Second, Third)
            for year in ['SS1', 'SS2', 'SS3']:
                for term in terms:
                    score = random.randint(12, 95)  # Random score between 12 and 95
                    if score >= 75:
                        grade = 'A1'
                    elif score >= 70:
                        grade = 'B2'
                    elif score >= 65:
                        grade = 'B3'
                    elif score >= 60:
                        grade = 'C4'
                    elif score >= 55:
                        grade = 'C5'
                    elif score >= 50:
                        grade = 'C6'
                    elif score >= 45:
                        grade = 'D7'
                    elif score >= 40:
                        grade = 'E8'
                    else:
                        grade = 'F9'
                    performance_data.append({
                        'ID': f"PERF{performance_id:03d}",
                        'Student_ID': student_id,
                        'Subject_Name': subject,
                        'Year': year,
                        'Term': term,
                        'Score': score,
                        'Grade': grade
                    })
                    performance_id += 1
    
    return performance_data

# Generate attendance data
def generate_attendance(students):
    attendance_data = []
    attendance_id = 1
    
    for student in students:
        student_id = student['ID']
        for year in ['SS1', 'SS2', 'SS3']:
            for term in terms:
                attendance_rate = round(random.uniform(75.0, 100.0), 2)  # Attendance rate as percentage
                attendance_data.append({
                    'ID': f"ATT{attendance_id:03d}",
                    'Student_ID': student_id,
                    'Year': year,
                    'Term': term,
                    'Attendance_Rate': attendance_rate
                })
                attendance_id += 1
    
    return attendance_data

# Generate parents data
def generate_parents(num_parents):
    parents = []
    education_levels = ['Primary School', 'Secondary School', 'NCE', 'HND', 'BSc', 'MSc', 'PhD']
    
    for i in range(num_parents):
        parent_id = f"PR{i+1:03d}"
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        education_level = random.choice(education_levels)
        occupation = random.choice(['Teacher', 'Engineer', 'Trader', 'Civil Servant', 'Doctor', 'Farmer'])
        socioeconomic_status = 'High' if occupation in ['Engineer', 'Doctor'] else 'Middle' if occupation in ['Civil Servant', 'Teacher'] else 'Low'
        marriage_status = random.choice(['Married', 'Divorced', 'Single'])
        parents.append({
            'ID': parent_id,
            'First_Name': first_name,
            'Last_Name': last_name,
            'Education_Level': education_level,
            'Occupation': occupation,
            'Socioeconomic_Status': socioeconomic_status,
            'Marriage_Status': marriage_status
        })
    
    return parents

# Generate teachers data
def generate_teachers(num_teachers):
    teachers = []
    assigned_subjects = set()  # To keep track of subjects already assigned

    for i in range(num_teachers):
        teacher_id = f"TCH{i+1:03d}"
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        qualification = random.choice(teacher_qualifications)
        gender = random.choice(['Male', 'Female'])
        years_experience = random.randint(1, 30)

        # Assign subjects while ensuring no duplication except for special cases
        if 'Accounting' not in assigned_subjects and 'Bookkeeping' not in assigned_subjects:
            subject_specialization = ['Accounting', 'Bookkeeping']
            assigned_subjects.update(subject_specialization)
        elif 'Mathematics' not in assigned_subjects and 'Further Mathematics' not in assigned_subjects:
            subject_specialization = ['Mathematics', 'Further Mathematics']
            assigned_subjects.update(subject_specialization)
        elif 'English Studies' not in assigned_subjects and 'Literature-in-English' not in assigned_subjects:
            subject_specialization = ['English Studies', 'Literature-in-English']
            assigned_subjects.update(subject_specialization)
        else:
            # Choose remaining unassigned subjects
            unassigned_subjects = [subj for subj in all_subjects if subj not in assigned_subjects]
            if unassigned_subjects:
                subject_specialization = [random.choice(unassigned_subjects)]
                assigned_subjects.update(subject_specialization)
            else:
                break  # No more subjects to assign

        teachers.append({
            'ID': teacher_id,
            'First_Name': first_name,
            'Last_Name': last_name,
            'Qualification': qualification,
            'Subject_Specialization': ', '.join(subject_specialization),
            'Years_Experience': years_experience,
            'Gender': gender
        })
    
    return teachers

# Generate the datasets
students = generate_students(n_students)
subjects = generate_subjects()
performance = generate_performance(students)
attendance = generate_attendance(students)
parents = generate_parents(n_students)
teachers = generate_teachers(n_teachers)

# Convert to DataFrames for visualization
students_df = pd.DataFrame(students)
subjects_df = pd.DataFrame(subjects)
performance_df = pd.DataFrame(performance)
attendance_df = pd.DataFrame(attendance)
parents_df = pd.DataFrame(parents)
teachers_df = pd.DataFrame(teachers)

# Output sample of each table for verification
print(students_df.head())
print(subjects_df.head())
print(performance_df.head())
print(attendance_df.head())
print(parents_df.head())
print(teachers_df.head())

students_df.to_csv('students_data_final.csv', index=None)
performance_df.to_csv('student_performance_final.csv', index=None)
subjects_df.to_csv('subjects_final.csv', index=None)
parents_df.to_csv('parents_final.csv', index=None)
teachers_df.to_csv('teachers_final.csv', index=None)
attendance_df.to_csv('attendance_final.csv', index=None)
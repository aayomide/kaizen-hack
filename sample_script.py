# from faker import Faker
# from random import randint 
# import pandas as pd 

# fake = Faker('en_UK')
# # print(fake.name())
# # print(fake.email())
# # print(fake.country())
# # print(fake.name())
# # print(fake.text())
# # print(fake.latitude(), fake.longitude())
# # print(fake.url())

 
# def input_data(x):
   
#     # pandas dataframe
#     data = pd.DataFrame()
#     for i in range(0, x):
#         data.loc[i,'id']= randint(1, 100)
#         data.loc[i,'name']= fake.name()
#         data.loc[i,'address']= fake.address()
#         data.loc[i,'latitude']= str(fake.latitude())
#         data.loc[i,'longitude']= str(fake.longitude())
#     return data
   

# Faker.seed(3)
# input_data(10)
import random
import string
import pandas as pd
from datetime import datetime, timedelta

# Function to generate a random string (e.g., names)
def random_string(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=length))

# Function to generate random dates between two ranges
def random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

# Function to generate a synthetic dataset
def generate_synthetic_data(num_rows):
    data = {
        'Name': [random_string() for _ in range(num_rows)],
        'Age': [random.randint(18, 65) for _ in range(num_rows)],
        'Date_of_Joining': [random_date(datetime(2015, 1, 1), datetime(2023, 12, 31)) for _ in range(num_rows)],
        'Salary': [random.randint(30000, 120000) for _ in range(num_rows)],
        'Department': [random.choice(['HR', 'IT', 'Finance', 'Sales']) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)

# Example usage
synthetic_data = generate_synthetic_data(100)  # Generate 100 rows of synthetic data
print(synthetic_data.head())

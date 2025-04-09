# Step 1: Import necessary libraries
from faker import Faker
import pandas as pd
import random

# Step 2: Initialize Faker generator
fake = Faker()

# Step 3: Define helper function to generate customer segment
def get_segment():
    return random.choice(["Regular", "VIP", "New"])

# Step 4: Generate a list of dictionaries with fake customer data
customers = []
for i in range(1, 101):  # generating 100 customers
    customer = {
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "signup_date": fake.date_between(start_date='-2y', end_date='today'),
        "customer_segment": get_segment()
    }
    customers.append(customer)

# Step 5: Convert the list to a pandas DataFrame
df = pd.DataFrame(customers)

# Step 6: Save the DataFrame to a CSV file
df.to_csv("data/customers.csv", index=False)

print("✅ customers.csv generated successfully!")

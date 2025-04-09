# Step 1: Import necessary libraries
import pandas as pd
import random
from faker import Faker

# Step 2: Load existing order data and parse date column
orders_df = pd.read_csv("data/orders.csv", parse_dates=["order_date"])


# Step 3: Initialize Faker and create empty list for transactions
fake = Faker()
transactions = []

# Step 4: Generate one transaction per order
for i, row in orders_df.iterrows():
    transaction = {
        "transaction_id": i + 1,
        "order_id": row["order_id"],
        "payment_method": random.choice(["Credit Card", "PayPal", "UPI", "Net Banking"]),
        "amount": round(row["quantity"] * random.uniform(10, 500), 2),
        "transaction_date": fake.date_between(start_date=row["order_date"], end_date='today')
    }
    transactions.append(transaction)

# Step 5: Convert transactions list to a DataFrame
df = pd.DataFrame(transactions)

# Step 6: Save the DataFrame to a CSV file
df.to_csv("data/transactions.csv", index=False)

print("✅ transactions.csv generated successfully!")

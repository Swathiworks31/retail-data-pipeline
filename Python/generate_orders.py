# Step 1: Import necessary libraries
import pandas as pd
import random
from faker import Faker

# Step 2: Load existing customer and product data
customers_df = pd.read_csv("data/customers.csv")
products_df = pd.read_csv("data/products.csv")

# Step 3: Initialize Faker and empty order list
fake = Faker()
orders = []

# Step 4: Generate 200 fake orders
for i in range(1, 201):  # You can increase to 500 or 1000 later
    order = {
        "order_id": i,
        "customer_id": random.choice(customers_df["customer_id"].tolist()),
        "product_id": random.choice(products_df["product_id"].tolist()),
        "order_date": fake.date_between(start_date='-1y', end_date='today'),
        "quantity": random.randint(1, 5)
    }
    orders.append(order)

# Step 5: Convert the list of orders to a DataFrame
df = pd.DataFrame(orders)

# Step 6: Save the DataFrame to a CSV file
df.to_csv("data/orders.csv", index=False)

print("✅ orders.csv generated successfully!")

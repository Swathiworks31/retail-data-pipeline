# Step 1: Import necessary libraries
from faker import Faker
import pandas as pd
import random

# Step 2: Initialize Faker generator
fake = Faker()

# Step 3: Define product categories (for variety)
categories = ["Electronics", "Clothing", "Books", "Home Decor", "Toys", "Groceries"]

# Step 4: Create an empty list to store product records
products = []
for i in range(1, 51):  # You can change 51 to 101 if you want 100 products
    product = {
        "product_id": i,
        "name": fake.word().capitalize() + " " + random.choice(["Pro", "Lite", "X", "Max", "Edition"]),
        "category": random.choice(categories),
        "price": round(random.uniform(5, 1000), 2)  # random float between 5 and 1000, rounded to 2 decimals
    }
    products.append(product)

# Step 6: Convert list of product dictionaries into a DataFrame
df = pd.DataFrame(products)

# Step 7: Save the DataFrame to CSV inside the data folder
df.to_csv("data/products.csv", index=False)

print("✅ products.csv generated successfully!")
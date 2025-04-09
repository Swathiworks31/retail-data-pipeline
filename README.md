# 🛍️ Retail Data Pipeline Project

A complete end-to-end **Retail Data Pipeline** project built using **Python, Snowflake, and Power BI** to simulate how a company ingests, processes, and visualizes retail sales data for actionable insights.

---

## 📌 Project Overview

This project simulates a real-world retail system where sales, product, customer, and transaction data are:
- **Generated using Python & Faker**
- **Stored and transformed in Snowflake**
- **Visualized in Power BI**

The pipeline demonstrates real-world data engineering and analytics practices.

---

## 🧰 Tech Stack

| Tool/Tech     | Purpose                                  |
|--------------|-------------------------------------------|
| Python (Pandas, Faker) | Data generation, cleaning, ETL scripting     |
| Snowflake     | Cloud Data Warehouse: staging, transforms |
| SQL           | Schema creation, joins, aggregations     |
| Power BI      | Dashboarding and business insights       |

---

## 📁 Project Structure

Retail_Data_Pipeline_Project/
├── data/                        
│   ├── customers.csv
│   ├── orders.csv
│   ├── products.csv
│   └── transactions.csv

├── python/                      
│   ├── generate_customers.py
│   ├── generate_orders.py
│   ├── generate_products.py
│   └── generate_transactions.py

├── dashboard/

│   └── Retail_Sales_Insights_Dashboard.pbix     

├── snowflake/                   

└── README.md     

---

## 📊 Power BI Insights

- 🧸 **Top 5 Products by Revenue**  
- 📈 **Monthly Sales Trends**  
- 🧑‍🤝‍🧑 **Customer Segment Revenue Breakdown**

Dashboard built using views directly connected to Snowflake.

---

## 🧠 Business Questions Answered

- Which products generate the most revenue?
- How does revenue trend across months?
- Which customer segments are most valuable?

---

## 🚀 How to Use

1. Run the ETL scripts in `python/` to generate data
2. Load data into Snowflake using the schema in `snowflake/schema.sql`
3. Create analytical views using `snowflake/views.sql`
4. Open the Power BI `.pbix` file in `dashboard/` to explore insights

---

## 🏁 Next Improvements

- Add dbt for transformation layer
- Automate refresh using Python & SnowSQL
- Publish dashboard via Power BI service

---

## 👩‍💻 Author

**Swathi Reddy**  
_Data Enthusiast | Cloud & SQL Explorer | Building Data Engineering Portfolio_


               

import sqlite3
import pandas as pd
import random
from datetime import datetime, timedelta

# Create Dummy Database
conn = sqlite3.connect('ecommerce_sales.db')
cursor = conn.cursor()

# Create Tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        order_id INTEGER PRIMARY KEY,
        date TEXT,
        category TEXT,
        amount REAL,
        region TEXT
    )
''')

# Generate Data
categories = ['Electronics', 'Fashion', 'Home', 'Beauty']
regions = ['North', 'South', 'East', 'West']

data_rows = []
start_date = datetime(2024, 1, 1)

print("Running ETL Job: Ingesting Sales Data...")
for i in range(5000):
    date = (start_date + timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')
    category = random.choice(categories)
    amount = round(random.uniform(20.0, 500.0), 2)
    region = random.choice(regions)
    data_rows.append((i, date, category, amount, region))

cursor.executemany('INSERT OR REPLACE INTO sales VALUES (?,?,?,?,?)', data_rows)
conn.commit()
print("Data Successfully Loaded into SQL Database.")

# Verify
df = pd.read_sql_query("SELECT * FROM sales LIMIT 5", conn)
print(df)
conn.close()
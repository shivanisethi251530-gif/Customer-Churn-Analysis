import pandas as pd
import sqlite3

# Load cleaned data
df = pd.read_csv("data/TelecomCustomerChurn_clean.csv")

# Create SQLite database
conn = sqlite3.connect("churn.db")

# Load data into SQL table
df.to_sql("customers", conn, if_exists="replace", index=False)

conn.close()

print("Data loaded into SQLite successfully.")
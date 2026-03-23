import pandas as pd

# Load dataset
df = pd.read_csv("data/TelecomCustomerChurn.csv")

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Remove rows with missing values
df.dropna(inplace=True)

# Save cleaned file
df.to_csv("data/TelecomCustomerChurn_clean.csv", index=False)

print("Data cleaned and saved.")
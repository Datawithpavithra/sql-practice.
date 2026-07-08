import pandas as pd

df = pd.read_csv("sales.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df = df.fillna(0)

# Convert date column
df["Order Date"] = pd.to_datetime(df["Order Date"])

print(df.head())

import pandas as pd

# Load Dataset
df = pd.read_csv("sales.csv")

# Display first 5 rows
print(df.head())

# Dataset Information
print(df.info())

# Summary Statistics
print(df.describe())

# Missing Values
print(df.isnull().sum())

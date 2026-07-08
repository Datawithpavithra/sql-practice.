import pandas as pd

df = pd.read_csv("sales.csv")

print(df.describe())

print(df.corr(numeric_only=True))

print(df.groupby("Category")["Sales"].sum())

import pandas as pd

df = pd.read_csv("data/processed/sales_clean.csv")

print("DIMENSIONES")
print(df.shape)

print("\nNULOS")
print(df.isna().sum())

print("\nDUPLICADOS")
print(df.duplicated().sum())

print("\nCOLUMNAS")
print(df.columns.tolist())

print("\nTIPOS")
print(df.dtypes)
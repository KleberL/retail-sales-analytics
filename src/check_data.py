import pandas as pd

df = pd.read_csv("data/raw/sales_raw.csv")

print("PRIMERAS FILAS")
print(df.head())

print("\nINFORMACIÓN DEL DATASET")
df.info()

print("\nDIMENSIONES")
print(df.shape)

print("\nVALORES NULOS")
print(df.isna().sum())

print("\nDUPLICADOS")
print(df.duplicated().sum())
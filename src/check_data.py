import pandas as pd
from src.paths import RAW_SALES_FILE

df = pd.read_csv(RAW_SALES_FILE)

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
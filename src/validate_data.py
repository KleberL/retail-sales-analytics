import pandas as pd
from src.paths import CLEAN_SALES_FILE

df = pd.read_csv(CLEAN_SALES_FILE)

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
import pandas as pd
from src.paths import RAW_SALES_FILE, CLEAN_SALES_FILE

df = pd.read_csv(RAW_SALES_FILE)

# print("Filas antes de limpiar:", len(df))

df = df.drop_duplicates()

# print("Filas después de eliminar duplicados:", len(df))

df["Ciudad"] = df["Ciudad"].str.strip().str.title()

df["Producto"] = df["Producto"].str.strip().str.title()

df["Tienda"] = df["Tienda"].str.strip()

# print("\nCiudades:")
# print(df["Ciudad"].unique())

# print("\nProductos:")
# print(df["Producto"].unique())

df["Supervisor"] = df["Supervisor"].fillna("Sin asignar")

mediana_inventario = df["Inventario"].median()

df["Inventario"] = df["Inventario"].fillna(
    mediana_inventario
)

df["Inventario"] = df["Inventario"].astype(int)

# print("\nNulos después de limpiar:")
# print(df.isna().sum())

# print("\nMediana usada para Inventario:")
# print(mediana_inventario)

df["Tienda"] = df["Tienda"].replace(
    {
        "MTA centro": "MTA Centro"
    }
)

df["Fecha"] = pd.to_datetime(df["Fecha"])

df["Año"] = df["Fecha"].dt.year
df["Mes"] = df["Fecha"].dt.month


# print("\nTipo de Fecha:")
# print(df["Fecha"].dtype)

# print("\nTiendas:")
# print(sorted(df["Tienda"].unique()))

df["Venta_Total"] = df["Precio"] * df["Unidades"]

df["Cumplimiento"] = (
    df["Unidades"] / df["Target"] * 100
).round(2)

df["Cumple_Target"] = (
    df["Unidades"] >= df["Target"]
).astype(int)

df["Cobertura"] = (
    (df["Unidades"] > 0) |
    (df["Inventario"] > 0)
).astype(int)


columnas = [
    "Fecha",
    "Año",
    "Mes",
    "Ciudad",
    "Tienda",
    "Supervisor",
    "Producto",
    "Precio",
    "Unidades",
    "Target",
    "Inventario",
    "Venta_Total",
    "Cumplimiento",
    "Cumple_Target",
    "Cobertura"
]

df = df[columnas]

df.to_csv(
    CLEAN_SALES_FILE,
    index=False
)

print("\nDataset limpio:")
print(df.head())

print("\nDimensiones finales:")
print(df.shape)

print("\nDataset procesado guardado correctamente")
import pandas as pd 
import random
from datetime import datetime, timedelta
from src.paths import RAW_SALES_FILE

random.seed(42)

ciudades = [
    "Guayaquil",
    "Quito",
    "Cuenca",
    "Machala",
    "Manta"
]

productos = {
    "Nova X1": 180,
    "Nova X2": 230,
    "Nova Pro": 320,
    "Pulse A1": 150,
    "Pulse A2": 200
}

supervisores = [
    "Andrea Torres",
    "Carlos Mendoza",
    "Daniela Ruiz",
    "Luis Vera"
]

tiendas = {
    "Guayaquil": ["GYE Centro", "GYE Norte", "GYE Sur"],
    "Quito": ["UIO Centro", "UIO Norte", "UIO Sur"],
    "Cuenca": ["CUE Centro", "CUE Mall", "CUE Norte"],
    "Machala": ["MCH Centro", "MCH Norte", "MCH Sur"],
    "Manta": ["MTA Centro", "MTA Mall", "MTA Norte"]
}

registros = []

fecha_inicio = datetime(2026, 1, 1)

for i in range(500):
    fecha = fecha_inicio + timedelta(
        days=random.randint(0, 364)
    )

    ciudad = random.choice(ciudades)

    tienda = random.choice(
        tiendas[ciudad]
    )

    supervisor = random.choice(supervisores)

    producto = random.choice(
        list(productos.keys())
    )

    precio = productos[producto]

    unidades = random.randint(1, 10)

    target = random.randint(4, 12)

    inventario = random.randint(0, 20)

    registro = {
        "Fecha": fecha.date(),
        "Ciudad": ciudad,
        "Tienda": tienda,
        "Supervisor": supervisor,
        "Producto": producto,
        "Precio": precio,
        "Unidades": unidades,
        "Target": target,
        "Inventario": inventario
    }

    registros.append(registro)

df = pd.DataFrame(registros)


# Introducir problemas controlados de calidad de datos

# Valores nulos
df.loc[[3, 17, 88], "Supervisor"] = None
df.loc[[25, 111], "Inventario"] = None

# Inconsistencias de texto
df.loc[40, "Ciudad"] = " guayaquil "
df.loc[150, "Producto"] = "nova x2"
df.loc[275, "Tienda"] = "MTA centro"

# Filas duplicadas
duplicados = df.iloc[[10, 50, 120, 220, 350]].copy()

df = pd.concat(
    [df, duplicados],
    ignore_index=True
)

print(df.head())
print()
print("Cantidad de registros:", len(df))


df.to_csv(
    RAW_SALES_FILE,
    index=False
)

print("Dataset generado correctamente")
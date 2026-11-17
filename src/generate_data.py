import random
from datetime import datetime, timedelta

import pandas as pd

from src.paths import RAW_SALES_FILE


random.seed(42)


# Catálogos del proyecto
cities = [
    "Guayaquil",
    "Quito",
    "Cuenca",
    "Machala",
    "Manta",
]

products = {
    "Nova X1": 180,
    "Nova X2": 230,
    "Nova Pro": 320,
    "Pulse A1": 150,
    "Pulse A2": 200,
}

supervisors = [
    "Carlos Mendoza",
    "Andrea Ruiz",
    "Luis Torres",
    "Sofía Herrera",
]

stores = {
    "Guayaquil": [
        "GYE Centro",
        "GYE Norte",
        "GYE Sur",
    ],
    "Quito": [
        "UIO Centro",
        "UIO Norte",
        "UIO Sur",
    ],
    "Cuenca": [
        "CUE Centro",
        "CUE Norte",
        "CUE Sur",
    ],
    "Machala": [
        "MCH Centro",
        "MCH Norte",
        "MCH Sur",
    ],
    "Manta": [
        "MTA Centro",
        "MTA Norte",
        "MTA Sur",
    ],
}


# Fecha inicial para generar ventas durante un año
start_date = datetime(2026, 1, 1)


data = []


for _ in range(500):
    city = random.choice(cities)
    store = random.choice(stores[city])

    product = random.choice(list(products.keys()))
    price = products[product]

    date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    # Aproximadamente 20% de los registros tendrá cero ventas.
    units = (
        0
        if random.random() < 0.20
        else random.randint(1, 10)
    )

    target = random.randint(4, 12)

    # Aproximadamente 30% tendrá inventario igual a cero.
    inventory = (
        0
        if random.random() < 0.30
        else random.randint(1, 20)
    )

    supervisor = random.choice(supervisors)

    data.append({
        "Fecha": date.strftime("%Y-%m-%d"),
        "Ciudad": city,
        "Tienda": store,
        "Supervisor": supervisor,
        "Producto": product,
        "Precio": price,
        "Unidades": units,
        "Target": target,
        "Inventario": inventory,
    })


df = pd.DataFrame(data)


# --------------------------------------------------
# Problemas controlados de calidad
# --------------------------------------------------

# Valores nulos en Supervisor
df.loc[5, "Supervisor"] = None
df.loc[100, "Supervisor"] = None
df.loc[250, "Supervisor"] = None


# Valores nulos en Inventario
df.loc[50, "Inventario"] = None
df.loc[300, "Inventario"] = None


# Espacios innecesarios
df.loc[20, "Ciudad"] = " Guayaquil "
df.loc[75, "Producto"] = " Nova X1 "
df.loc[160, "Supervisor"] = " Carlos Mendoza "


# Diferencias de mayúsculas y minúsculas
df.loc[120, "Ciudad"] = "quito"
df.loc[220, "Producto"] = "pulse a2"


# Inconsistencia controlada en una tienda
df.loc[350, "Tienda"] = "MTA centro"


# --------------------------------------------------
# Crear duplicados intencionales
# --------------------------------------------------

duplicate_rows = df.iloc[:5].copy()

df = pd.concat(
    [df, duplicate_rows],
    ignore_index=True,
)


# --------------------------------------------------
# Guardar dataset raw
# --------------------------------------------------

df.to_csv(
    RAW_SALES_FILE,
    index=False,
)


print("Dataset generado correctamente")
print(f"Archivo: {RAW_SALES_FILE}")
print(f"Filas generadas: {len(df)}")
print(f"Columnas: {len(df.columns)}")
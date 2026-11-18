import random
from datetime import datetime, timedelta

import pandas as pd

from src.paths import RAW_SALES_FILE


CITIES = [
    "Guayaquil",
    "Quito",
    "Cuenca",
    "Machala",
    "Manta",
]

PRODUCTS = {
    "Nova X1": 180,
    "Nova X2": 230,
    "Nova Pro": 320,
    "Pulse A1": 150,
    "Pulse A2": 200,
}

SUPERVISORS = [
    "Carlos Mendoza",
    "Andrea Ruiz",
    "Luis Torres",
    "Sofía Herrera",
]

STORES = {
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


def generate_dataset(
    rows=500,
    seed=42,
):
    random.seed(seed)

    start_date = datetime(
        2026,
        1,
        1,
    )

    data = []

    for _ in range(rows):
        city = random.choice(CITIES)
        store = random.choice(STORES[city])

        product = random.choice(
            list(PRODUCTS.keys())
        )

        price = PRODUCTS[product]

        date = start_date + timedelta(
            days=random.randint(0, 364)
        )

        units = (
            0
            if random.random() < 0.20
            else random.randint(1, 10)
        )

        target = random.randint(
            4,
            12,
        )

        inventory = (
            0
            if random.random() < 0.30
            else random.randint(1, 20)
        )

        supervisor = random.choice(
            SUPERVISORS
        )

        data.append({
            "Fecha": date.strftime(
                "%Y-%m-%d"
            ),
            "Ciudad": city,
            "Tienda": store,
            "Supervisor": supervisor,
            "Producto": product,
            "Precio": price,
            "Unidades": units,
            "Target": target,
            "Inventario": inventory,
        })

    return pd.DataFrame(data)


def add_quality_issues(df):
    df = df.copy()

    df.loc[5, "Supervisor"] = None
    df.loc[100, "Supervisor"] = None
    df.loc[250, "Supervisor"] = None

    df.loc[50, "Inventario"] = None
    df.loc[300, "Inventario"] = None

    df.loc[20, "Ciudad"] = " Guayaquil "
    df.loc[75, "Producto"] = " Nova X1 "
    df.loc[160, "Supervisor"] = " Carlos Mendoza "

    df.loc[120, "Ciudad"] = "quito"
    df.loc[220, "Producto"] = "pulse a2"

    df.loc[350, "Tienda"] = "MTA centro"

    duplicate_rows = df.iloc[:5].copy()

    df = pd.concat(
        [
            df,
            duplicate_rows,
        ],
        ignore_index=True,
    )

    return df


def save_dataset(df):
    df.to_csv(
        RAW_SALES_FILE,
        index=False,
    )

    print(
        "Dataset generado correctamente"
    )
    print(
        f"Archivo: {RAW_SALES_FILE}"
    )
    print(
        f"Filas generadas: {len(df)}"
    )
    print(
        f"Columnas: {len(df.columns)}"
    )


def main():
    df = generate_dataset()

    df = add_quality_issues(
        df
    )

    save_dataset(
        df
    )


if __name__ == "__main__":
    main()
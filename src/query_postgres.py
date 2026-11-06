import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

url = URL.create(
    drivername="postgresql+psycopg",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)

engine = create_engine(url)

consulta = """
SELECT
    producto,
    SUM(unidades) AS unidades_totales,
    SUM(venta_total) AS venta_total,
    ROUND(AVG(cumplimiento), 2) AS cumplimiento_promedio
FROM sales
GROUP BY producto
ORDER BY venta_total DESC;
"""

df = pd.read_sql(
    consulta,
    engine
)

print(df)

engine.dispose()
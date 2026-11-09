import pandas as pd

from src.database import get_engine


engine = get_engine()

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
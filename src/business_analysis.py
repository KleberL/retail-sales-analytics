import pandas as pd
import matplotlib.pyplot as plt

from src.database import get_engine
from src.paths import (
    KPI_REPORT_FILE,
    CITY_REPORT_FILE,
    PRODUCT_REPORT_FILE,
    MONTH_REPORT_FILE,
    CITY_CHART_FILE,
    MONTH_CHART_FILE,
)


engine = get_engine()

consulta_kpis = """
SELECT
    SUM(unidades) AS unidades_totales,
    SUM(venta_total) AS venta_total,
    ROUND(AVG(cumplimiento), 2) AS cumplimiento_promedio,
    ROUND(
        AVG(cumple_target) * 100,
        2
    ) AS porcentaje_cumplimiento
FROM sales;
"""

kpis = pd.read_sql(
    consulta_kpis,
    engine
)

print("\n=== KPIs GENERALES ===")
print(kpis)


consulta_ciudades = """
SELECT
    ciudad,
    SUM(unidades) AS unidades_totales,
    SUM(venta_total) AS venta_total,
    ROUND(AVG(cumplimiento), 2) AS cumplimiento_promedio
FROM sales
GROUP BY ciudad
ORDER BY venta_total DESC;
"""

ventas_ciudad = pd.read_sql(
    consulta_ciudades,
    engine
)

print("\n=== RENDIMIENTO POR CIUDAD ===")
print(ventas_ciudad)


# Gráfico de venta total por ciudad
fig, ax = plt.subplots(figsize=(9, 5))

ax.bar(
    ventas_ciudad["ciudad"],
    ventas_ciudad["venta_total"]
)

ax.set_title("Venta total por ciudad")
ax.set_xlabel("Ciudad")
ax.set_ylabel("Venta total")

ax.bar_label(
    ax.containers[0],
    fmt="%.0f"
)

plt.tight_layout()

plt.savefig(
    CITY_CHART_FILE,
    dpi=300
)

plt.close()


consulta_mensual = """
SELECT
    mes,
    SUM(unidades) AS unidades_totales,
    SUM(venta_total) AS venta_total
FROM sales
GROUP BY mes
ORDER BY mes;
"""

ventas_mes = pd.read_sql(
    consulta_mensual,
    engine
)

print("\n=== VENTAS POR MES ===")
print(ventas_mes)


fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    ventas_mes["mes"],
    ventas_mes["venta_total"],
    marker="o"
)

ax.set_title("Evolución mensual de ventas")
ax.set_xlabel("Mes")
ax.set_ylabel("Venta total")

ax.set_xticks(
    ventas_mes["mes"]
)

ax.grid(
    axis="y",
    alpha=0.3
)

plt.tight_layout()

plt.savefig(
    MONTH_CHART_FILE,
    dpi=300
)

plt.close()

consulta_productos = """
SELECT
    producto,
    SUM(unidades) AS unidades_totales,
    SUM(venta_total) AS venta_total,
    ROUND(AVG(cumplimiento), 2) AS cumplimiento_promedio
FROM sales
GROUP BY producto
ORDER BY venta_total DESC;
"""

ventas_producto = pd.read_sql(
    consulta_productos,
    engine
)

print("\n=== RENDIMIENTO POR PRODUCTO ===")
print(ventas_producto)

mejor_ciudad = ventas_ciudad.loc[
    ventas_producto["venta_total"].idxmax()
]

mejor_producto = ventas_producto.loc[
    ventas_producto["venta_total"].idxmax()
]

mejor_mes = ventas_mes.loc[
    ventas_mes["venta_total"].idxmax()
]

peor_mes = ventas_mes.loc[
    ventas_mes["venta_total"].idxmin()
]

print("\n=== PRINCIPALES INSIGHTS ===")

print(
    f"Mejor ciudad por ventas: "
    f"{mejor_ciudad['ciudad']} "
    f"(${mejor_ciudad['venta_total']})"
)

print(
    f"Mejor producto por ventas: "
    f"{mejor_producto['producto']} "
    f"(${mejor_producto['venta_total']})"
)

print(
    f"Mejor mes: "
    f"{int(mejor_mes['mes'])} "
    f"(${mejor_mes['venta_total']})"
)

print(
    f"Mes con menor venta: "
    f"{int(peor_mes['mes'])} "
    f"(${peor_mes['venta_total']})"
)

kpis.to_csv(
    KPI_REPORT_FILE,
    index=False
)

ventas_ciudad.to_csv(
    CITY_REPORT_FILE,
    index=False
)

ventas_producto.to_csv(
    PRODUCT_REPORT_FILE,
    index=False
)

ventas_mes.to_csv(
    MONTH_REPORT_FILE,
    index=False
)

engine.dispose()
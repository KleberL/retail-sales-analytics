import matplotlib.pyplot as plt
import pandas as pd

from src.database import get_engine
from src.paths import (
    KPI_REPORT_FILE,
    CITY_REPORT_FILE,
    PRODUCT_REPORT_FILE,
    MONTH_REPORT_FILE,
    CITY_CHART_FILE,
    MONTH_CHART_FILE,
)


def get_kpis(engine):
    query = """
    SELECT
        SUM(unidades) AS total_unidades,
        SUM(venta_total) AS venta_total,
        ROUND(AVG(cumplimiento), 2) AS cumplimiento_promedio,
        ROUND(AVG(cumple_target) * 100, 2) AS porcentaje_cumple_target,
        ROUND(AVG(cobertura) * 100, 2) AS cobertura_general
    FROM sales;
    """

    return pd.read_sql(
        query,
        engine,
    )


def get_city_analysis(engine):
    query = """
    SELECT
        ciudad,
        SUM(unidades) AS unidades,
        SUM(venta_total) AS venta_total,
        ROUND(AVG(cumplimiento), 2) AS cumplimiento_promedio,
        ROUND(AVG(cobertura) * 100, 2) AS cobertura_promedio
    FROM sales
    GROUP BY ciudad
    ORDER BY venta_total DESC;
    """

    return pd.read_sql(
        query,
        engine,
    )


def get_product_analysis(engine):
    query = """
    SELECT
        producto,
        SUM(unidades) AS unidades,
        SUM(venta_total) AS venta_total,
        ROUND(AVG(cumplimiento), 2) AS cumplimiento_promedio
    FROM sales
    GROUP BY producto
    ORDER BY venta_total DESC;
    """

    return pd.read_sql(
        query,
        engine,
    )


def get_month_analysis(engine):
    query = """
    SELECT
        mes,
        SUM(unidades) AS unidades,
        SUM(venta_total) AS venta_total
    FROM sales
    GROUP BY mes
    ORDER BY mes;
    """

    return pd.read_sql(
        query,
        engine,
    )


def print_results(
    df_kpis,
    df_cities,
    df_products,
    df_months,
):
    print("\n" + "=" * 60)
    print("KPIs GENERALES")
    print("=" * 60)

    print(
        f"Unidades vendidas: "
        f"{int(df_kpis.loc[0, 'total_unidades'])}"
    )

    print(
        f"Venta total: "
        f"${int(df_kpis.loc[0, 'venta_total']):,}"
    )

    print(
        f"Cumplimiento promedio: "
        f"{float(df_kpis.loc[0, 'cumplimiento_promedio']):.2f}%"
    )

    print(
        f"Registros que cumplen target: "
        f"{float(df_kpis.loc[0, 'porcentaje_cumple_target']):.2f}%"
    )

    print(
        f"Cobertura general: "
        f"{float(df_kpis.loc[0, 'cobertura_general']):.2f}%"
    )

    print("\n" + "=" * 60)
    print("VENTAS POR CIUDAD")
    print("=" * 60)

    print(
        df_cities.to_string(
            index=False
        )
    )

    print("\n" + "=" * 60)
    print("VENTAS POR PRODUCTO")
    print("=" * 60)

    print(
        df_products.to_string(
            index=False
        )
    )

    print("\n" + "=" * 60)
    print("VENTAS POR MES")
    print("=" * 60)

    print(
        df_months.to_string(
            index=False
        )
    )


def print_insights(
    df_cities,
    df_products,
    df_months,
):
    best_city = df_cities.loc[
        df_cities["venta_total"].idxmax()
    ]

    best_product = df_products.loc[
        df_products["venta_total"].idxmax()
    ]

    best_month = df_months.loc[
        df_months["venta_total"].idxmax()
    ]

    worst_month = df_months.loc[
        df_months["venta_total"].idxmin()
    ]

    best_coverage_city = df_cities.loc[
        df_cities["cobertura_promedio"].idxmax()
    ]

    print("\n" + "=" * 60)
    print("INSIGHTS")
    print("=" * 60)

    print(
        f"Ciudad con mayor venta: "
        f"{best_city['ciudad']} "
        f"(${int(best_city['venta_total']):,})"
    )

    print(
        f"Producto con mayor venta: "
        f"{best_product['producto']} "
        f"(${int(best_product['venta_total']):,})"
    )

    print(
        f"Mes con mayor venta: "
        f"{int(best_month['mes'])} "
        f"(${int(best_month['venta_total']):,})"
    )

    print(
        f"Mes con menor venta: "
        f"{int(worst_month['mes'])} "
        f"(${int(worst_month['venta_total']):,})"
    )

    print(
        f"Ciudad con mayor cobertura: "
        f"{best_coverage_city['ciudad']} "
        f"({float(best_coverage_city['cobertura_promedio']):.2f}%)"
    )


def save_reports(
    df_kpis,
    df_cities,
    df_products,
    df_months,
):
    df_kpis.to_csv(
        KPI_REPORT_FILE,
        index=False,
    )

    df_cities.to_csv(
        CITY_REPORT_FILE,
        index=False,
    )

    df_products.to_csv(
        PRODUCT_REPORT_FILE,
        index=False,
    )

    df_months.to_csv(
        MONTH_REPORT_FILE,
        index=False,
    )

    print(
        "\nReportes CSV guardados correctamente"
    )


def create_charts(
    df_cities,
    df_months,
):
    plt.figure(
        figsize=(9, 5)
    )

    plt.bar(
        df_cities["ciudad"],
        df_cities["venta_total"],
    )

    plt.title(
        "Venta total por ciudad"
    )

    plt.xlabel(
        "Ciudad"
    )

    plt.ylabel(
        "Venta total"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.savefig(
        CITY_CHART_FILE,
        dpi=150,
    )

    plt.close()

    plt.figure(
        figsize=(9, 5)
    )

    plt.plot(
        df_months["mes"],
        df_months["venta_total"],
        marker="o",
    )

    plt.title(
        "Evolución mensual de ventas"
    )

    plt.xlabel(
        "Mes"
    )

    plt.ylabel(
        "Venta total"
    )

    plt.xticks(
        df_months["mes"]
    )

    plt.grid(
        alpha=0.3
    )

    plt.tight_layout()

    plt.savefig(
        MONTH_CHART_FILE,
        dpi=150,
    )

    plt.close()

    print(
        "Gráficos guardados correctamente"
    )


def main():
    engine = get_engine()

    df_kpis = get_kpis(
        engine
    )

    df_cities = get_city_analysis(
        engine
    )

    df_products = get_product_analysis(
        engine
    )

    df_months = get_month_analysis(
        engine
    )

    print_results(
        df_kpis,
        df_cities,
        df_products,
        df_months,
    )

    print_insights(
        df_cities,
        df_products,
        df_months,
    )

    save_reports(
        df_kpis,
        df_cities,
        df_products,
        df_months,
    )

    create_charts(
        df_cities,
        df_months,
    )


if __name__ == "__main__":
    main()
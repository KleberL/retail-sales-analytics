from pathlib import Path


# Raíz del proyecto:
# retail-sales-analytics/
PROJECT_ROOT = Path(__file__).resolve().parent.parent


# Carpetas principales
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

REPORTS_DIR = PROJECT_ROOT / "reports"
IMAGES_DIR = PROJECT_ROOT / "images"
SQL_DIR = PROJECT_ROOT / "sql"


# Archivos de datos
RAW_SALES_FILE = RAW_DATA_DIR / "sales_raw.csv"
CLEAN_SALES_FILE = PROCESSED_DATA_DIR / "sales_clean.csv"


# Reportes CSV
KPI_REPORT_FILE = REPORTS_DIR / "kpis_generales.csv"
CITY_REPORT_FILE = REPORTS_DIR / "ventas_por_ciudad.csv"
PRODUCT_REPORT_FILE = REPORTS_DIR / "ventas_por_producto.csv"
MONTH_REPORT_FILE = REPORTS_DIR / "ventas_por_mes.csv"


# Gráficos
CITY_CHART_FILE = IMAGES_DIR / "ventas_por_ciudad.png"
MONTH_CHART_FILE = IMAGES_DIR / "ventas_mensuales.png"
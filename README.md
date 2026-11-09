# Retail Sales & Inventory Analytics

Proyecto de análisis de datos enfocado en ventas, cumplimiento de objetivos e inventario para un negocio minorista ficticio.

El proyecto implementa un flujo completo de datos utilizando Python, PostgreSQL y SQL, desde la generación y limpieza de información hasta la creación automatizada de KPIs, reportes y visualizaciones.

> Los datos utilizados en este proyecto son completamente sintéticos y fueron generados únicamente con fines educativos y de portafolio.

## Objetivo del proyecto

Construir un flujo de análisis reproducible que permita:

- Generar datos de ventas ficticios pero realistas.
- Detectar y corregir problemas de calidad de datos.
- Almacenar información procesada en PostgreSQL.
- Analizar ventas mediante SQL.
- Consultar PostgreSQL desde Python.
- Calcular KPIs de negocio.
- Identificar ciudades, productos y meses con mejor desempeño.
- Generar reportes y gráficos automáticamente.

## Pipeline de datos

```text
Datos sintéticos
      ↓
sales_raw.csv
      ↓
Limpieza con pandas
      ↓
sales_clean.csv
      ↓
PostgreSQL
      ↓
Consultas SQL
      ↓
Python + pandas
      ↓
KPIs e insights
      ↓
Reportes CSV + gráficos
```

## KPIs principales

El análisis actual obtiene los siguientes resultados:

| KPI | Resultado |
|---|---:|
| Unidades vendidas | 2,643 |
| Venta total | $572,420 |
| Cumplimiento promedio | 74.67% |
| Registros que cumplen el target | 28.60% |

## Principales insights

- **Manta** es la ciudad con mayor venta total: **$133,830**.
- **Nova Pro** es el producto con mayor venta total: **$180,160**.
- **Agosto** es el mes con mayor venta: **$68,850**.
- **Abril** es el mes con menor venta: **$28,760**.
- **Machala** presenta el mayor cumplimiento promedio entre las ciudades: **77.44%**.
- El producto con mayor volumen de unidades vendidas es **Pulse A1**, mientras que **Nova Pro** genera el mayor valor de ventas.

Debido a que el dataset es sintético, estos resultados sirven para demostrar el proceso analítico y no representan tendencias reales de mercado.

## Visualizaciones

### Venta total por ciudad

![Venta total por ciudad](images/ventas_por_ciudad.png)

### Evolución mensual de ventas

![Evolución mensual de ventas](images/ventas_mensuales.png)

## Tecnologías utilizadas

- Python
- pandas
- PostgreSQL
- SQL
- psycopg
- SQLAlchemy
- python-dotenv
- Matplotlib
- Git
- GitHub

## Estructura del proyecto

```text
retail-sales-analytics/
│
├── data/
│   ├── raw/
│   │   └── sales_raw.csv
│   └── processed/
│       └── sales_clean.csv
│
├── images/
│   ├── ventas_mensuales.png
│   └── ventas_por_ciudad.png
│
├── reports/
│   ├── kpis_generales.csv
│   ├── ventas_por_ciudad.csv
│   ├── ventas_por_mes.csv
│   └── ventas_por_producto.csv
│
├── sql/
│   └── analysis_queries.sql
│
├── src/
│   ├── generate_data.py
│   ├── check_data.py
│   ├── clean_data.py
│   ├── validate_data.py
│   ├── load_to_postgres.py
│   ├── query_postgres.py
│   └── business_analysis.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Flujo del proyecto

### 1. Generación de datos

`generate_data.py` crea un dataset sintético de ventas e introduce algunos problemas controlados de calidad, como:

- valores nulos,
- registros duplicados,
- inconsistencias de formato,
- diferencias en mayúsculas y minúsculas.

### 2. Revisión de calidad

`check_data.py` permite inspeccionar:

- dimensiones del dataset,
- tipos de datos,
- valores nulos,
- duplicados.

### 3. Limpieza y transformación

`clean_data.py`:

- elimina duplicados,
- normaliza valores de texto,
- completa valores faltantes,
- convierte fechas,
- crea variables derivadas,
- calcula ventas y cumplimiento,
- genera indicadores de cobertura.

El resultado se almacena en:

```text
data/processed/sales_clean.csv
```

### 4. Validación

`validate_data.py` verifica que el dataset procesado:

- no contenga valores nulos,
- no contenga duplicados,
- tenga las columnas esperadas.

### 5. Carga en PostgreSQL

`load_to_postgres.py` carga los datos procesados en la tabla:

```text
sales
```

dentro de la base de datos PostgreSQL:

```text
retail_sales_analytics
```

### 6. Análisis SQL y Python

Las consultas SQL permiten analizar:

- ventas por ciudad,
- ventas por producto,
- comportamiento mensual,
- cumplimiento de objetivos.

`business_analysis.py` consulta PostgreSQL y genera automáticamente KPIs, rankings, reportes y visualizaciones.

## Configuración de credenciales

Las credenciales de PostgreSQL no se almacenan directamente en el código.

El proyecto utiliza un archivo local `.env` con una estructura similar a:

```text
DB_NAME=retail_sales_analytics
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

El archivo `.env` está incluido en `.gitignore` y no debe subirse al repositorio.

## Ejecución

Después de instalar las dependencias y configurar PostgreSQL:

```bash
python src/generate_data.py
python src/check_data.py
python src/clean_data.py
python src/validate_data.py

python -m src.load_to_postgres
python -m src.query_postgres
python -m src.business_analysis
```

Los resultados del análisis se generan automáticamente dentro de:

```text
reports/
images/
```

## Habilidades demostradas

Este proyecto demuestra conocimientos prácticos de:

- limpieza y transformación de datos con pandas,
- análisis exploratorio de datos,
- SQL y agregaciones,
- integración Python–PostgreSQL,
- creación de KPIs,
- automatización de reportes,
- visualización de datos,
- manejo seguro de credenciales,
- control de versiones con Git,
- organización de proyectos de datos.

## Estado del proyecto

El proyecto continúa en desarrollo como parte de una ruta de aprendizaje de análisis y ciencia de datos.
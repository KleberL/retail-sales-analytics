# Retail Sales & Inventory Analytics

Proyecto end-to-end de análisis de datos para un negocio minorista ficticio, enfocado en ventas, cumplimiento de objetivos e inventario.

El proyecto cubre un flujo completo de datos: generación de información sintética, control de calidad, limpieza con Python y pandas, almacenamiento en PostgreSQL, análisis con SQL, cálculo de KPIs, generación de reportes y creación automatizada de visualizaciones.

> **Nota:** todos los datos utilizados son sintéticos y fueron generados exclusivamente con fines educativos y de portafolio. No contienen información real de empresas, clientes o personas.

---

## Objetivo

Construir un pipeline de análisis reproducible que permita:

- Generar datos de ventas ficticios con problemas controlados de calidad.
- Detectar valores nulos, duplicados e inconsistencias.
- Limpiar y transformar información con pandas.
- Calcular métricas derivadas de ventas, cumplimiento y cobertura.
- Almacenar los datos procesados en PostgreSQL.
- Ejecutar análisis mediante SQL.
- Consultar PostgreSQL desde Python.
- Crear KPIs y rankings de negocio.
- Detectar automáticamente los mejores y peores resultados.
- Generar reportes CSV y gráficos reutilizables.
- Mantener credenciales fuera del código.
- Ejecutar el proyecto dentro de un entorno virtual reproducible.
- Centralizar las rutas del proyecto mediante `pathlib`.
- Validar la configuración antes de conectarse a PostgreSQL.
- Manejar errores de conexión y liberar recursos correctamente.

---

## Pipeline de datos

```text
Datos sintéticos
      ↓
sales_raw.csv
      ↓
Control de calidad
      ↓
Limpieza y transformación con pandas
      ↓
sales_clean.csv
      ↓
PostgreSQL
      ↓
Consultas SQL
      ↓
Python + SQLAlchemy
      ↓
KPIs e insights
      ↓
Reportes CSV + visualizaciones
```

---

## KPIs principales

| KPI | Resultado |
|---|---:|
| Unidades vendidas | 2,643 |
| Venta total | $572,420 |
| Cumplimiento promedio | 74.67% |
| Registros que cumplen el target | 28.60% |

---

## Principales insights

- **Manta** presenta la mayor venta total: **$133,830**.
- **Nova Pro** es el producto con mayor venta total: **$180,160**.
- **Pulse A1** registra el mayor volumen de unidades vendidas.
- **Pulse A2** presenta el mayor cumplimiento promedio entre los productos: **83.82%**.
- **Machala** registra el mayor cumplimiento promedio entre las ciudades: **77.44%**.
- **Agosto** es el mes con mayor venta: **$68,850**.
- **Abril** es el mes con menor venta: **$28,760**.

La ciudad con mayor volumen de ventas no necesariamente es la que presenta mayor cumplimiento de objetivos, lo que demuestra la importancia de analizar diferentes KPIs antes de evaluar desempeño.

Debido a que el dataset es sintético, estos resultados demuestran el proceso analítico y no deben interpretarse como tendencias reales de mercado.

---

# Visualizaciones

## Venta total por ciudad

![Venta total por ciudad](images/ventas_por_ciudad.png)

## Evolución mensual de ventas

![Evolución mensual de ventas](images/ventas_mensuales.png)

---

# Tecnologías utilizadas

## Lenguajes y análisis

- Python 3.11
- SQL
- pandas
- NumPy

## Base de datos

- PostgreSQL
- psycopg
- SQLAlchemy

## Visualización

- Matplotlib

## Configuración y seguridad

- python-dotenv
- Variables de entorno
- `.gitignore`

## Organización del proyecto

- `pathlib`
- módulos Python
- paquetes Python
- entorno virtual `venv`
- separación de responsabilidades
- manejo de excepciones

## Control de versiones

- Git
- GitHub

---

# Estructura del proyecto

```text
retail-sales-analytics/
│
├── data/
│   ├── raw/
│   │   └── sales_raw.csv
│   │
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
│   ├── __init__.py
│   ├── database.py
│   ├── paths.py
│   ├── generate_data.py
│   ├── check_data.py
│   ├── clean_data.py
│   ├── validate_data.py
│   ├── load_to_postgres.py
│   ├── query_postgres.py
│   └── business_analysis.py
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

El directorio `.venv/` se crea localmente para el entorno virtual, pero está excluido del repositorio mediante `.gitignore`.

---

# Flujo del proyecto

## 1. Generación de datos

`generate_data.py` crea un dataset sintético de ventas con aproximadamente 500 registros.

Además introduce intencionalmente problemas controlados de calidad para simular situaciones reales:

- valores nulos,
- registros duplicados,
- espacios innecesarios,
- diferencias entre mayúsculas y minúsculas,
- inconsistencias en nombres.

El resultado inicial se almacena en:

```text
data/raw/sales_raw.csv
```

---

## 2. Control de calidad

`check_data.py` realiza una inspección inicial del dataset y permite revisar:

- número de filas y columnas,
- tipos de datos,
- valores nulos,
- registros duplicados,
- estructura general de la información.

---

## 3. Limpieza y transformación

`clean_data.py` realiza el procesamiento principal del dataset.

Entre las transformaciones se incluyen:

- eliminación de duplicados,
- normalización de texto,
- tratamiento de valores faltantes,
- conversión de fechas,
- creación de año y mes,
- cálculo de venta total,
- cálculo de porcentaje de cumplimiento,
- creación de indicador de cumplimiento de target,
- creación de indicador de cobertura.

El dataset procesado se almacena en:

```text
data/processed/sales_clean.csv
```

---

## 4. Validación

`validate_data.py` comprueba que el dataset final:

- no contenga valores nulos,
- no contenga duplicados,
- tenga las columnas esperadas,
- conserve una estructura adecuada para el análisis.

---

## 5. Gestión centralizada de rutas

Las rutas utilizadas por los diferentes módulos están centralizadas en:

```text
src/paths.py
```

El proyecto utiliza `pathlib` para construir rutas a partir de la carpeta raíz.

Ejemplo:

```python
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
REPORTS_DIR = PROJECT_ROOT / "reports"
IMAGES_DIR = PROJECT_ROOT / "images"
```

Esto evita repetir rutas manuales en diferentes archivos.

En lugar de escribir:

```python
pd.read_csv("data/processed/sales_clean.csv")
```

los módulos utilizan:

```python
from src.paths import CLEAN_SALES_FILE

df = pd.read_csv(CLEAN_SALES_FILE)
```

Esto facilita el mantenimiento y reduce errores relacionados con rutas.

---

## 6. Configuración de PostgreSQL

La configuración de base de datos está centralizada en:

```text
src/database.py
```

El módulo se encarga de:

- cargar las variables desde `.env`,
- validar la configuración,
- crear conexiones mediante SQLAlchemy,
- proporcionar parámetros para psycopg.

El flujo es:

```text
.env
 ↓
get_db_config()
 ↓
validación
 ↓
get_engine()
o
get_connection_params()
```

---

## 7. Validación de configuración

Antes de crear una conexión, `database.py` comprueba que las variables necesarias tengan un valor válido.

Las variables requeridas son:

```text
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

Si alguna falta o está vacía, el programa genera un error claro.

Ejemplo:

```text
RuntimeError: Faltan variables de entorno: port
```

Esto evita que el programa continúe hasta producir errores menos claros dentro de PostgreSQL o SQLAlchemy.

---

## 8. Carga de datos a PostgreSQL

`load_to_postgres.py`:

- obtiene la configuración validada,
- crea una conexión mediante psycopg,
- crea la tabla `sales` si no existe,
- elimina los datos de la carga anterior,
- carga las 500 filas procesadas,
- confirma los cambios mediante una transacción,
- cierra correctamente los recursos utilizados.

La información se almacena en la base de datos:

```text
retail_sales_analytics
```

---

## 9. Manejo de errores

La carga de datos utiliza:

```text
try
except
finally
```

para controlar errores de PostgreSQL y garantizar el cierre de recursos.

Flujo general:

```text
try
→ intenta conectarse
→ crea el cursor
→ ejecuta operaciones SQL
→ carga los datos

except
→ captura errores de PostgreSQL
→ muestra información del error
→ vuelve a propagar el error

finally
→ cierra el cursor si fue creado
→ cierra la conexión si fue creada
```

Ejemplo simplificado:

```python
conexion = None
cursor = None

try:
    conexion = psycopg.connect(**parametros)
    cursor = conexion.cursor()

except psycopg.Error as error:
    print("Error de PostgreSQL:")
    print(error)
    raise

finally:
    if cursor is not None:
        cursor.close()

    if conexion is not None:
        conexion.close()
```

Este enfoque evita dejar conexiones abiertas si ocurre un error durante una operación.

---

## 10. Análisis SQL

Las consultas principales se almacenan en:

```text
sql/analysis_queries.sql
```

El análisis incluye:

- ventas por ciudad,
- ventas por producto,
- unidades vendidas,
- cumplimiento promedio,
- comportamiento mensual.

---

## 11. Análisis de negocio

`business_analysis.py` consulta PostgreSQL y automatiza la generación de:

- KPIs generales,
- ranking de ciudades,
- ranking de productos,
- ventas mensuales,
- mejores y peores resultados,
- reportes CSV,
- visualizaciones.

Los resultados se almacenan automáticamente en:

```text
reports/
images/
```

---

# Instalación

## Requisitos previos

Para ejecutar el proyecto se necesita:

- Python 3.11 o compatible.
- PostgreSQL.
- Git.
- Una base de datos PostgreSQL llamada:

```text
retail_sales_analytics
```

Los comandos deben ejecutarse desde la raíz del proyecto.

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/KleberL/retail-sales-analytics.git
cd retail-sales-analytics
```

---

## 2. Crear un entorno virtual

```bash
python -m venv .venv
```

El entorno virtual mantiene las dependencias del proyecto separadas de las librerías instaladas globalmente en el sistema.

---

## 3. Activar el entorno virtual

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo, la terminal mostrará:

```text
(.venv)
```

Si PowerShell bloquea la ejecución de `Activate.ps1`, puede habilitarse temporalmente para la sesión actual:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Luego volver a ejecutar:

```powershell
.\.venv\Scripts\Activate.ps1
```

El cambio realizado mediante `-Scope Process` solo afecta la sesión actual de PowerShell.

### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 4. Instalar dependencias

Con el entorno virtual activo:

```bash
python -m pip install -r requirements.txt
```

Las principales dependencias son:

```text
pandas==3.0.6
matplotlib==3.11.2
psycopg[binary]==3.3.8
SQLAlchemy==2.1.8
python-dotenv==1.2.4
```

Se utiliza `psycopg[binary]` para incluir los componentes necesarios para la conexión con PostgreSQL y facilitar la reproducibilidad del proyecto en entornos nuevos.

---

## 5. Configurar variables de entorno

Crear un archivo:

```text
.env
```

en la raíz del proyecto.

Puede utilizarse `.env.example` como referencia:

```text
DB_NAME=retail_sales_analytics
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

Reemplazar `your_password` por la contraseña local de PostgreSQL.

El archivo `.env` está incluido en `.gitignore` y **no debe subirse a GitHub**.

---

# Ejecución

Con PostgreSQL disponible, las variables configuradas y el entorno virtual activo, ejecutar el pipeline desde la raíz del proyecto.

## 1. Generar los datos

```bash
python -m src.generate_data
```

## 2. Revisar la calidad inicial

```bash
python -m src.check_data
```

## 3. Limpiar y transformar los datos

```bash
python -m src.clean_data
```

## 4. Validar el dataset procesado

```bash
python -m src.validate_data
```

## 5. Cargar los datos en PostgreSQL

```bash
python -m src.load_to_postgres
```

## 6. Ejecutar una consulta desde Python

```bash
python -m src.query_postgres
```

## 7. Generar el análisis de negocio

```bash
python -m src.business_analysis
```

El flujo completo es:

```text
python -m src.generate_data
          ↓
python -m src.check_data
          ↓
python -m src.clean_data
          ↓
python -m src.validate_data
          ↓
python -m src.load_to_postgres
          ↓
python -m src.query_postgres
          ↓
python -m src.business_analysis
```

---

# Archivos generados

El pipeline produce:

```text
data/raw/sales_raw.csv
data/processed/sales_clean.csv
```

Los reportes:

```text
reports/kpis_generales.csv
reports/ventas_por_ciudad.csv
reports/ventas_por_producto.csv
reports/ventas_por_mes.csv
```

Y las visualizaciones:

```text
images/ventas_por_ciudad.png
images/ventas_mensuales.png
```

---

# Ejemplo de resultados

| Producto | Unidades | Venta total | Cumplimiento promedio |
|---|---:|---:|---:|
| Nova Pro | 563 | $180,160 | 74.63% |
| Nova X2 | 506 | $116,560 | 71.88% |
| Pulse A2 | 486 | $97,200 | 83.82% |
| Nova X1 | 510 | $91,800 | 70.56% |
| Pulse A1 | 578 | $86,700 | 74.18% |

---

# Seguridad

El proyecto evita almacenar credenciales directamente dentro del código.

Las credenciales se cargan mediante:

```text
.env
      ↓
python-dotenv
      ↓
src/database.py
      ↓
PostgreSQL
```

`.env` está excluido mediante `.gitignore`.

El repositorio público solo incluye:

```text
.env.example
```

con valores de referencia.

---

# Reproducibilidad

El proyecto fue probado dentro de un entorno virtual limpio.

El flujo validado fue:

```text
Nuevo .venv
      ↓
pip install -r requirements.txt
      ↓
configuración de .env
      ↓
validación de variables
      ↓
conexión PostgreSQL
      ↓
ejecución del pipeline
      ↓
KPIs, reportes y gráficos
```

Esta prueba permitió detectar y corregir una dependencia incompleta de `psycopg`, reemplazándola por `psycopg[binary]`.

También se centralizaron las rutas mediante `pathlib` y se agregaron validaciones para detectar configuraciones incompletas antes de conectarse a PostgreSQL.

---

# Arquitectura

El proyecto separa responsabilidades entre módulos:

```text
paths.py
→ rutas y ubicaciones del proyecto

database.py
→ configuración, validación y conexiones PostgreSQL

generate_data.py
→ generación de datos

check_data.py
→ revisión inicial de calidad

clean_data.py
→ limpieza y transformación

validate_data.py
→ validación del dataset procesado

load_to_postgres.py
→ carga de datos y manejo de errores PostgreSQL

query_postgres.py
→ consultas desde Python

business_analysis.py
→ KPIs, reportes, gráficos e insights
```

Esta organización reduce código duplicado y facilita futuras mejoras.

---

# Habilidades demostradas

Este proyecto demuestra conocimientos prácticos de:

- Python.
- pandas.
- NumPy.
- limpieza y transformación de datos.
- análisis exploratorio.
- SQL.
- PostgreSQL.
- integración Python–PostgreSQL.
- SQLAlchemy.
- psycopg.
- creación de KPIs.
- análisis de negocio.
- automatización de reportes.
- visualización con Matplotlib.
- variables de entorno.
- validación de configuración.
- manejo seguro de credenciales.
- módulos y paquetes Python.
- `pathlib`.
- gestión centralizada de rutas.
- entornos virtuales.
- `try`, `except` y `finally`.
- manejo de excepciones.
- liberación de recursos.
- Git y GitHub.
- documentación técnica.
- separación de responsabilidades.
- organización de proyectos de datos.
- reproducibilidad de entornos.

---

# Estado del proyecto

El proyecto continúa en desarrollo como parte de una ruta práctica de aprendizaje en análisis de datos, ciencia de datos e ingeniería de software.

Las siguientes mejoras se incorporarán progresivamente a medida que avance el proyecto.

---

# Autor

**Kleber Landívar**

Proyecto desarrollado como parte de un portafolio profesional de análisis de datos.
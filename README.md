# Retail Sales & Inventory Analytics

![Tests](https://github.com/KleberL/retail-sales-analytics/actions/workflows/tests.yml/badge.svg)

Proyecto end-to-end de análisis de datos para un negocio minorista ficticio, enfocado en ventas, cumplimiento de objetivos, inventario y cobertura comercial.

El proyecto cubre un flujo completo de datos: generación de información sintética, control de calidad, limpieza con Python y pandas, almacenamiento en PostgreSQL, análisis con SQL, cálculo de KPIs, generación de reportes, creación automatizada de visualizaciones, pruebas automáticas, ejecución integral del pipeline e integración continua con GitHub Actions.

> **Nota:** todos los datos utilizados son sintéticos y fueron generados exclusivamente con fines educativos y de portafolio. No contienen información real de empresas, clientes o personas.

---

# Objetivo

Construir un pipeline de análisis reproducible que permita:

- Generar datos de ventas ficticios con problemas controlados de calidad.
- Simular tiendas con ventas e inventarios iguales a cero.
- Detectar valores nulos, duplicados e inconsistencias.
- Limpiar y transformar información con pandas.
- Calcular métricas derivadas de ventas, cumplimiento y cobertura.
- Evaluar cobertura comercial de forma realista.
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
- Validar automáticamente rutas, configuración y calidad de datos mediante tests.
- Ejecutar todo el pipeline automáticamente con un solo comando.
- Detener la ejecución si una etapa crítica falla.
- Medir el tiempo total de ejecución del pipeline.
- Ejecutar automáticamente los tests en GitHub después de cada `push` o Pull Request hacia `main`.
- Trabajar con ramas y Pull Requests antes de integrar cambios a `main`.

---

# Pipeline de datos

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
      ↓
Pruebas automáticas
      ↓
GitHub Actions
```

El flujo completo también puede ejecutarse mediante:

```bash
python -m src.run_pipeline
```

---

# KPIs principales

| KPI | Resultado |
|---|---:|
| Unidades vendidas | 2,184 |
| Venta total | $461,760 |
| Cumplimiento promedio | 61.69% |
| Registros que cumplen el target | 23.40% |
| Cobertura general | 93.80% |

---

# Principales insights

- **Guayaquil** presenta la mayor venta total: **$103,760**.
- **Nova Pro** es el producto con mayor venta total: **$129,280**.
- **Pulse A1** registra el mayor volumen de unidades vendidas.
- **Manta** presenta la mayor cobertura promedio: **98.17%**.
- **Agosto** es el mes con mayor venta: **$61,390**.
- **Septiembre** es el mes con menor venta: **$21,480**.
- La cobertura general del dataset es de **93.80%**.

Los resultados cambiaron respecto a versiones anteriores del proyecto porque el generador ahora permite registros con cero ventas y cero inventario.

Esto produce KPIs más realistas y evita que la cobertura quede artificialmente cercana al 100%.

Debido a que el dataset es sintético, estos resultados demuestran el proceso analítico y no deben interpretarse como tendencias reales de mercado.

---

# Lógica de cobertura

La cobertura representa si un registro tiene presencia comercial mediante ventas o inventario.

La regla utilizada es:

```text
Unidades > 0
O
Inventario > 0
        ↓
Cobertura = 1
```

Solo existe falta de cobertura cuando:

```text
Unidades = 0
Y
Inventario = 0
        ↓
Cobertura = 0
```

Ejemplos:

```text
Unidades = 0
Inventario = 8
→ Cobertura = 1
```

```text
Unidades = 4
Inventario = 0
→ Cobertura = 1
```

```text
Unidades = 0
Inventario = 0
→ Cobertura = 0
```

En el dataset actual:

```text
Cobertura = 0 → 31 registros
Cobertura = 1 → 469 registros
Total         → 500 registros
```

Por tanto:

```text
Cobertura general = 469 / 500
Cobertura general = 93.80%
```

---

# Generación realista de ventas e inventario

Anteriormente las unidades vendidas se generaban siempre entre:

```text
1 y 10
```

Eso provocaba que todos los registros tuvieran ventas y, por tanto, la cobertura fuera prácticamente siempre igual a 1.

La lógica actual permite ventas iguales a cero:

```python
units = (
    0
    if random.random() < 0.20
    else random.randint(1, 10)
)
```

Esto genera aproximadamente un **20% de probabilidad** de tener cero unidades vendidas.

El inventario utiliza:

```python
inventory = (
    0
    if random.random() < 0.30
    else random.randint(1, 20)
)
```

Esto genera aproximadamente un **30% de probabilidad** de inventario igual a cero.

La combinación de ambas condiciones permite crear registros sin cobertura de forma natural.

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
- variables de entorno
- `.gitignore`

## Organización del proyecto

- `pathlib`
- módulos Python
- paquetes Python
- entorno virtual `venv`
- separación de responsabilidades
- manejo de excepciones

## Testing

- `unittest`
- `unittest.mock`
- assertions
- pruebas de calidad de datos
- validación de reglas de negocio

## Automatización

- `subprocess`
- `sys.executable`
- `time.perf_counter`
- códigos de salida
- orquestación de procesos

## Integración continua

- GitHub Actions
- workflows YAML
- ejecución automática de tests
- runners Ubuntu

## Control de versiones

- Git
- GitHub
- ramas
- Pull Requests
- merge

---

# Estructura del proyecto

```text
retail-sales-analytics/
│
├── .github/
│   └── workflows/
│       └── tests.yml
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
│   ├── business_analysis.py
│   └── run_pipeline.py
│
├── tests/
│   ├── __init__.py
│   ├── test_paths.py
│   ├── test_database.py
│   └── test_data_quality.py
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

`generate_data.py` crea un dataset sintético de ventas con 500 registros base.

Además introduce intencionalmente problemas controlados de calidad para simular situaciones reales:

- valores nulos,
- registros duplicados,
- espacios innecesarios,
- diferencias entre mayúsculas y minúsculas,
- inconsistencias en nombres.

También genera condiciones comerciales más realistas:

- aproximadamente 20% de probabilidad de tener cero ventas,
- aproximadamente 30% de probabilidad de tener inventario igual a cero.

Después se agregan 5 duplicados intencionales.

El resultado inicial contiene:

```text
505 filas
9 columnas
```

y se almacena en:

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

El dataset procesado final contiene:

```text
500 filas
15 columnas
```

y se almacena en:

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

- cargar variables desde `.env`,
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
- cobertura,
- comportamiento mensual.

---

## 11. Análisis de negocio

`business_analysis.py` consulta PostgreSQL y automatiza la generación de:

- KPIs generales,
- cobertura general,
- ranking de ciudades,
- cobertura promedio por ciudad,
- ranking de productos,
- ventas mensuales,
- mejores y peores resultados,
- reportes CSV,
- visualizaciones.

El KPI de cobertura general se calcula mediante:

```sql
ROUND(AVG(cobertura) * 100, 2) AS cobertura_general
```

La cobertura por ciudad utiliza:

```sql
ROUND(AVG(cobertura) * 100, 2) AS cobertura_promedio
```

Los resultados se almacenan automáticamente en:

```text
reports/
images/
```

---

# Ejecución automatizada del pipeline

El proyecto incluye un orquestador en:

```text
src/run_pipeline.py
```

Este módulo permite ejecutar el pipeline completo con un solo comando:

```bash
python -m src.run_pipeline
```

El proceso ejecuta automáticamente:

```text
Generación de datos
        ↓
Control de calidad inicial
        ↓
Limpieza y transformación
        ↓
Validación
        ↓
Carga a PostgreSQL
        ↓
Consulta de PostgreSQL
        ↓
Análisis de negocio
        ↓
Tests automáticos
```

---

## Medición del tiempo

El pipeline utiliza:

```python
time.perf_counter()
```

para medir cuánto tarda la ejecución completa.

Ejemplo:

```python
start_time = time.perf_counter()

# Pipeline

elapsed_time = time.perf_counter() - start_time
```

Al finalizar muestra:

```text
Tiempo total: 10.60 segundos
```

Si una etapa falla, también puede mostrar cuánto tiempo transcurrió antes del error.

---

## Uso de subprocess

El pipeline utiliza:

```python
import subprocess
```

para ejecutar cada etapa como un proceso independiente.

Ejemplo:

```python
subprocess.run(
    command,
    cwd=PROJECT_ROOT,
    check=True,
)
```

`cwd=PROJECT_ROOT` garantiza que los comandos se ejecuten desde la raíz del proyecto.

`check=True` permite detectar automáticamente procesos que terminan con error.

---

## Uso de sys.executable

En lugar de utilizar simplemente:

```text
python
```

el pipeline utiliza:

```python
sys.executable
```

Esto permite utilizar exactamente el mismo intérprete con el que se inició el proyecto.

Si el entorno virtual está activo:

```text
(.venv)
```

se utilizará el Python del entorno virtual.

---

## Manejo de fallos del pipeline

Cuando una etapa falla, el pipeline captura:

```python
subprocess.CalledProcessError
```

y muestra:

```text
============================================================
PIPELINE DETENIDO
============================================================
Etapa con error: nombre_etapa
Código de salida: 1
Tiempo transcurrido: X.XX segundos
```

Esto evita que etapas posteriores continúen trabajando con datos incompletos o incorrectos.

---

# Pruebas automáticas

El proyecto utiliza `unittest`, incluido en la biblioteca estándar de Python.

Actualmente existen **12 tests automáticos**.

Los tests están ubicados en:

```text
tests/
```

---

## Tests de rutas

Archivo:

```text
tests/test_paths.py
```

Comprueba:

- que la raíz del proyecto exista,
- que las carpetas de datos existan,
- que las carpetas de reportes e imágenes existan,
- que `sales_raw.csv` exista,
- que `sales_clean.csv` exista.

---

## Tests de configuración

Archivo:

```text
tests/test_database.py
```

Comprueba:

- que `get_db_config()` genere correctamente la configuración esperada,
- que una variable inválida produzca un `RuntimeError`,
- que la validación funcione sin modificar el `.env` real.

Utiliza:

```python
from unittest.mock import patch
```

para simular variables de entorno.

---

## Tests de calidad de datos

Archivo:

```text
tests/test_data_quality.py
```

Comprueba automáticamente que `sales_clean.csv`:

- tenga exactamente 500 registros,
- no contenga valores nulos,
- no contenga registros duplicados,
- tenga las 15 columnas esperadas,
- conserve el orden esperado de las columnas,
- contenga valores de cobertura 0 y 1,
- aplique correctamente la regla de cobertura.

Las dos nuevas pruebas de cobertura son:

```text
test_coverage_has_zero_and_one
test_coverage_rule_is_correct
```

---

## Validación de la regla de cobertura

La prueba recalcula la cobertura de manera independiente:

```python
expected_coverage = (
    (self.df["Unidades"] > 0)
    | (self.df["Inventario"] > 0)
).astype(int)
```

Luego la compara con la columna real:

```python
coverage_is_correct = (
    self.df["Cobertura"]
    == expected_coverage
).all()
```

Finalmente:

```python
self.assertTrue(
    coverage_is_correct
)
```

Esto permite detectar automáticamente si la lógica de cobertura se rompe en el futuro.

---

## Ejecutar todos los tests

Desde la raíz del proyecto:

```bash
python -m unittest discover -s tests -v
```

Resultado actual:

```text
Ran 12 tests

OK
```

---

# Integración continua

El proyecto utiliza **GitHub Actions** para ejecutar automáticamente la suite de pruebas cada vez que se realiza un `push` o un Pull Request hacia la rama `main`.

El workflow está definido en:

```text
.github/workflows/tests.yml
```

El proceso realiza:

```text
Push / Pull Request
        ↓
GitHub Actions
        ↓
Máquina Ubuntu temporal
        ↓
Python 3.11
        ↓
Instalación de dependencias
        ↓
Ejecución de unittest
        ↓
Tests OK / Tests fallidos
```

La suite se ejecuta mediante:

```bash
python -m unittest discover -s tests -v
```

El proyecto cuenta actualmente con **12 tests automáticos**.

---

# Flujo de trabajo con ramas

Las mejoras se pueden desarrollar utilizando ramas independientes.

Ejemplo utilizado:

```text
main
  ↓
feature/pipeline-timing
  ↓
cambio
  ↓
commit
  ↓
push
  ↓
Pull Request
  ↓
GitHub Actions
  ↓
merge
  ↓
main
```

Este flujo permite validar los cambios antes de integrarlos en la rama principal.

Para la mejora actual de cobertura se utiliza:

```text
feature/realistic-coverage
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

---

## 3. Activar el entorno virtual

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la ejecución:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Luego:

```powershell
.\.venv\Scripts\Activate.ps1
```

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

```bash
python -m pip install -r requirements.txt
```

Dependencias principales:

```text
pandas==3.0.6
matplotlib==3.11.2
psycopg[binary]==3.3.8
SQLAlchemy==2.1.8
python-dotenv==1.2.4
```

---

## 5. Configurar variables de entorno

Crear:

```text
.env
```

Puede utilizarse `.env.example` como referencia:

```text
DB_NAME=retail_sales_analytics
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

El archivo `.env` está incluido en `.gitignore` y no debe subirse a GitHub.

---

# Ejecución

## Ejecución recomendada

```bash
python -m src.run_pipeline
```

Este comando ejecuta automáticamente todo el flujo principal.

---

## Ejecución manual

### Generar datos

```bash
python -m src.generate_data
```

### Revisar calidad inicial

```bash
python -m src.check_data
```

### Limpiar datos

```bash
python -m src.clean_data
```

### Validar datos

```bash
python -m src.validate_data
```

### Cargar PostgreSQL

```bash
python -m src.load_to_postgres
```

### Consultar PostgreSQL

```bash
python -m src.query_postgres
```

### Generar análisis de negocio

```bash
python -m src.business_analysis
```

### Ejecutar tests

```bash
python -m unittest discover -s tests -v
```

---

# Archivos generados

## Datos

```text
data/raw/sales_raw.csv
data/processed/sales_clean.csv
```

## Reportes

```text
reports/kpis_generales.csv
reports/ventas_por_ciudad.csv
reports/ventas_por_producto.csv
reports/ventas_por_mes.csv
```

## Visualizaciones

```text
images/ventas_por_ciudad.png
images/ventas_mensuales.png
```

---

# Ejemplo de resultados por producto

| Producto | Unidades | Venta total | Cumplimiento promedio |
|---|---:|---:|---:|
| Nova Pro | 404 | $129,280 | 58.52% |
| Nova X1 | 481 | $87,840 | 66.80% |
| Nova X2 | 368 | $84,640 | 61.82% |
| Pulse A2 | 407 | $81,400 | 63.31% |
| Pulse A1 | 524 | $78,600 | 58.25% |

---

# Ejemplo de resultados por ciudad

| Ciudad | Unidades | Venta total | Cumplimiento | Cobertura |
|---|---:|---:|---:|---:|
| Guayaquil | 470 | $103,760 | 67.22% | 95.65% |
| Manta | 490 | $101,250 | 62.72% | 98.17% |
| Cuenca | 469 | $96,010 | 58.43% | 94.64% |
| Machala | 407 | $84,380 | 65.96% | 90.32% |
| Quito | 348 | $76,360 | 54.75% | 89.36% |

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

Los tests de configuración utilizan mocking, por lo que GitHub Actions no necesita la contraseña local de PostgreSQL.

---

# Reproducibilidad

El proyecto fue probado:

- en Windows,
- dentro de un entorno virtual limpio,
- mediante ejecución completa del pipeline,
- mediante tests automáticos,
- dentro de GitHub Actions utilizando Ubuntu.

El flujo validado es:

```text
Nuevo entorno
      ↓
pip install -r requirements.txt
      ↓
configuración
      ↓
pipeline
      ↓
PostgreSQL
      ↓
KPIs y reportes
      ↓
12 tests
      ↓
GitHub Actions
```

---

# Arquitectura

El proyecto separa responsabilidades entre módulos:

```text
paths.py
→ rutas y ubicaciones del proyecto

database.py
→ configuración, validación y conexiones PostgreSQL

generate_data.py
→ generación de datos sintéticos y escenarios comerciales

check_data.py
→ revisión inicial de calidad

clean_data.py
→ limpieza, transformación y cálculo de cobertura

validate_data.py
→ validación del dataset procesado

load_to_postgres.py
→ carga de datos y manejo de errores PostgreSQL

query_postgres.py
→ consultas desde Python

business_analysis.py
→ KPIs, cobertura, reportes, gráficos e insights

run_pipeline.py
→ automatización, orquestación y medición de tiempo

tests/
→ validación automática del proyecto y reglas de negocio

.github/workflows/tests.yml
→ integración continua y ejecución automática de tests
```

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
- cobertura comercial.
- reglas de negocio.
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
- pruebas automáticas con `unittest`.
- assertions.
- `unittest.mock.patch`.
- mocking de variables de entorno.
- validación automatizada de calidad de datos.
- tests de reglas de negocio.
- automatización de pipelines.
- `subprocess`.
- `sys.executable`.
- `time.perf_counter`.
- códigos de salida de procesos.
- manejo de fallos entre procesos.
- orquestación de tareas.
- integración continua.
- GitHub Actions.
- workflows YAML.
- runners Ubuntu.
- Git.
- GitHub.
- ramas.
- Pull Requests.
- merges.
- documentación técnica.
- separación de responsabilidades.
- organización de proyectos de datos.
- reproducibilidad de entornos.

---

# Estado del proyecto

El proyecto se encuentra en una etapa avanzada de desarrollo como parte de una ruta práctica de aprendizaje en análisis de datos, ciencia de datos e ingeniería de software.

Actualmente cuenta con:

- pipeline completo de datos,
- generación de escenarios comerciales realistas,
- almacenamiento en PostgreSQL,
- análisis SQL,
- KPIs,
- cobertura comercial,
- visualizaciones,
- reportes automatizados,
- configuración segura,
- manejo de errores,
- 12 tests automáticos,
- tests específicos para reglas de cobertura,
- ejecución integral mediante un solo comando,
- medición del tiempo de ejecución,
- integración continua con GitHub Actions,
- validación automática después de cada `push`,
- flujo de trabajo basado en ramas y Pull Requests.

Las siguientes mejoras estarán orientadas al cierre y presentación final del proyecto como pieza de portafolio.

---

# Autor

**Kleber Landívar**

Proyecto desarrollado como parte de un portafolio profesional de análisis de datos.
import pandas as pd
import psycopg

from src.database import get_connection_params



# 1. Conectarse a PostgreSQL
parametros = get_connection_params()

conexion = psycopg.connect(**parametros)

print("Conexión exitosa")


# 2. Crear cursor para ejecutar SQL
cursor = conexion.cursor()


# 3. Crear la tabla si todavía no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    fecha DATE,
    anio INTEGER,
    mes INTEGER,
    ciudad VARCHAR(50),
    tienda VARCHAR(50),
    supervisor VARCHAR(100),
    producto VARCHAR(50),
    precio INTEGER,
    unidades INTEGER,
    target INTEGER,
    inventario INTEGER,
    venta_total INTEGER,
    cumplimiento NUMERIC(10,2),
    cumple_target INTEGER,
    cobertura INTEGER
);
""")

conexion.commit()

print("Tabla sales creada correctamente")


# 4. Leer el dataset limpio
df = pd.read_csv(
    "data/processed/sales_clean.csv"
)


# 5. Renombrar las columnas para PostgreSQL
df = df.rename(
    columns={
        "Fecha": "fecha",
        "Año": "anio",
        "Mes": "mes",
        "Ciudad": "ciudad",
        "Tienda": "tienda",
        "Supervisor": "supervisor",
        "Producto": "producto",
        "Precio": "precio",
        "Unidades": "unidades",
        "Target": "target",
        "Inventario": "inventario",
        "Venta_Total": "venta_total",
        "Cumplimiento": "cumplimiento",
        "Cumple_Target": "cumple_target",
        "Cobertura": "cobertura"
    }
)


# 6. Vaciar la tabla antes de volver a cargar datos
cursor.execute("DELETE FROM sales;")


# 7. Insertar las filas del DataFrame en PostgreSQL
for _, fila in df.iterrows():

    cursor.execute(
        """
        INSERT INTO sales (
            fecha,
            anio,
            mes,
            ciudad,
            tienda,
            supervisor,
            producto,
            precio,
            unidades,
            target,
            inventario,
            venta_total,
            cumplimiento,
            cumple_target,
            cobertura
        )
        VALUES (
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s
        );
        """,
        tuple(fila)
    )


# 8. Confirmar los INSERT
conexion.commit()

print("Datos cargados correctamente")
print("Filas cargadas:", len(df))


# 9. Cerrar cursor y conexión
cursor.close()
conexion.close()

print("Conexión cerrada")
import pandas as pd
import psycopg

from src.database import get_connection_params
from src.paths import CLEAN_SALES_FILE


parametros = get_connection_params()

conexion = None
cursor = None

try:
    conexion = psycopg.connect(**parametros)
    print("Conexión exitosa")

    cursor = conexion.cursor()

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

    df = pd.read_csv(CLEAN_SALES_FILE)

    df = df.rename(columns={
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
    })

    cursor.execute("""
        DELETE FROM sales;
    """)

    for _, fila in df.iterrows():
        cursor.execute("""
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
        """, tuple(fila))

    conexion.commit()

    print("Datos cargados correctamente")
    print(f"Filas cargadas: {len(df)}")

except psycopg.Error as error:
    print("Error de PostgreSQL:")
    print(error)
    raise

finally:
    if cursor is not None:
        cursor.close()

    if conexion is not None:
        conexion.close()
        print("Conexión cerrada")
import subprocess
import sys

from src.paths import PROJECT_ROOT


STEPS = [
    ("Generar datos", [sys.executable, "-m", "src.generate_data"]),
    ("Revisar calidad inicial", [sys.executable, "-m", "src.check_data"]),
    ("Limpiar datos", [sys.executable, "-m", "src.clean_data"]),
    ("Validar datos", [sys.executable, "-m", "src.validate_data"]),
    ("Cargar datos a PostgreSQL", [sys.executable, "-m", "src.load_to_postgres"]),
    ("Consultar PostgreSQL", [sys.executable, "-m", "src.query_postgres"]),
    ("Generar análisis de negocio", [sys.executable, "-m", "src.business_analysis"]),
    (
        "Ejecutar tests",
        [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            "tests",
            "-v",
        ],
    ),
]


def run_pipeline():
    print("=" * 60)
    print("INICIANDO PIPELINE")
    print("=" * 60)

    for name, command in STEPS:
        print(f"\n>>> {name}")

        try:
            subprocess.run(
                command,
                cwd=PROJECT_ROOT,
                check=True,
            )

        except subprocess.CalledProcessError as error:
            print("\n" + "=" * 60)
            print("PIPELINE DETENIDO")
            print("=" * 60)
            print(f"Etapa con error: {name}")
            print(f"Código de salida: {error.returncode}")

            sys.exit(error.returncode)

    print("\n" + "=" * 60)
    print("PIPELINE COMPLETADO CORRECTAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()
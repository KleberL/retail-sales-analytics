import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


def get_db_config():
    load_dotenv()

    config = {
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
    }

    missing = [
        name
        for name, value in config.items()
        if value is None or not value.strip()
    ]

    if missing:
        raise RuntimeError(
            "Faltan variables de entorno: "
            + ", ".join(missing)
        )

    return config


def get_engine():
    config = get_db_config()

    url = URL.create(
        drivername="postgresql+psycopg",
        username=config["user"],
        password=config["password"],
        host=config["host"],
        port=int(config["port"]),
        database=config["dbname"],
    )

    return create_engine(url)


def get_connection_params():
    return get_db_config()
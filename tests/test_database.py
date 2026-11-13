import unittest
from unittest.mock import patch

from src.database import get_db_config


class TestDatabaseConfig(unittest.TestCase):

    @patch("src.database.os.getenv")
    def test_get_db_config_returns_values(self, mock_getenv):
        variables = {
            "DB_NAME": "retail_sales_analytics",
            "DB_USER": "postgres",
            "DB_PASSWORD": "password_prueba",
            "DB_HOST": "localhost",
            "DB_PORT": "5432",
        }

        mock_getenv.side_effect = variables.get

        config = get_db_config()

        self.assertEqual(
            config,
            {
                "dbname": "retail_sales_analytics",
                "user": "postgres",
                "password": "password_prueba",
                "host": "localhost",
                "port": "5432",
            }
        )

    @patch("src.database.os.getenv")
    def test_get_db_config_raises_error_when_port_missing(
        self,
        mock_getenv
    ):
        variables = {
            "DB_NAME": "retail_sales_analytics",
            "DB_USER": "postgres",
            "DB_PASSWORD": "password_prueba",
            "DB_HOST": "localhost",
            "DB_PORT": " ",
        }

        mock_getenv.side_effect = variables.get

        with self.assertRaises(RuntimeError) as context:
            get_db_config()

        self.assertIn(
            "port",
            str(context.exception)
        )


if __name__ == "__main__":
    unittest.main()
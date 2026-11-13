import unittest

import pandas as pd

from src.paths import CLEAN_SALES_FILE


class TestDataQuality(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv(CLEAN_SALES_FILE)

    def test_processed_data_has_500_rows(self):
        self.assertEqual(
            len(self.df),
            500
        )

    def test_processed_data_has_no_nulls(self):
        total_nulls = self.df.isna().sum().sum()

        self.assertEqual(
            total_nulls,
            0
        )

    def test_processed_data_has_no_duplicates(self):
        total_duplicates = self.df.duplicated().sum()

        self.assertEqual(
            total_duplicates,
            0
        )

    def test_expected_columns_exist(self):
        expected_columns = [
            "Fecha",
            "Año",
            "Mes",
            "Ciudad",
            "Tienda",
            "Supervisor",
            "Producto",
            "Precio",
            "Unidades",
            "Target",
            "Inventario",
            "Venta_Total",
            "Cumplimiento",
            "Cumple_Target",
            "Cobertura",
        ]

        self.assertEqual(
            list(self.df.columns),
            expected_columns
        )


if __name__ == "__main__":
    unittest.main()
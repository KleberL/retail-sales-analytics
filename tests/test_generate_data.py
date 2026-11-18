import unittest

from pandas.testing import assert_frame_equal

from src.generate_data import generate_dataset


class TestGenerateDataset(unittest.TestCase):

    def test_generate_dataset_has_expected_shape(self):
        df = generate_dataset()

        self.assertEqual(
            df.shape,
            (500, 9),
        )

    def test_generate_dataset_is_reproducible(self):
        df_1 = generate_dataset(
            seed=42
        )

        df_2 = generate_dataset(
            seed=42
        )

        assert_frame_equal(
            df_1,
            df_2,
        )

    def test_generate_dataset_has_zero_sales_and_inventory(self):
        df = generate_dataset(
            seed=42
        )

        has_zero_sales = (
            df["Unidades"] == 0
        ).any()

        has_zero_inventory = (
            df["Inventario"] == 0
        ).any()

        self.assertTrue(
            has_zero_sales
        )

        self.assertTrue(
            has_zero_inventory
        )


if __name__ == "__main__":
    unittest.main()
import unittest

from src.paths import (
    PROJECT_ROOT,
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    REPORTS_DIR,
    IMAGES_DIR,
    RAW_SALES_FILE,
    CLEAN_SALES_FILE,
)


class TestPaths(unittest.TestCase):

    def test_project_root_exists(self):
        self.assertTrue(PROJECT_ROOT.exists())

    def test_data_directories_exist(self):
        self.assertTrue(DATA_DIR.exists())
        self.assertTrue(RAW_DATA_DIR.exists())
        self.assertTrue(PROCESSED_DATA_DIR.exists())

    def test_output_directories_exist(self):
        self.assertTrue(REPORTS_DIR.exists())
        self.assertTrue(IMAGES_DIR.exists())

    def test_sales_files_exist(self):
        self.assertTrue(RAW_SALES_FILE.exists())
        self.assertTrue(CLEAN_SALES_FILE.exists())

if __name__ == "__main__":
    unittest.main()
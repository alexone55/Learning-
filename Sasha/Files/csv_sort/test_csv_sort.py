from csv_sort import sort_data
from csv_sort import open_file
import unittest
import csv

class TestCSVSort(unittest.TestCase):
    def test_sort_data_if_file_var_is_not_none(self):
        with open ("file.csv") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]

        col_name = "some_col_name"
        sort_type = "some_sort_type"
        sort_data(data, col_name, sort_type)

        self.assertIsNotNone(data, "Data shouldn't be None")

    def test_sort_data_if_col_name_var_is_not_none(self):
        data = []
        col_name = "some_col_name"
        sort_type = "some_sort_type"
        sort_data(data, col_name, sort_type)

        self.assertIsNotNone(col_name, "Column name shouldn't be None")

    def test_sort_data_if_sort_type_is_not_none(self):
        data = []
        col_name = "some_col_name"
        sort_type = "some_sort_type"
        sort_data(data, col_name, sort_type)

        self.assertIsNotNone(sort_type, "Sort type shouldn't be None")
    
    def test_sort_data_if_sort_type_is_in_list(self):
        data = []
        col_name = "some_col_name"
        sort_type = "ASC"
        sort_data(data, col_name, sort_type)

        self.assertIn(sort_type, ("ASC", "DESC"), "Sort type should be ASC or DESC")

    def test_sort_data_if_file_var_is_empty(self):
        with open ("file.csv") as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
        col_name = "some_col_name"
        sort_type = "some_sort_type"
        sort_data(data, col_name, sort_type)

        self.assertIsNot(len(data), 0, "File mustn't be empty")

    def test_write_data_if_file_var_is_none(self):
        data = [] #None
        col_name = "some_col_name"
        sort_type = "some_sort_type"
        sort_data(data, col_name, sort_type)

        self.assertIsNotNone(data, "Data shouldn't be None")

if __name__ == "__main__":
    unittest.main()
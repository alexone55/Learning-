import unittest
from Alexey.Files.sort_csv.main.sort_csv import csv_reader, write_csv


class TestSortCsv(unittest.TestCase):
    def test_open_csv_file(self):
        expect_set = ['1', '2', '3', '4', '5', '6']
        actual_set = csv_reader('myfile.csv')
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_filename_and_expect_error(self):
        with self.assertRaises(FileNotFoundError) as context:
            FileNotFoundError, csv_reader("myfile1.csv")
        exception_message = str(context.exception)
        self.assertEqual("[Errno 2] No such file or directory: 'myfile1.csv'", exception_message)

    def test_write_csv_file(self):
        expect_set = ['1', '2', '3', '4', '5', '6', '7']
        write_csv(['1', '2', '3', '4', '5', '6', '7'], 'myfile_writed.csv')
        actual_set = csv_reader('myfile_writed.csv')
        self.assertEqual(expect_set, actual_set)

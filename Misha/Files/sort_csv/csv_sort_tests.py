import unittest
import csv_sort_main
from unittest.mock import patch


# 'sort_csv' and 'write_data_to_csv_file' were not tested because it has no sense, i think
class SortCSVTest(unittest.TestCase):

    @patch('builtins.input', side_effect=['wrong_path.file'])
    def test_input_file_name_with_wrong_path(self, mock_input):
        with self.assertRaises(TypeError) as context:
            csv_sort_main.input_file_name()
        exception_message = str(context.exception)
        self.assertEqual('Invalid file type: got file instead of \'csv\'.', exception_message)

    @patch('builtins.input', side_effect=['testfiles/empty.csv'])
    def test_input_file_name_with_empty_file(self, mock_input):
        with self.assertRaises(OSError) as context:
            csv_sort_main.input_file_name()
        exception_message = str(context.exception)
        self.assertEqual('File is empty.', exception_message)

    @patch('builtins.input', side_effect=['TemplateImportEmpl.csv'])
    def test_input_file_name_with_right_file(self, mock_input):
        actual_file_name = csv_sort_main.input_file_name()
        self.assertEqual(actual_file_name, 'TemplateImportEmpl.csv')

    @patch('builtins.input', side_effect=['TEXT'])
    def test_input_sort_type_with_letters(self, mock_input):
        with self.assertRaises(ValueError) as context:
            csv_sort_main.input_sort_type()
        exception_message = str(context.exception)
        self.assertEqual('Incorrect input', exception_message)

    @patch('builtins.input', side_effect=['3'])
    def test_input_sort_type_with_wrong_number(self, mock_input):
        with self.assertRaises(ValueError) as context:
            csv_sort_main.input_sort_type()
        exception_message = str(context.exception)
        self.assertEqual('Incorrect input', exception_message)

    @patch('builtins.input', side_effect=['1'])
    def test_input_sort_type_with_right_number(self, mock_input):
        expected_sort_type = csv_sort_main.input_sort_type()
        self.assertEqual(expected_sort_type, True)

    @patch('builtins.input', side_effect=['228'])
    def test_input_column_name_with_wrong_name(self, mock_input):
        with self.assertRaises(ValueError) as context:
            csv_sort_main.input_column_name(['1','2','3'])
        exception_message = str(context.exception)
        self.assertEqual('Column name is incorrect', exception_message)

    @patch('builtins.input', side_effect=['228'])
    def test_input_column_name_with_right_name(self, mock_input):
        expected_index = csv_sort_main.input_column_name(['1', '2', '3', '228'])
        self.assertEqual(expected_index, 3)



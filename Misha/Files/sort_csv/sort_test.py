import unittest
import pandas
from sort_main import sort_csv_file_by_column_name, read_from_file


class SortCSVTest(unittest.TestCase):

    def test_read_from_file_with_wrong_path(self):
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(read_from_file('Inquisitio Haereticae Pravitatis Sanctum Officium'))
        exception_message = str(context.exception)
        self.assertEqual('No such file or directory', exception_message)

    def test_read_from_file_with_right_dataframe(self):
        path = 'TemplateImportEmpl.csv'
        expected_dataframe = pandas.read_csv(path, sep=';', encoding='utf-8')
        dataframe = read_from_file(path)
        self.assertEqual(str(expected_dataframe), str(dataframe))

    def test_sort_csv_file_by_column_name(self):
        path = 'TemplateImportEmpl.csv'
        dataframe = pandas.read_csv(path, sep=';', encoding='utf-8')
        column_names = dataframe.columns
        expected_dataframe = dataframe.sort_values(column_names[1], kind='mergesort').reset_index(drop=True)
        print(expected_dataframe)
        sort_csv_file_by_column_name(dataframe, column_names[1], path)
        dataframe = pandas.read_csv(path, sep=';', encoding='utf-8')
        print(dataframe)
        self.assertEqual(str(expected_dataframe), str(dataframe))

    def test_sort_csv_file_by_column_name_with_wrong_coloumn_name(self):
        path = 'TemplateImportEmpl.csv'
        dataframe = pandas.read_csv(path, sep=';', encoding='utf-8')
        with self.assertRaises(KeyError) as context:
            self.assertRaises(sort_csv_file_by_column_name(dataframe, 'wrong_coloumn', path))
        exception_message = str(context.exception)
        self.assertEqual('', exception_message)


if __name__ == '__main__':
    unittest.main()

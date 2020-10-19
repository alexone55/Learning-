import unittest
from pdf_converter_main import read_from_file, change_format_to_pdf


class PDFConverterTest(unittest.TestCase):

    def test_read_from_file_with_wrong_path(self):
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(FileNotFoundError, read_from_file('path/to/file/'))
        exception_message = str(context.exception)
        self.assertEqual('No such file or directory', exception_message)

    def test_read_from_file_with_right_path(self):
        text = read_from_file('test_file.ibc')
        expected_value = 'text128281488'
        self.assertEqual(expected_value, text)

    def test_change_format_to_pdf_with_wrong_path(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, change_format_to_pdf('path/to/file/'))
        exception_message = str(context.exception)
        self.assertEqual('Not path given', exception_message)

    def test_change_format_to_pdf_with_right_path(self):
        path = change_format_to_pdf('path.txt')
        expected_value = 'path.pdf'
        self.assertEqual(expected_value, path)


if __name__ == '__main__':
    unittest.main()

import unittest
import os
from pdf_converter_main import read_from_file, change_format_to_pdf, convert_to_pdf


class PDFConverterTest(unittest.TestCase):

    def test_read_from_file_with_right_path(self):
        text = read_from_file('test_file.ibc')
        expected_value = 'text128281488'
        self.assertEqual(expected_value, text)

    def test_change_format_to_pdf_with_wrong_path(self):
        with self.assertRaises(TypeError) as context:
            change_format_to_pdf('path/to/file/')
        exception_message = str(context.exception)
        self.assertEqual('Not path given', exception_message)

    def test_change_format_to_pdf_with_right_path(self):
        path = change_format_to_pdf('path.txt')
        expected_value = 'path.pdf'
        self.assertEqual(expected_value, path)

    def test_create_pdf_with_long_string_without_blanks(self):
        text = read_from_file('longstr.txt')
        path_to_pdf = change_format_to_pdf('longstr.txt')
        convert_to_pdf(text, path_to_pdf)
        expected_answer = True
        if os.path.exists(path_to_pdf):
            actual_answer = True
        else:
            actual_answer = False
        self.assertEqual(expected_answer, actual_answer)


if __name__ == '__main__':
    unittest.main()

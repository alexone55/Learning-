import unittest
from Alexey.Files.PDF_generator.main.PDF_generator import txt_file_reader, pdf_file_writer, main
from unittest.mock import patch


class TestPdfGenerator(unittest.TestCase):
    def test_open_txt_file_and_get_text(self):
        expect_set = "Any string in english from txt"
        actual_set = txt_file_reader("test_resource/myfile.txt")
        self.assertEqual(expect_set, actual_set)

    def test_open_html_file_and_get_text(self):
        expect_set = "Any string in english from html"
        actual_set = txt_file_reader("test_resource/myfile.html")
        self.assertEqual(expect_set, actual_set)

    def test_open_ibc_file_and_get_text(self):
        expect_set = "Any string in english from ibc"
        actual_set = txt_file_reader("test_resource/myfile.ibc")
        self.assertEqual(expect_set, actual_set)

    def test_open_wrong_file_and_expect_error(self):
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(FileNotFoundError, txt_file_reader("wrong_file.txt"))
        exception_message = str(context.exception)
        self.assertEqual("[Errno 2] No such file or directory: 'wrong_file.txt'", exception_message)

    def test_add_text_file_and_get_few_pages_in_pdf(self):
        with open('test_resource/generated_text.txt', 'r') as object_from_txt:
            text_from_txt = object_from_txt.read()
        pdf_file_writer(text_from_txt)

    def test_add_big_single_line_and_get_normal_pdf(self):
        with open('test_resource/big_single_line_text', 'r') as object_from_txt:
            text_from_txt = object_from_txt.read()
        pdf_file_writer(text_from_txt)

    @patch('builtins.input', return_value="test_resource/myfile.txt")
    def test_input_file_name_and_expect_normal_programm_work(self, mock_input):
        main()


import unittest
from Alexey.Files.PDF_generator.main.PDF_generator import txt_file_reader, pdf_file_writer
import fpdf

class TestPdfGenerator(unittest.TestCase):
    def test_open_txt_file_and_get_text(self):
        expect_set = "Any string in english from txt"
        actual_set = txt_file_reader("myfile.txt")
        self.assertEqual(expect_set, actual_set)

    def test_open_html_file_and_get_text(self):
        expect_set = "Any string in english from html"
        actual_set = txt_file_reader("myfile.html")
        self.assertEqual(expect_set, actual_set)

    def test_open_ibc_file_and_get_text(self):
        expect_set = "Any string in english from ibc"
        actual_set = txt_file_reader("myfile.ibc")
        self.assertEqual(expect_set, actual_set)

    def test_open_wrong_file_and_expect_error(self):
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(FileNotFoundError, txt_file_reader("wrong_file.txt"))
        exception_message = str(context.exception)
        self.assertEqual("[Errno 2] No such file or directory: 'wrong_file.txt'", exception_message)

    def test_add_big_line_file_and_get_text(self):
        expect_set = "Any string in english from txt"
        actual_set = pdf_file_writer("onebigsinglelinetoaddinpdf-------------------------------111111111111112222222222222222222222222")
        self.assertEqual(expect_set, actual_set)
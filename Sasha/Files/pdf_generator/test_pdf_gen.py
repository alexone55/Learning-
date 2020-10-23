from pdf_gen import open_text_file
from fpdf import FPDF
import unittest

class TestPDFGen(unittest.TestCase):
    def test_open_text_file_and_get_data(self):
        expected_result = "PLA1471C"
        current_result = open_text_file("sample.txt")
        self.assertIn(expected_result, current_result[0]) # check first value in file as list

    def test_check_if_file_exists(self):
        with self.assertRaises(FileNotFoundError):
            open_text_file("sample1.txt")

        #with self.assertRaises(FileNotFoundError) as context:
        #    open_text_file("sample1.txt")
        #self.assertTrue('No such file' in str(context.exception))

if __name__ == "__main__":
    unittest.main()
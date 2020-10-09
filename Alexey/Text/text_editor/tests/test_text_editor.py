import unittest
from Alexey.Text.text_editor.main.text_editor import *


class TestTextEditor(unittest.TestCase):

    def test_write_normal_text_and_expect_file_with_text(self):
        expect_set = "Awesome!"
        some_text = "Awesome!"
        write_file(some_text)
        self.assertEqual(expect_set, check_file())

    def test_append_normal_text_and_expect_file_with_appended_text(self):
        expect_set = "Awesome!"
        some_text = "Awesome!"
        edit_file(some_text)
        self.assertEqual(expect_set, check_file())

    def test_send_int_to_write_function_and_expect_file_with_text(self):
        expect_set = "12"
        some_text = 12
        write_file(some_text)
        self.assertEqual(expect_set, check_file())

    def test_send_int_to_write_function_and_expect_file_with_appended_text(self):
        expect_set = "Awesome!12"
        some_text = 12
        edit_file(some_text)
        self.assertEqual(expect_set, check_file())
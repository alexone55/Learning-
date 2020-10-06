import unittest
from Alexey.Text.text_editor.main.text_editor import *


class TestTextEditor(unittest.TestCase):
    def test_write_normal_text_and_expect_file_with_text(self):
        expect_set = "Awesome!"
        some_text = "Awesome!"
        write_file(some_text)
        self.assertEqual(expect_set, check_file())

    def test_append_normal_text_and_expect_file_with_appended_text(self):
        expect_set = "Awesome!Awesome!"
        some_text = "Awesome!"
        edit_file(some_text)
        self.assertEqual(expect_set, check_file())

    def test_send_wrong_type_of_data_to_write_function_and_expect_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, write_file(12))
        exception_message = str(context.exception)
        self.assertEqual('write() argument must be str, not int', exception_message)

    def test_send_wrong_type_of_data_to_edit_function_and_expect_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, edit_file(12))
        exception_message = str(context.exception)
        self.assertEqual('write() argument must be str, not int', exception_message)
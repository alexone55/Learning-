import unittest
from main import check_input_data_format


class InputTest(unittest.TestCase):

    def test_input_with_string_startet_with_zero(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, check_input_data_format('01003012'))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)

    def test_input_with_string_with_not_only_digits(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, check_input_data_format('0hb32'))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)

    def test_input_with_big_right_value(self):
        str_value = '12345'
        check_input_data_format(str_value)
        int_value = int(str_value)
        self.assertEqual(int_value, 12345)

    def test_input_with_zero(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, check_input_data_format('0'))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)

    def test_input_with_right_value(self):
        str_value = '7'
        check_input_data_format(str_value)
        int_value = int(str_value)
        self.assertEqual(int_value, 7)

    def test_input_with_empty_string(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, check_input_data_format(''))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)

    def test_input_with_none_type_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, check_input_data_format(None))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)


if __name__ == '__main__':
    unittest.main()

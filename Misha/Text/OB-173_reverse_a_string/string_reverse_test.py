import unittest
from string_reverse import string_reverser


class StringReverserTest(unittest.TestCase):

    def test_string_reverser_with_none_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, string_reverser(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_string_reverser_with_int_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, string_reverser(123))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_string_reverser_with_list_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, string_reverser(['1', '2', '3', '4']))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_string_reverser_with_empty_string(self):
        reversed_string = string_reverser('')
        expected_value = ''
        self.assertEqual(expected_value, reversed_string)

    def test_string_reverser_with_special_symbol(self):
        reversed_string = string_reverser('\n')
        expected_value = '\n'
        self.assertEqual(expected_value, reversed_string)

    def test_string_reverser_with_set_of_special_symbols(self):
        reversed_string = string_reverser('\n\t')
        expected_value = '\t\n'
        self.assertEqual(expected_value, reversed_string)

    # почему проходит этот тест?
    def test_string_reverser_with_set_of_special_symbols_2(self):
        reversed_string = string_reverser('\0\n\t')
        expected_value = '\t\n\0'
        self.assertEqual(expected_value, reversed_string)

    def test_string_reverser_with_mirrored_special_symbols(self):
        reversed_string = string_reverser('\\0\\n\\t')
        expected_value = 't\\n\\0\\'
        self.assertEqual(expected_value, reversed_string)

    def test_string_reverser_with_mirrored_special_symbols_2(self):
        reversed_string = string_reverser('\\0')
        expected_value = '0\\'
        self.assertEqual(expected_value, reversed_string)

    def test_string_reverser_with_zero_terminator(self):
        reversed_string = string_reverser('\0')
        expected_value = '\0'
        self.assertEqual(expected_value, reversed_string)

    def test_string_reverser_with_default_string(self):
        reversed_string = string_reverser('string')
        expected_value = 'gnirts'
        self.assertEqual(expected_value, reversed_string)


if __name__ == '__main__':
    unittest.main()

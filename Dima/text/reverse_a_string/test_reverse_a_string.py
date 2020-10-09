import unittest
from Dima.text.reverse_a_string.reverse_a_string import reverse_a_string


class TestReverseString(unittest.TestCase):

    def test_reverse_a_string_with_none_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, reverse_a_string(None))
        exception_message = str(context.exception)
        self.assertEqual('input isn`t str type: ', exception_message)

    def test_reverse_a_string_with_int_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, reverse_a_string(123))
        exception_message = str(context.exception)
        self.assertEqual('input isn`t str type: ', exception_message)

    def test_reverse_a_string_with_list_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, reverse_a_string(['1', '2', '3', '4']))
        exception_message = str(context.exception)
        self.assertEqual('input isn`t str type: ', exception_message)

    def test_reverse_a_string_with_empty_string(self):
        reversed_string = reverse_a_string('')
        expected_value = ''
        self.assertEqual(expected_value, reversed_string)

    def test_reverse_a_string_with_special_symbol(self):
        reversed_string = reverse_a_string('\n')
        expected_value = '\n'
        self.assertEqual(expected_value, reversed_string)

    def test_reverse_a_string_with_set_of_special_symbols(self):
        reversed_string = reverse_a_string('\n\t')
        expected_value = '\t\n'
        self.assertEqual(expected_value, reversed_string)

    def test_reverse_a_string_with_set_of_special_symbols_2(self):
        reversed_string = reverse_a_string('\0\n\t')
        expected_value = '\t\n\0'
        self.assertEqual(expected_value, reversed_string)

    def test_reverse_a_string_with_mirrored_special_symbols(self):
        reversed_string = reverse_a_string('\\0\\n\\t')
        expected_value = 't\\n\\0\\'
        self.assertEqual(expected_value, reversed_string)

    def test_reverse_a_string_with_mirrored_special_symbols_2(self):
        reversed_string = reverse_a_string('\\0')
        expected_value = '0\\'
        self.assertEqual(expected_value, reversed_string)

    def test_reverse_a_string_with_zero_terminator(self):
        reversed_string = reverse_a_string('\0')
        expected_value = '\0'
        self.assertEqual(expected_value, reversed_string)

    def test_reverse_a_string_with_default_string(self):
        reversed_string = reverse_a_string('abcde')
        expected_value = 'edcba'
        self.assertEqual(expected_value, reversed_string)


if __name__ == '__main__':
    unittest.main()

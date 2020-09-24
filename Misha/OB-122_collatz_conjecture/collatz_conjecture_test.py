import unittest
from collatz_conjecture import collatz_conjecture


class CollatzConjectureTest(unittest.TestCase):

    def test_cc_with_string_started_with_zero(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, collatz_conjecture('01003012'))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)

    def test_cc_with_string_with_not_only_digits(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, collatz_conjecture('0hb32'))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)

    def test_cc_with_right_value(self):
        iterations = collatz_conjecture('12')
        expected_value = 9
        self.assertEqual(expected_value, iterations)

    def test_cc_with_value_one(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, collatz_conjecture('1'))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)

    def test_cc_with_right_value_2(self):
        iterations = collatz_conjecture('7')
        expected_value = 16
        self.assertEqual(expected_value, iterations)

    def test_cc_with_right_value_3(self):
        iterations = collatz_conjecture('2')
        expected_value = 1
        self.assertEqual(expected_value, iterations)

    def test_cc_with_empty_string(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, collatz_conjecture(''))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)

    def test_cc_with_none_type_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, collatz_conjecture(None))
        exception_message = str(context.exception)
        self.assertEqual('Invalid data format', exception_message)


if __name__ == '__main__':
    unittest.main()

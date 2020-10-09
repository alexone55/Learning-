import unittest
from Alexey.Text.fizz_buzz.main.fizz_buzz import fizzbuzz_printer


class TestFizzBuzz(unittest.TestCase):
    def test_send_5_number_and_expect_normal_response(self):
        expect_set = 'Buzz'
        actual_set = fizzbuzz_printer(5)
        self.assertEqual(expect_set, actual_set)

    def test_send_20_number_and_expect_normal_response(self):
        expect_set = 'FizzBuzz'
        actual_set = fizzbuzz_printer(15)
        self.assertEqual(expect_set, actual_set)

    def test_send_2_number_and_expect_not_fizzbuzz(self):
        expect_set = 'Not FizzBuzz'
        actual_set = fizzbuzz_printer(2)
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_type_of_data_and_expect_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, fizzbuzz_printer("hello"))
        exception_message = str(context.exception)
        self.assertEqual('not all arguments converted during string formatting', exception_message)

    def test_send_none_and_expect_none_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, fizzbuzz_printer(None))
        exception_message = str(context.exception)
        self.assertEqual("unsupported operand type(s) for %: 'NoneType' and 'int'", exception_message)

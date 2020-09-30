import unittest
from Alexey.Text.fizz_buzz.main.fizz_buzz import fizzbuzz_cycle


class TestFizzBuzz(unittest.TestCase):
    def test_send_5_number_and_expect_normal_response(self):
        expect_set = [1, 2, 'Fizz', 4, 'Buzz']
        actual_set = fizzbuzz_cycle(5)
        self.assertEqual(expect_set, actual_set)

    def test_send_20_number_and_expect_normal_response(self):
        expect_set = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz']
        actual_set = fizzbuzz_cycle(20)
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_type_of_data_and_expect_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, fizzbuzz_cycle("hello"))
        exception_message = str(context.exception)
        self.assertEqual('can only concatenate str (not "int") to str', exception_message)

    def test_send_none_and_expect_none_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, fizzbuzz_cycle(None))
        exception_message = str(context.exception)
        self.assertEqual("unsupported operand type(s) for +: 'NoneType' and 'int'", exception_message)

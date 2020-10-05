import unittest
from Dima.text.fizz_buzz.fizz_buzz import cycle_fizzbuzz


class FizzBuzzTest(unittest.TestCase):

    def test_when_input_is_None(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, cycle_fizzbuzz(None))
        exception_message = str(context.exception)
        self.assertEqual('Number isn`t int type: ', exception_message)

    def test_when_input_str(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, cycle_fizzbuzz(None))
        exception_message = str(context.exception)
        self.assertEqual('Number isn`t int type: ', exception_message)

    def test_when_input_zero(self):
        fizzbuzz = cycle_fizzbuzz(0)
        expected_results = ['FizzBuzz']
        self.assertEqual(fizzbuzz, expected_results)

    def test_when_input_is_negative(self):
        output = cycle_fizzbuzz(-100)
        expected_results = []
        self.assertEqual(output, expected_results)

    def test_when_input_is_normal(self):
        output = cycle_fizzbuzz(10)
        expected_results = ['FizzBuzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
        self.assertEqual(output, expected_results)


if __name__ == '__main__':
    unittest.main()

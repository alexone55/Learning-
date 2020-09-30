import unittest
from fizz_buzz_main import fizz_buzz


class StringReverserTest(unittest.TestCase):

    def test_fizz_buzz_with_none_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, fizz_buzz(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_fizz_buzz_with_string_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, fizz_buzz('123'))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_fizz_buzz_with_list_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, fizz_buzz(['1', '2', '3', '4']))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_fizz_buzz_with_int_5(self):
        answer = fizz_buzz(5)
        expected_value = 'Buzz'
        self.assertEqual(expected_value, answer)

    def test_fizz_buzz_with_int_3(self):
        answer = fizz_buzz(3)
        expected_value = 'Fizz'
        self.assertEqual(expected_value, answer)

    def test_fizz_buzz_with_int_30(self):
        answer = fizz_buzz(30)
        expected_value = 'FizzBuzz'
        self.assertEqual(expected_value, answer)

    def test_fizz_buzz_with_int_2(self):
        answer = fizz_buzz(2)
        expected_value = 2
        self.assertEqual(expected_value, answer)


if __name__ == '__main__':
    unittest.main()

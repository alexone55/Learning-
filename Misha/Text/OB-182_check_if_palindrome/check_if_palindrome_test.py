import unittest
from palindrome import check_if_palindrome


class CheckIfPalindromeTest(unittest.TestCase):

    def test_check_if_palindrome_with_none_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, check_if_palindrome(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_check_if_palindrome_with_int_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, check_if_palindrome(123))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_check_if_palindrome_with_list_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, check_if_palindrome(['1', '2', '3', '4']))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_check_if_palindrome_with_empty_string(self):
        given_answer = check_if_palindrome('')
        expected_value = True
        self.assertEqual(expected_value, given_answer)

    def test_check_if_palindrome_with_palindrome(self):
        given_answer = check_if_palindrome('stringnirts')
        expected_value = True
        self.assertEqual(expected_value, given_answer)

    def test_check_if_palindrome_with_not_palindrome(self):
        given_answer = check_if_palindrome('1234qwert')
        expected_value = False
        self.assertEqual(expected_value, given_answer)

    def test_check_if_palindrome_with_palindrome_2(self):
        given_answer = check_if_palindrome('stringgnirts')
        expected_value = True
        self.assertEqual(expected_value, given_answer)


if __name__ == '__main__':
    unittest.main()

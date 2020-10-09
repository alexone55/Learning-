import unittest
from Dima.text.check_if_palindrome.check_if_palindrome import check_if_palindrome


class TestCheckPalindrome(unittest.TestCase):

    def test_when_check_if_palindrome_input_palindrome(self):
        palindrome = check_if_palindrome('abccba')
        expected_result = True
        self.assertEqual(palindrome, expected_result)

    def test_when_check_if_palindrome_input_palindrome_phrase(self):
        palindrome = check_if_palindrome('a bc    \t c ba ')
        expected_result = True
        self.assertEqual(palindrome, expected_result)

    def test_when_check_if_palindrome_input_nonpalindrome(self):
        palindrome = check_if_palindrome('abcsdf cba')
        expected_result = False
        self.assertEqual(palindrome, expected_result)

    def test_when_check_if_palindrome_input_None(self):
        with self.assertRaises(AttributeError) as context:
            self.assertRaises(AttributeError, check_if_palindrome(None))
        exception_message = str(context.exception)
        self.assertEqual('Input isn`t string type', exception_message)

    def test_when_check_if_palindrome_input_int(self):
        with self.assertRaises(AttributeError) as context:
            self.assertRaises(AttributeError, check_if_palindrome(1))
        exception_message = str(context.exception)
        self.assertEqual('Input isn`t string type', exception_message)

    def test_when_check_if_palindrome_input_list(self):
        with self.assertRaises(AttributeError) as context:
            self.assertRaises(AttributeError, check_if_palindrome(['abccba', '123321']))
        exception_message = str(context.exception)
        self.assertEqual('Input isn`t string type', exception_message)




if __name__ == '__main__':
    unittest.main()

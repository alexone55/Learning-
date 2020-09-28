import unittest
from Alexey.Text.check_if_palindrome.main.check_if_palindrome import check_if_palindrome


class GeneratingDotsTest(unittest.TestCase):
    def test_send_sentence_and_expect_palindrome_message(self):
        expect_set = "Congrats your sentence is palindrome!"
        actual_set = check_if_palindrome('Racecar')
        self.assertEqual(expect_set, actual_set)

    def test_send_sentence_and_expect_nonpalindron_message(self):
        expect_set = "This is not palindrome=("
        actual_set = check_if_palindrome('Hitman')
        self.assertEqual(expect_set, actual_set)

    def test_send_numbers_as_palindrome_and_expect_palindrome_message(self):
        expect_set = "Congrats your sentence is palindrome!"
        actual_set = check_if_palindrome('02/02/2020')
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_type_of_data_and_expect_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, check_if_palindrome(12))
        exception_message = str(context.exception)
        self.assertEqual('expected string or bytes-like object', exception_message)



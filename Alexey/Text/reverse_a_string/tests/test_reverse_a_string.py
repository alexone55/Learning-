import unittest
from Alexey.Text.reverse_a_string.main.reverse_a_string import reverse


class TestReverseAString(unittest.TestCase):
    def test_send_sentence_and_expect_palindrome_message(self):
        expect_set = "racecaR"
        actual_set = reverse('Racecar')
        self.assertEqual(expect_set, actual_set)

    def test_send_numbers_as_palindrome_and_expect_palindrome_message(self):
        expect_set = "0202/20/20"
        actual_set = reverse('02/02/2020')
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_type_data_and_expext_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, reverse(12))
        exception_message = str(context.exception)
        self.assertEqual("'int' object is not subscriptable", exception_message)


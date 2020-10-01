import unittest
from Alexey.Text.count_vowels.main.count_vowels import vowel_counter


class TestCountVowels(unittest.TestCase):
    def test_send_normal_sentence_and_expect_count_vowels(self):
        expect_set = 21
        actual_set = vowel_counter('Captain Cold and his hotheaded partner Heat Wave plot to steal a')
        self.assertEqual(expect_set, actual_set)

    def test_send_sentence_with_symbols_and_numbers_and_expect_normal_vowels_count(self):
        expect_set = 4
        actual_set = vowel_counter('Blade Runner - 2049')
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_type_of_data_and_expect_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, vowel_counter(12))
        exception_message = str(context.exception)
        self.assertEqual("'int' object is not iterable", exception_message)


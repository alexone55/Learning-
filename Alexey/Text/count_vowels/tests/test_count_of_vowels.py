import unittest
from Alexey.Text.count_vowels.main.count_vowels import vowel_counter


class TestCountVowels(unittest.TestCase):
    def test_send_normal_sentence_and_expect_count_vowels(self):
        expect_set = 'Char A is: 9| Char E is : 6| Char I is : 2| Char O is : 4| Char U is : 0| Total: 21'
        actual_set = vowel_counter('Captain Cold and his hotheaded partner Heat Wave plot to steal a')
        self.assertEqual(expect_set, actual_set)

    def test_send_sentence_with_symbols_and_numbers_and_expect_normal_vowels_count(self):
        expect_set = 'Char A is: 1| Char E is : 2| Char I is : 0| Char O is : 0| Char U is : 1| Total: 4'
        actual_set = vowel_counter('Blade Runner - 2049')
        self.assertEqual(expect_set, actual_set)

    def test_send_numeric_type_of_data_and_expect_no_vowel_message(self):
        expect_set = 'There is no vowels here'
        actual_set = vowel_counter(12)
        self.assertEqual(expect_set, actual_set)


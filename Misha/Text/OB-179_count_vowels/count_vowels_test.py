import unittest
from count_vowels_main import count_vowels


class CheckIfPalindromeTest(unittest.TestCase):

    def test_count_vowels_with_none_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, count_vowels(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_ccount_vowels_with_int_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, count_vowels(123))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_count_vowels_with_list_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, count_vowels(['1', '2', '3', '4']))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_count_vowels_with_empty_vowel_string(self):
        given_answer = count_vowels('1234567890')
        expected_value = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        self.assertEqual(expected_value, given_answer)

    def test_count_vowels_with_string_with_one_vowel(self):
        given_answer = count_vowels('string')
        expected_value = {'a': 0, 'e': 0, 'i': 1, 'o': 0, 'u': 0}
        self.assertEqual(expected_value, given_answer)

    def test_count_vowels_with_all_vowels(self):
        given_answer = count_vowels('aeiou')
        expected_value = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        self.assertEqual(expected_value, given_answer)

    def test_count_vowels_with_long_string(self):
        given_answer = count_vowels('Lorem ipsum dolor sit amet, consectetur adipiscing elit')
        expected_value = {'a': 2, 'e': 5, 'i': 6, 'o': 4, 'u': 2}
        self.assertEqual(expected_value, given_answer)


if __name__ == '__main__':
    unittest.main()

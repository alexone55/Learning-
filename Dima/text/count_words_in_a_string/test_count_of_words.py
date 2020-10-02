import unittest
from Dima.text.count_words_in_a_string.count_of_words import count_of_words_input
from Dima.text.count_words_in_a_string.count_of_words import count_of_words_str
from Dima.text.count_words_in_a_string.count_of_words import count_of_words_text


class CountWordsTest(unittest.TestCase):

    def test_count_words_with_none_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, count_of_words_input(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_count_words_with_list_value(self):
        with self.assertRaises(AttributeError) as context:
            self.assertRaises(AttributeError, count_of_words_input([1, '234', '34', 'dafgdsg', 'sdgfts']))
        exception_message = str(context.exception)
        self.assertEqual('AttributeError, The text contains invalid symbols', exception_message)

    def test_count_words_with_digit_value(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, count_of_words_input(3))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_count_words_with_empty_string(self):
        amount_of_words = count_of_words_str('')
        expected_value = 0
        self.assertEqual(expected_value, amount_of_words)

    def test_count_words_with_right_value(self):
        amount_of_words = count_of_words_str('asdfadsf asdfasdfasdf sadfadf')
        expected_value = 3
        self.assertEqual(expected_value, amount_of_words)


if __name__ == '__main__':
    unittest.main()

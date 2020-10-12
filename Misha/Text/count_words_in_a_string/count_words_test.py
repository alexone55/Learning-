import unittest
from Misha.Text.count_words_in_a_string.count_words_in_a_string import count_words,read_from_file


class CountWordsTest(unittest.TestCase):

    def test_count_words_with_none_value(self):
        with self.assertRaises(AttributeError) as context:
            self.assertRaises(AttributeError, count_words(None))
        exception_message = str(context.exception)
        self.assertEqual('AttributeError', exception_message)

    def test_count_words_with_list_value(self):
        with self.assertRaises(AttributeError) as context:
            self.assertRaises(AttributeError, count_words([1, 2, '34', 'lorem', 'ipsum']))
        exception_message = str(context.exception)
        self.assertEqual('AttributeError', exception_message)

    def test_count_words_with_digit_value(self):
        with self.assertRaises(AttributeError) as context:
            self.assertRaises(AttributeError, count_words(1488))
        exception_message = str(context.exception)
        self.assertEqual('AttributeError', exception_message)

    def test_count_words_with_empty_string(self):
        amount_of_words = count_words('')
        expected_value = 0
        self.assertEqual(expected_value, amount_of_words)

    def test_count_words_with_right_value(self):
        amount_of_words = count_words('123 124 43 ')
        expected_value = 0
        self.assertEqual(expected_value, amount_of_words)

    def test_count_words_with_right_value_2(self):
        amount_of_words = count_words('lorem ipsum dolor ')
        expected_value = 3
        self.assertEqual(expected_value, amount_of_words)

    def test_count_words_with_right_value_3(self):
        amount_of_words = count_words('lorem ipsum dolor 1234')
        expected_value = 3
        self.assertEqual(expected_value, amount_of_words)

    def test_count_words_with_right_value_4(self):
        text = read_from_file('2600-0.txt')
        amount_of_words = count_words(text)
        expected_value = 514664
        self.assertEqual(expected_value, amount_of_words)


if __name__ == '__main__':
    unittest.main()

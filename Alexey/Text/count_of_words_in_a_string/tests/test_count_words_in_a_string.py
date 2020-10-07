import unittest
from Alexey.Text.count_of_words_in_a_string.main.count_words_in_a_string import words_counter


class TestCountWordsInAString(unittest.TestCase):

    def test_send_normal_sentence_and_expect_count_words(self):
        expect_set = 2
        actual_set = words_counter('Captain Cold')
        self.assertEqual(expect_set, actual_set)

    def test_send_sentences_with_numbers_and_symbols_and_expect_count_words(self):
        expect_set = 2
        actual_set = words_counter('Captain Cold 2 ?')
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_type_of_data_and_expect_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, words_counter(13))
        exception_message = str(context.exception)
        self.assertEqual('expected string or bytes-like object', exception_message)

    def test_send_war_and_peace_and_expect_count_of_words(self):
        text = open("war_and_peace.txt", "r")
        count = words_counter(text.read())
        print(count)
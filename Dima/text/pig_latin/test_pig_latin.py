import unittest
from Dima.text.pig_latin.pig_latin import word_to_pig_latin


class TestPigLatin(unittest.TestCase):

    def test_send_none_and_expect_attribute_error(self):
        with self.assertRaises(TypeError) as context:
            word_to_pig_latin(None)
        exception_message = str(context.exception)
        self.assertEqual('Word isn`t string type: ', exception_message)

    def test_send_number_and_expect_attribute_error(self):
        with self.assertRaises(TypeError) as context:
            word_to_pig_latin(1)
        exception_message = str(context.exception)
        self.assertEqual("Word isn`t string type: ", exception_message)

    def test_send_special_symbols_and_return_value_error(self):
        with self.assertRaises(ValueError) as context:
            word_to_pig_latin('google.com')
        exception_message = str(context.exception)
        self.assertEqual('Word contains symbols: ', exception_message)

    def test_send_sentence_and_expect_pig_latin_translate(self):
        expect_set = "Ananabay"
        input_sentence = word_to_pig_latin(str("Banana"))
        self.assertEqual(expect_set, input_sentence)


if __name__ == '__main__':
    unittest.main()
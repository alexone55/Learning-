import unittest
from Alexey.Text.pig_latin.main.pig_latin import translater


class TestPigLatin(unittest.TestCase):

    def test_send_none_and_expect_attribute_error(self):
        with self.assertRaises(AttributeError) as context:
            self.assertRaises(AttributeError, translater(None))
        exception_message = str(context.exception)
        self.assertEqual('AttributeError', exception_message)

    def test_send_sentence_and_expect_pig_latin_translate(self):
        expect_set = "ityay isyay igpay atinlay entencesay esttay"
        input_sentence = translater(str("It is pig latin sentence test"))
        self.assertEqual(expect_set, input_sentence)

    def test_send_special_symbols_and_return_normal_translation(self):
        expect_set = "ayay roupgay ofyay ordsway usuallyyay ontainingcay ayay erbvay hattay expressesyay ayay houghttay inyay hetay ormfay ofyay ayay tatementsay"
        actual_set = translater("a group of words, usually containing a verb, that expresses a thought in the form of a statement")
        self.assertEqual(expect_set, actual_set)

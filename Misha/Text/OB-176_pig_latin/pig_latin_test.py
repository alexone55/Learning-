import unittest
from pig_latin_main import pig_latin_transformation


class PigLatinTest(unittest.TestCase):

    def test_pig_latin_with_sentence(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, pig_latin_transformation('Inquisitio Haereticae Pravitatis Sanctum Officium'))
        exception_message = str(context.exception)
        self.assertEqual('Not a word given', exception_message)

    def test_pig_latin_with_int(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, pig_latin_transformation(1234))
        exception_message = str(context.exception)
        self.assertEqual('Not a word given', exception_message)

    def test_pig_latin(self):
        given_answer = pig_latin_transformation('banana')
        expected_value = 'ananabay'
        self.assertEqual(expected_value, given_answer)

    def test_ceasar_ciphres_2(self):
        given_answer = pig_latin_transformation('three')
        expected_value = 'eethray'
        self.assertEqual(expected_value, given_answer)

    def test_ceasar_ciphres_3(self):
        given_answer = pig_latin_transformation('example')
        expected_value = 'exampleay'
        self.assertEqual(expected_value, given_answer)

    def test_ceasar_ciphres_4(self):
        given_answer = pig_latin_transformation('star')
        expected_value = 'arstay'
        self.assertEqual(expected_value, given_answer)


if __name__ == '__main__':
    unittest.main()

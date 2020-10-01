import unittest
from ceasar_ciphres_main import ceasar_ciphres


class CeasarCiphresTest(unittest.TestCase):

    def test_ceasar_ciphres_with_none_and_int_values(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, ceasar_ciphres(None, 2))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_ceasar_ciphres_with_int_values(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, ceasar_ciphres(123, 2))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_ceasar_ciphres_with_list_and_int_values(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, ceasar_ciphres(['1', '2', '3', '4'], 12))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_ceasar_ciphres_with_list_and_int_values_2(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, ceasar_ciphres(12, ['1', '2', '3', '4']))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_ceasar_ciphres(self):
        given_answer = ceasar_ciphres('Inquisitio Haereticae Pravitatis Sanctum Officium', 3)
        expected_value = 'lqtylvlxlr kdhuhxlfdh sudzlxdxlv vdqfxyp riilflyp'
        self.assertEqual(expected_value, given_answer[0])

    def test_ceasar_ciphres_2(self):
        given_answer = ceasar_ciphres('Inquisitio Haereticae Pravitatis Sanctum Officium', 0)
        expected_value = 'inquisitio haereticae pravitatis sanctum officium'
        self.assertEqual(expected_value, given_answer[0])

    def test_ceasar_ciphres_3(self):
        given_answer = ceasar_ciphres('Inquisitio Haereticae Pravitatis Sanctum Officium', 26)
        expected_value = 'inquisitio haereticae pravitatis sanctum officium'
        self.assertEqual(expected_value, given_answer[0])

    def test_ceasar_ciphres_4(self):
        given_answer = ceasar_ciphres('Inquisitio Haereticae Pravitatis Sanctum Officium', -3)
        expected_value = 'fknrfpfqfl exbobqfzxb moxsfqxqfp pxkzqrj lccfzfrj'
        self.assertEqual(expected_value, given_answer[0])

    def test_ceasar_ciphres_5(self):
        given_answer = ceasar_ciphres('Inquisitio Haereticae Pravitatis Sanctum Officium', 22)
        expected_value = 'fknrfpfqfl exbobqfzxb moxsfqxqfp pxkzqrj lccfzfrj'
        self.assertEqual(expected_value, given_answer[0])

    def test_ceasar_ciphres_6(self):
        given_answer = ceasar_ciphres('Inquisitio Haereticae Pravitatis Sanctum Officium', 52)
        expected_value = 'inquisitio haereticae pravitatis sanctum officium'
        self.assertEqual(expected_value, given_answer[0])


if __name__ == '__main__':
    unittest.main()

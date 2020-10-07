import unittest
from ceasar_ciphres_main import ceasar_unciphres


class CeasarUniphresTest(unittest.TestCase):

    def test_ceasar_unciphres_with_none_and_int_values(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, ceasar_unciphres(None, 2))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_ceasar_unciphres_with_int_values(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, ceasar_unciphres(123, 2))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_ceasar_unciphres_with_list_and_int_values(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, ceasar_unciphres(['1', '2', '3', '4'], 12))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_ceasar_unciphres_with_list_and_int_values_2(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, ceasar_unciphres(12, ['1', '2', '3', '4']))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_ceasar_unciphres(self):
        given_answer = \
            ceasar_unciphres('defghijklmnopqrstuvxyzabc', 'lqtylvlxlr kdhuhxlfdh sudzlxdxlv vdqfxyp riilflyp')
        expected_value = 'inquisitio haereticae pravitatis sanctum officium'
        self.assertEqual(expected_value, given_answer)

    def test_ceasar_unciphres_2(self):
        given_answer = \
            ceasar_unciphres('abcdefghijklmnopqrstuvxyz', 'inquisitio haereticae pravitatis sanctum officium')
        expected_value = 'inquisitio haereticae pravitatis sanctum officium'
        self.assertEqual(expected_value, given_answer)

    def test_ceasar_unciphres_3(self):
        given_answer = \
            ceasar_unciphres('xyzabcdefghijklmnopqrstuv', 'fknrfpfqfl exbobqfzxb moxsfqxqfp pxkzqrj lccfzfrj')
        expected_value = 'inquisitio haereticae pravitatis sanctum officium'
        self.assertEqual(expected_value, given_answer)


if __name__ == '__main__':
    unittest.main()

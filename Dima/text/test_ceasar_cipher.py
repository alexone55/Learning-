import unittest
from unittest.mock import patch
from Dima.text.ceasar_cipher import check_and_return_input_to_encrypt
from Dima.text.ceasar_cipher import CaesarCipher


class CeasarCipherTest(unittest.TestCase):

    @patch('builtins.input', side_effect=('abc', 3))
    def test_check_and_return_input_to_encrypt_using_side_effect(self, mock_input):
        expected = ('abc', 3)
        self.assertEqual(check_and_return_input_to_encrypt(), expected)

    def test_caesar_cipher_encrypt(self):
        text_to_encrypt = CaesarCipher('abc', 3)
        actual = text_to_encrypt.encrypt()
        expected = 'def'
        self.assertEqual(actual, expected)

    def test_caesar_cipher_decrypt(self):
        encrypted_text = CaesarCipher('def', 3)
        decrypted_text = encrypted_text.decrypt()
        expected = 'abc'
        self.assertEqual(decrypted_text, expected)

    @patch('builtins.input', side_effect=('3', 3))
    def test_check_and_return_input_to_encrypt_using_side_effect_with_number_parameter(self, mock_input):
        with self.assertRaises(ValueError) as context:
            check_and_return_input_to_encrypt()
        exception_message = str(context.exception)
        self.assertEqual('String contains symbols or numbers', exception_message)

    @patch('builtins.input', side_effect=('@', 3))
    def test_check_and_return_input_to_encrypt_using_side_effect_with_symbol_parameter(self, mock_input):
        with self.assertRaises(ValueError) as context:
            check_and_return_input_to_encrypt()
        exception_message = str(context.exception)
        self.assertEqual('String contains symbols or numbers', exception_message)

    @patch('builtins.input', side_effect=('abc', 'dfd'))
    def test_check_and_return_input_to_encrypt_using_side_effect_with_str_parameter(self, mock_input):
        with self.assertRaises(ValueError) as context:
            check_and_return_input_to_encrypt()
        exception_message = str(context.exception)
        self.assertEqual('Key isn`t int type: ', exception_message)

    @patch('builtins.input', side_effect=('', 3))
    def test_check_and_return_input_to_encrypt_using_side_effect_with_empty_string(self, mock_input):
        expected = ('', 3)
        self.assertEqual(check_and_return_input_to_encrypt(), expected)


if __name__ == '__main__':
    unittest.main()

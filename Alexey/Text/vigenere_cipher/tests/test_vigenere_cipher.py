import unittest
from Alexey.Text.vigenere_cipher.main.vigenere_cipher import generate_key, original_text, cipher_text_func


class TestVigenereCipher(unittest.TestCase):
    def test_send_word_and_key_and_expect_generated_key(self):
        expect_set = 'SEASEASEAS'
        actual_set = generate_key('bigbrother', 'SEA')
        self.assertEqual(expect_set, actual_set)

    def test_send_word_and_key_and_expect_crypted_word(self):
        expect_set = 'TMGTVOLLEJ'
        actual_set = cipher_text_func('BIGBROTHER', 'SEASEASEAS')
        self.assertEqual(expect_set, actual_set)

    def test_send_crypted_word_and_key_and_expect_decrypted_word(self):
        expect_set = 'BIGBROTHER'
        actual_set = original_text('TMGTVOLLEJ', 'SEASEASEAS')
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_type_of_data_in_generator_end_expect_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, generate_key(12, 12))
        exception_message = str(context.exception)
        self.assertEqual("'int' object is not iterable", exception_message)

    def test_send_wrong_type_of_data_in_crypt_func_end_expect_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, cipher_text_func(12, 12))
        exception_message = str(context.exception)
        self.assertEqual("object of type 'int' has no len()", exception_message)

    def test_send_wrong_type_of_data_in_decrypt_func_end_expect_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, original_text(12, 12))
        exception_message = str(context.exception)
        self.assertEqual("object of type 'int' has no len()", exception_message)


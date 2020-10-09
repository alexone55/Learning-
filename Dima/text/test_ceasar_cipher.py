import unittest
from unittest.mock import patch
from Dima.text.ceasar_cipher import check_and_return_input_to_encrypt
from Dima.text.ceasar_cipher import CaesarCipher


class CeasarCipherTest(unittest.TestCase):

    @patch('builtins.input', side_effect=('abc', 3))
    def test_using_side_effect(self, mock_input):
        text = mock_input()
        key = mock_input()
        self.assertTrue(text == 'abc' and key == 3)


if __name__ == '__main__':
    unittest.main()

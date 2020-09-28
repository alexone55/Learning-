import unittest
from count_words_in_a_string import read_from_file


class ReadFromFileTest(unittest.TestCase):

    def test_read_from_file_with_none_value(self):
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(FileNotFoundError, read_from_file(None))
        exception_message = str(context.exception)
        self.assertEqual('File not found', exception_message)

    def test_read_from_file_with_list_value(self):
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(FileNotFoundError, read_from_file([1, 2, '34', 'lorem', 'ipsum']))
        exception_message = str(context.exception)
        self.assertEqual('File not found', exception_message)

    def test_read_from_file_with_digit_value(self):
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(FileNotFoundError, read_from_file(1488))
        exception_message = str(context.exception)
        self.assertEqual('File not found', exception_message)

    def test_read_from_file_with_wrong_string_value(self):
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(FileNotFoundError, read_from_file('text'))
        exception_message = str(context.exception)
        self.assertEqual('File not found', exception_message)

    def test_read_from_file_with_right_path(self):
        text = read_from_file('text.txt')
        expected_value = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
        self.assertEqual(expected_value, text)


if __name__ == '__main__':
    unittest.main()

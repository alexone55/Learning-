from Files.mp3_tagger.main.mp3_tagger import tags_dictionary, add_tags
from unittest.mock import patch
import unittest
import eyed3


class TestMp3Tagger(unittest.TestCase):

    def test_add_new_tags_to_mp3_files(self):
        actual_set = tags_dictionary('check', eyed3.load('test-resources/Михаил Круг - Владимирский Централ.mp3'))
        add_tags(eyed3.load('test-resources/Михаил Круг - Владимирский Централ.mp3'),
                 {'artist': 'test', 'album': 'test', 'album artist': 'test', 'title': 'test', 'track num': 1})
        expect_set = {'artist': 'test', 'album': 'test', 'album artist': 'test', 'title': 'test',
                      'track num': (1, None)}
        self.assertEqual(expect_set, actual_set)

    @patch('builtins.input', side_effect=('Михаил Круг', 'Михаил Круг', 'Михаил Круг', 'Михаил Круг', 1))
    def test_input_new_tags_and_expect_new_dict(self, mock_input):
        expect_set = {'artist': 'Михаил Круг', 'album': 'Михаил Круг', 'album artist': 'Михаил Круг',
                      'title': 'Михаил Круг', 'track num': '1'}
        actual_set = tags_dictionary('edit', '')
        self.assertEqual(expect_set, actual_set)

    def test_input_normal_mp3_file_and_expect_normal_dict(self):
        expect_set = {'artist': 'Михаил Круг', 'album': 'Михаил Круг', 'album artist': 'Михаил Круг',
                      'title': 'Михаил Круг', 'track num': (1, None)}
        actual_set = tags_dictionary('check', eyed3.load('test-resources/myfile.mp3'))
        self.assertEqual(expect_set, actual_set)

    def test_add_less_tags_to_mp3_files(self):
        with self.assertRaises(KeyError) as context:
            add_tags(eyed3.load('test-resources/Михаил Круг - Владимирский Централ.mp3'),
                 {'artist': 'test', 'album': 'test', 'album artist': 'test1', 'title': 'test'})
        exception_message = str(context.exception)
        self.assertEqual('\'Wrong tag or tags count\'', exception_message)

    def test_add_different_tag_to_mp3_files(self):
        with self.assertRaises(KeyError) as context:
            add_tags(eyed3.load('test-resources/Михаил Круг - Владимирский Централ.mp3'),
                 {'artist': 'test', 'album': 'test', 'album artists': 'test1', 'title': 'test'})
        exception_message = str(context.exception)
        self.assertEqual('\'Wrong tag or tags count\'', exception_message)
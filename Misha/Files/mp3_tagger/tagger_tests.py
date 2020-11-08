import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import eyed3
from tagger_main import input_mp3_file_name, set_tag, get_tag, main


class TaggerTest(unittest.TestCase):

    def test_input_mp3_file_name_with_wrong_path(self):
        with self.assertRaises(TypeError) as context:
            input_mp3_file_name('path/to/file/')
        exception_message = str(context.exception)
        self.assertEqual('Invalid file type', exception_message)

    def test_tag_setter_with_right_dict(self):
        audiofile = eyed3.load('Распродажа_на_AliExpress_Максим_Галкин.mp3')
        tags_dict = {'artist': 'artist_name',
                     'album': 'album_name',
                     'album artist': 'alb_artist_name',
                     'title': 'audio_title',
                     'track num': (1, 1)}
        set_tag(audiofile, tags_dict)
        audiofile_tags = get_tag(audiofile)
        self.assertEqual(tags_dict, audiofile_tags)

    def test_tag_setter_with_right_dict_and_big_strings(self):
        audiofile = eyed3.load('Распродажа_на_AliExpress_Максим_Галкин.mp3')
        tags_dict = {'artist': 'artist_name'*228,
                     'album': 'album_name'*1488,
                     'album artist': 'alb_artist_name'*88,
                     'title': 'audio_title'*9524,
                     'track num': (1, 1)}
        set_tag(audiofile, tags_dict)
        audiofile_tags = get_tag(audiofile)
        self.assertEqual(tags_dict, audiofile_tags)

    @patch('builtins.input', side_effect=['qwerty'])  # called all string only when in [], otherwise called first letter
    def test_main_1(self, mock_input):
        with self.assertRaises(TypeError) as context:
            main()
        exception_message = str(context.exception)
        self.assertEqual('Invalid file type', exception_message)

    @patch('builtins.input', side_effect=['Распродажа_на_AliExpress_Максим_Галкин.mp3'])
    @patch('tagger_main.get_tag')
    @patch('tagger_main.input_mp3_file_name')
    def test_main_2(self, mock_input, mock_get_tag, mock_input_mp3_file_name):
        main()
        mock_input.assert_called_once_with('Распродажа_на_AliExpress_Максим_Галкин.mp3')
        mock_get_tag.assert_called_once()
        mock_input_mp3_file_name.assert_called_once()

from Alexey.Files.mp3_tagger.main.mp3_tagger import new_dictionary, tag_dictionary, add_tags
import unittest
import mock
import eyed3


class TestMp3Tagger(unittest.TestCase):

    def test_input_wrong_mp3_name_and_expect_error_in_tag_dict(self):
        with self.assertRaises(OSError) as context:
            self.assertRaises(OSError, tag_dictionary(eyed3.load('file_name')))
        exception_message = str(context.exception)
        self.assertEqual('file not found: file_name', exception_message)

    def test_input_normal_mp3_file_and_expect_normal_dict(self):
        expect_set = {'artist': 'Михаил Круг', 'album': 'Михаил Круг', 'album artist': 'Михаил круг', 'title': 'Михаил Круг', 'track num': (1, None)}
        actual_set = tag_dictionary(eyed3.load('Михаил Круг - Владимирский Централ.mp3'))
        self.assertEqual(expect_set, actual_set)

    def test_input_new_tags_and_expect_new_dict(self):
        artist = 'Михаил Круг'
        album = 'Михаил Круг'
        album_artist = 'Михаил круг'
        title = 'Михаил Круг'
        track_num = 1
        expect_set = {'artist': 'Михаил Круг', 'album': 'Михаил Круг', 'album artist': 'Михаил круг', 'title': 'Михаил Круг', 'track num': 1}
        actual_set = new_dictionary(artist, album, album_artist, title, track_num)
        self.assertEqual(expect_set, actual_set)

    def test_add_new_tags_to_mp3_files(self):
        actual_set = tag_dictionary(eyed3.load('Михаил Круг - Владимирский Централ.mp3'))
        add_tags(eyed3.load('Михаил Круг - Владимирский Централ.mp3'), {'artist': 'test', 'album': 'test', 'album artist': 'test', 'title': 'test', 'track num': 1})
        expect_set = {'artist': 'test', 'album': 'test', 'album artist': 'test', 'title': 'test', 'track num': (1, None)}
        self.assertEqual(expect_set, actual_set)
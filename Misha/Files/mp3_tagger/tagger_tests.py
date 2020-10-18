import unittest
import eyed3
from tagger_main import input_mp3_file_name, set_tag, get_tag


class TaggerTest(unittest.TestCase):

    def test_input_mp3_file_name_with_wrong_path(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, input_mp3_file_name('path/to/file/'))
        exception_message = str(context.exception)
        self.assertEqual('Invalid file type', exception_message)

    def test_input_mp3_file_name_with_wrong_filename(self):
        with self.assertRaises(OSError) as context:
            self.assertRaises(OSError, input_mp3_file_name('file.mp3'))
        exception_message = str(context.exception)
        self.assertEqual('file not found', exception_message)

    def test_tag_setter_with_wrong_dict(self):
        audiofile = eyed3.load('Распродажа_на_AliExpress_Максим_Галкин.mp3')
        tags_dict = {'artist': audiofile.tag.artist,
                     'album': audiofile.tag.album,
                     'album artist': audiofile.tag.album_artist,
                     'title': audiofile.tag.title,
                     'track number': audiofile.tag.track_num}
        with self.assertRaises(KeyError) as context:
            self.assertRaises(KeyError, set_tag(audiofile, tags_dict))
        exception_message = str(context.exception)
        self.assertEqual('Key error', exception_message)

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


if __name__ == '__main__':
    unittest.main()

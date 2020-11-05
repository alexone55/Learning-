import unittest
import os
from Alexey.Files.create_zip_file.main.create_zip_file import all_files_in_folder, archive_maker


class TestCreateZipFileMaker(unittest.TestCase):
    def test_add_all_files_in_folders(self):
        expect_set = ['NewZip.zip', 'test_create_zip_file.py', 'test_file.txt']
        actual_set = all_files_in_folder()
        self.assertEqual(expect_set, actual_set)

    def test_make_new_zip_file(self):
        expect_set = 'NewZip.zip'
        archive_maker(all_files_in_folder())
        actual_set = all_files_in_folder()
        self.assertEqual(expect_set, actual_set[0])

    def test_make_archive_with_one_file(self):
        expect_set = True
        archive_maker(['test_file.txt'], 'one_file.zip', )
        actual_set = os.path.isfile('one_file.zip')
        self.assertEqual(expect_set, actual_set)

    def test_make_archive_with_many_files(self):
        expect_set = True
        archive_maker(['test_file.txt', 'NewZip.zip'], 'many_files.zip')
        actual_set = os.path.isfile('many_files.zip')
        self.assertEqual(expect_set, actual_set)

    def test_add_empty_folder_to_zip_archive(self):
        expect_set = True
        archive_maker(['test_add_empty_folder_to_zip'], 'empty_folder.zip')
        actual_set = os.path.isfile('empty_folder.zip')
        self.assertEqual(expect_set, actual_set)
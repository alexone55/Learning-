import unittest
import os
from Alexey.Files.create_zip_file.main.create_zip_file import all_files_in_folder, archive_maker


class TestCreateZipFileMaker(unittest.TestCase):
    def test_add_all_files_in_folders(self):
        expect_set = ['NewZip.zip', 'test_create_zip_file.py', 'test_file.txt']
        actual_set = all_files_in_folder()
        self.assertEqual(expect_set, actual_set)

    def test_make_new_zip_file(self):
        expect_set = ['NewZip.zip']
        archive_maker(all_files_in_folder())
        actual_set = []
        files_set = all_files_in_folder()
        for file in files_set:
            if file == 'NewZip.zip':
                actual_set.append(file)
        self.assertEqual(expect_set, actual_set)
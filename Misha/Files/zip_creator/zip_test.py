import unittest
import os
from zip_main import check_set_of_paths, create_archive
import zipfile


class ZipTest(unittest.TestCase):

    def test_check_set_of_paths_with_wrong_paths(self):
        set_of_paths = ['path/to/file.1', 'path.txt', 'file.1']
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(FileNotFoundError, check_set_of_paths(set_of_paths))
        exception_message = str(context.exception)
        self.assertEqual('List of paths is empty', exception_message)

    def test_create_archive_with_right_set_of_paths(self):
        set_of_paths = ['zip_main.py', 'zip_test.py']
        expected_path_size_list = [os.path.getsize(set_of_paths[0]), os.path.getsize(set_of_paths[1])]
        archive_name = 'utestzip.zip'
        create_archive(set_of_paths, archive_name)
        testzip = zipfile.ZipFile(archive_name, 'r')
        returned_size_list = []
        for name in testzip.namelist():
            returned_size_list.append(testzip.getinfo(name).file_size)
        self.assertEqual(returned_size_list, expected_path_size_list)

    def test_create_archive_with_wrong_paths(self):
        set_of_paths = ['path/to/file.1', 'path.txt', 'file.1']
        with self.assertRaises(FileNotFoundError) as context:
            self.assertRaises(FileNotFoundError, create_archive(set_of_paths, 'wrong_archive.zip'))
        exception_message = str(context.exception)
        self.assertEqual('List of paths is empty', exception_message)


if __name__ == '__main__':
    unittest.main()

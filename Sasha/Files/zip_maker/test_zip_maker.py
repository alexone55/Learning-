from zip_maker import get_cmd_files
from zip_maker import get_all_files
import unittest
import sys

class TestZipMaker(unittest.TestCase):
    def test_get_files_from_cmd_are_not_null(self):
        input_files = ["text.txt", "text1.txt"]
        files = get_cmd_files(input_files)

        assert len(input_files) - 1 > 0

    def test_get_all_files_in_dir(self):
        files = get_all_files()
        assert len(files) > 0

if __name__ == "__main__":
    unittest.main()
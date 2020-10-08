import unittest
import os
from Alexey.Text.guestbook.main.guestbook import add_comment, show_comment


class TestGuestbook(unittest.TestCase):
    def test_comment_and_check_file_is_exist(self):
        add_comment("comment")
        expect_file = os.path.isfile("comment_book.txt")
        self.assertEqual(expect_file, True)

    def test_read_commend(self):
        expect_set = 77
        actual_set = len(show_comment())
        self.assertEqual(expect_set, actual_set)


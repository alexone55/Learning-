import unittest
from Alexey.OB-366.sieve_of_eratostenes.sieve_of_eratosthenes import eratosthenes


class TestSort(unittest.TestCase):

    def test_send_zero(self):
        expect_set = []
        self.assertEqual(eratosthenes(0), expect_set)

    def test_one_num(self):
        expect_set = []
        self.assertEqual(eratosthenes(1), expect_set)

    def test_fifty_nums(self):
        expect_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(eratosthenes(50), expect_set)

    def test_two_hundred_nums(self):
        expect_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                      73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                      179, 181, 191, 193, 197, 199]
        self.assertEqual(eratosthenes(200), expect_set)


    def test_send_none(self):
        expect_set = []
        self.assertEqual(eratosthenes(None), expect_set)
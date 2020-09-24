import unittest
from Alexey.OB_366.sieve_of_eratostenes.sieve_of_eratosthenes import eratosthenes


class TestSort(unittest.TestCase):

    def test_send_zero_and_return_empty_list(self):
        expect_set = []
        actual_list = eratosthenes(0)
        self.assertEqual(expect_set, actual_list)

    def test_send_one_and_expect_return_empty_list(self):
        expect_set = []
        actual_list = eratosthenes(1)
        self.assertEqual(expect_set, actual_list)

    def test_send_number_fifty_and_return_expect_list(self):
        expect_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        actual_list = eratosthenes(50)
        self.assertEqual(expect_set, actual_list)

    def test_send_number_two_hundred_and_return_expect_list(self):
        expect_set = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
                      73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
                      179, 181, 191, 193, 197, 199]
        actual_list = eratosthenes(200)
        self.assertEqual(expect_set, actual_list)

    def test_send_none_and_expect_return_exception_typeerror(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, eratosthenes(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

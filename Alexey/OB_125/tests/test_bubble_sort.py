from Alexey.OB_125.sorting.time_decorator import timer
from Alexey.OB_125.sorting.bubble_sort import sort
import unittest


class TestSort(unittest.TestCase):

    def test_send_numbers_and_return_expect_set(self):
        expect_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        actual_set = sort([2, 1, 5, 4, 3, 6, 7, 8, 10, 9])
        self.assertEqual(expect_set, actual_set)

    def test_send_liters_and_return_expect_set(self):
        expect_set = ["a", "b", "c"]
        actual_set = sort(["a", "c", "b"])
        self.assertEqual(expect_set, actual_set)

    def test_send_empty_list_and_return_empty_list(self):
        expect_set = []
        actual_set = sort([])
        self.assertEqual(expect_set, actual_set)

    def test_send_one_number_in_lit_and_return_one_number_in_list(self):
        expect_set = [1]
        actual_set = sort([1])
        self.assertEqual(expect_set, actual_set)

    def test_send_none_and_expect_empty_list(self):
        expect_set = []
        actual_set = sort(None)
        self.assertEqual(expect_set, actual_set)


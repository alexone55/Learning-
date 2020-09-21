from Alexey.OB_125.sorting.merge_sort import sort
import unittest


class TestSort(unittest.TestCase):

    def test_normal_sort(self):
        expect_set = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sort([2, 1, 5, 4, 3, 6, 7, 8, 10, 9]),
                         expect_set)

    def test_liters_sort(self):
        expect_set = ["a", "b", "c"]
        self.assertEqual(sort(["a", "c", "b"]),
                         expect_set)

    def test_send_nothing(self):
        expect_set = []
        self.assertEqual(sort([]),
                         expect_set)

    def test_send_one_num(self):
        expect_set = [1]
        self.assertEqual(sort([1]),
                         expect_set)

    def test_send_none(self):
        expect_set = []
        self.assertEqual(sort(None),
                         expect_set)


from bubble_sort import sort
import unittest
import random


class TestSort(unittest.TestCase):

    def test_normal_sort(self):
        expect_set = [i for i in range(1, 100)]
        self.assertEqual(sort(random.sample(range(1, 100), 99)),
                         expect_set)

    def test_liters_sort(self):
        expect_set = ["a", "b", "c"]
        self.assertEqual(sort(["a", "c", "b"]),
                         expect_set)

    def test_send_nothing(self):
        expect_set = []
        self.assertEqual(sort([]), [])

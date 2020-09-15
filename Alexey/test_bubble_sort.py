from bubble_sort import sort
import unittest
import random


class TestSort(unittest.TestCase):

    def test_sort(self):
        self.assertEqual(sort(random.sample(range(1, 100), 99)),
                         [i for i in range(1, 100)])

import unittest
import random
import time
from main import bubble_sort
from main import merge_sort_iterative
from main import check_input_data_format


class SortingTest(unittest.TestCase):

    def setUp(self):
        random.seed = time.time()
        self.arr_to_sort = [0] * 1000
        for index in range(1000):
            self.arr_to_sort[index] = random.randint(1, 1000)

    def test_bubble(self):
        sorted_array = bubble_sort(self.arr_to_sort)
        test_pass = True
        for index in range(1, 1000):
            if sorted_array[index - 1] > sorted_array[index]:
                test_pass = False
                break
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_merge(self):
        sorted_array = merge_sort_iterative(self.arr_to_sort)
        test_pass = True
        for index in range(1, 1000):
            if sorted_array[index - 1] > sorted_array[index]:
                test_pass = False
                break
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)


if __name__ == '__main__':
    unittest.main()

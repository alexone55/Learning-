import unittest
from main import merge_sort_iterative


class MergeSortingTest(unittest.TestCase):

    def test_merge_1(self):
        arr_to_sort = [1, 5, 1, 235, 2, 51, 5, 1, 25, 2]
        sorted_array = merge_sort_iterative(arr_to_sort)
        test_pass = True
        for index in range(1, 10):
            if sorted_array[index - 1] > sorted_array[index]:
                test_pass = False
                break
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_merge_2(self):
        arr_to_sort = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sorted_array = merge_sort_iterative(arr_to_sort)
        test_pass = True
        for index in range(1, 10):
            if sorted_array[index - 1] > sorted_array[index]:
                test_pass = False
                break
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_merge_3(self):
        arr_to_sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sorted_array = merge_sort_iterative(arr_to_sort)
        test_pass = True
        for index in range(1, 10):
            if sorted_array[index - 1] > sorted_array[index]:
                test_pass = False
                break
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_merge_4(self):
        arr_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_array = merge_sort_iterative(arr_to_sort)
        test_pass = True
        for index in range(1, 10):
            if sorted_array[index - 1] > sorted_array[index]:
                test_pass = False
                break
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_merge_5(self):
        arr_to_sort = [1]
        sorted_array = merge_sort_iterative(arr_to_sort)
        test_pass = True
        for index in range(1, 1):
            if sorted_array[index - 1] > sorted_array[index]:
                test_pass = False
                break
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_merge_6(self):
        arr_to_sort = [1, 5, ' ', 235, 2, 51, 5, 1, 25, 2]
        sorted_array = merge_sort_iterative(arr_to_sort)
        test_pass = False
        if sorted_array =='Error':
            test_pass=True
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_merge_7(self):
        arr_to_sort = [1, 5, None, 235, 2, 51, 5, 1, 25, 2]
        sorted_array = merge_sort_iterative(arr_to_sort)
        test_pass = False
        if sorted_array == 'Error':
            test_pass = True
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_merge_8(self):
        arr_to_sort = [None,None,None,None,None]
        sorted_array = merge_sort_iterative(arr_to_sort)
        test_pass = False
        if sorted_array == 'Error':
            test_pass = True
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)


if __name__ == '__main__':
    unittest.main()

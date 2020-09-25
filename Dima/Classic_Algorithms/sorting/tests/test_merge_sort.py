import unittest
from Dima.Classic_Algorithms.sorting.merge_sort import merge_sort
from Dima.Classic_Algorithms.sorting.merge_sort import merge


class MergeSortTest(unittest.TestCase):

    def test_when_input_is_None_return_type_error(self):
        self.assertRaises(TypeError, merge_sort, None)

    def test_when_input_zero(self):
        sorted_list = merge_sort([0])
        expected_results = [0]
        self.assertEqual(sorted_list, expected_results)

    def test_when_input_str(self):
        sorted_list = merge_sort(['b', 'a', 'd', 'c', 'e', 'aaa', 'aa'])
        expected_results = ['a', 'aa', 'aaa', 'b', 'c', 'd', 'e']
        self.assertEqual(sorted_list, expected_results)

    def test_when_input_is_negative(self):
        sorted_list = merge_sort([0, -1, -3, -2, -5, -4])
        expected_results = [-5, -4, -3, -2, -1, 0]
        self.assertEqual(sorted_list, expected_results)

    def test_when_input_is_normal(self):
        sorted_list = merge_sort([0, 1, 3, 2, 5, 4])
        expected_results = [0, 1, 2, 3, 4, 5]
        self.assertEqual(sorted_list, expected_results)

    def test_when_input_repeated_values(self):
        sorted_list = merge_sort([1, 3, 0, 1, 3, 2, 5, 4, 3])
        expected_results = [0, 1, 1, 2, 3, 3, 3, 4, 5]
        self.assertEqual(sorted_list, expected_results)

    def test_when_merge_function_input_is_null(self):
        merged = merge([0], [0], [0, 0])
        expected_results = [0, 0]
        self.assertEqual(merged, expected_results)

    def test_when_merge_function_input_normal(self):
        merged = merge([0, 1, 3], [2, 5, 4], [0, 1, 3, 2, 5, 4])
        expected_results = [0, 1, 2, 3, 5, 4]
        self.assertEqual(merged, expected_results)

    def test_when_merge_function_input_str_value(self):
        merged = merge(['erwerwe', '4dsfsdf'], ['asdfee'], ['erwerwe', 'asdfee', '4dsfsdf'])
        expected_results = ['asdfee', 'erwerwe', '4dsfsdf']
        self.assertEqual(merged, expected_results)


if __name__ == '__main__':
    unittest.main()

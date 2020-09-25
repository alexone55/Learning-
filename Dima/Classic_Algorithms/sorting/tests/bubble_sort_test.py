import unittest
from Dima.Classic_Algorithms.sorting.bubble_sort import bubble_sort


class BubbleSortTest(unittest.TestCase):

    def test_when_input_is_None(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, bubble_sort(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_when_input_zero(self):
        sorted_list = bubble_sort([0])
        expected_results = [0]
        self.assertEqual(sorted_list, expected_results)

    def test_when_input_str(self):
        sorted_list = bubble_sort(['b', 'a', 'd', 'c', 'e', 'aaa', 'aa'])
        expected_results = ['a', 'aa', 'aaa', 'b', 'c', 'd', 'e']
        self.assertEqual(sorted_list, expected_results)

    def test_when_input_is_negative(self):
        sorted_list = bubble_sort([0, -1, -3, -2, -5, -4])
        expected_results = [-5, -4, -3, -2, -1, 0]
        self.assertEqual(sorted_list, expected_results)

    def test_when_input_is_normal(self):
        sorted_list = bubble_sort([0, 1, 3, 2, 5, 4])
        expected_results = [0, 1, 2, 3, 4, 5]
        self.assertEqual(sorted_list, expected_results)


if __name__ == '__main__':
    unittest.main()

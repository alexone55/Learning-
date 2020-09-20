import unittest
from main import bubble_sort


class BubbleSortingTest(unittest.TestCase):

    def test_bubble_sort_with_random_array(self):
        arr_to_sort = [1, 5, 1, 235, 2, 51, 5, 1, 25, 2]
        sorted_array = bubble_sort(arr_to_sort)
        expected_result = [1, 1, 1, 2, 2, 5, 5, 25, 51, 235]
        self.assertEqual(expected_result, sorted_array)

    def test_bubble_with_equally_filled_array(self):
        arr_to_sort = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        sorted_array = bubble_sort(arr_to_sort)
        expected_result = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.assertEqual(expected_result, sorted_array)

    def test_bubble_with_sorted_array(self):
        arr_to_sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sorted_array = bubble_sort(arr_to_sort)
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expected_result, sorted_array)

    def test_bubble_with_reverse_sorted_array(self):
        arr_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        sorted_array = bubble_sort(arr_to_sort)
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expected_result, sorted_array)

    def test_bubble_with_one_element_array(self):
        arr_to_sort = [1]
        sorted_array = bubble_sort(arr_to_sort)
        expected_result = [1]
        self.assertEqual(expected_result, sorted_array)

    def test_bubble_with_wrong_string_object_in_array(self):
        arr_to_sort = [1, 5, ' ', 235, 2, 51, 5, 1, 25, 2]
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, bubble_sort(arr_to_sort))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_bubble_with_wrong_non_type_object_in_array(self):
        arr_to_sort = [1, 5, None, 235, 2, 51, 5, 1, 25, 2]
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, bubble_sort(arr_to_sort))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_bubble_with_array_of_none_type_objects(self):
        arr_to_sort = [None, None, None, None, None]
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, bubble_sort(arr_to_sort))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)


if __name__ == '__main__':
    unittest.main()

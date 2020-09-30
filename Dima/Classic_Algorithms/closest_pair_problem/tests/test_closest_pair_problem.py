import unittest
from Dima.Classic_Algorithms.closest_pair_problem.closest_pair_problem import create_route_matrix
from Dima.Classic_Algorithms.closest_pair_problem.closest_pair_problem import find_min_route


class ClosestPairProblemTest(unittest.TestCase):

    def test_create_route_matrix_when_input_is_None(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, create_route_matrix(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError_1, input dot_list isn`t type list: ', exception_message)

    def test_create_route_matrix_when_input_is_str(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, create_route_matrix('sdffsdfsdf'))
        exception_message = str(context.exception)
        self.assertEqual('TypeError_1, input dot_list isn`t type list: ', exception_message)

    def test_create_route_matrix_with_invalid_params_in_list(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, create_route_matrix([['213', 0], [None, 0], [2, 4], [0, 0]]))
        exception_message = str(context.exception)
        self.assertEqual('TypeError_1, input dot_list isn`t type list: ', exception_message)

    def test_create_route_matrix_with_none_params_in_list(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, create_route_matrix([None, [1, 0], [0, 0], [2, 4], [0, 0]]))
        exception_message = str(context.exception)
        self.assertEqual('TypeError_1, input dot_list isn`t type list: ', exception_message)

    def test_create_route_matrix_with_str_params_in_list(self):
        self.assertRaises(TypeError, create_route_matrix, ['sdfdsf', [1, 0], [0, 0], [2, 4], [0, 0]])

    def test_find_min_route_when_input_with_right_params(self):
        dots = find_min_route(create_route_matrix([[1, 1], [1, 100], [1, 50], [53, 3]]))
        expected_result = (0, 2, 49.0)
        self.assertEqual(expected_result, dots)

    def test_find_min_route_with_parameter_zero_in_all_dots(self):
        dots = find_min_route(create_route_matrix([[0, 0], [0, 0], [0, 0], [0, 0]]))
        expected_result = (0, 1, 0.0)
        self.assertEqual(expected_result, dots)

    def test_find_min_route_with_parameter_zero_in_some_dots(self):
        dots = find_min_route(create_route_matrix([[0, 1], [1, 0], [0, 0], [2, 4], [0, 0]]))
        expected_result = (2, 4, 0.0)
        self.assertEqual(expected_result, dots)

    def test_find_min_route_with_invalid_types_in_matrix(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, find_min_route([['213', 0, 'dfgsdfg'], [None, 0, 4], [2, 4, 5], [0, 0, 45]]))
        exception_message = str(context.exception)
        self.assertEqual('TypeError_3, some values in matrix isn`t numbers: ', exception_message)

    def test_find_min_route_with_invalid_type_of_input(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, find_min_route('dfdsd'))
        exception_message = str(context.exception)
        self.assertEqual('TypeError_2 Route_matrix isn`t type: list: ', exception_message)


if __name__ == '__main__':
    unittest.main()

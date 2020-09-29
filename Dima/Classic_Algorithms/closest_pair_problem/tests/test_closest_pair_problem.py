import unittest
from Dima.Classic_Algorithms.closest_pair_problem.closest_pair_problem import create_route_matrix
from Dima.Classic_Algorithms.closest_pair_problem.closest_pair_problem import find_min_route


class ClosestPairProblemTest(unittest.TestCase):

    def test_create_route_matrix_when_input_is_None(self):
        self.assertRaises(TypeError, create_route_matrix, None)

    def test_create_route_matrix_when_input_is_str(self):
        self.assertRaises(TypeError, create_route_matrix, '3dsfwer')

    def test_create_route_matrix_with_none_params_in_list(self):
        self.assertRaises(TypeError, create_route_matrix, [None, [1, 0], [0, 0], [2, 4], [0, 0]])

    def test_create_route_matrix_with_str_params_in_list(self):
        self.assertRaises(TypeError, create_route_matrix, ['sdfdsf', [1, 0], [0, 0], [2, 4], [0, 0]])

    def test_create_route_matrix_with_invalid_params_in_list(self):
        self.assertRaises(TypeError, create_route_matrix, [['213', 0], [None, 0], [2, 4], [0, 0]])

    def test_closest_pair_problem_when_input_with_right_params(self):
        dots = find_min_route(create_route_matrix([[1, 1], [1, 100], [1, 50], [53, 3]]))
        expected_result = (0, 2, 49.0)
        self.assertEqual(expected_result, dots)

    def test_closest_pair_problem_with_parameter_zero_in_all_dots(self):
        dots = find_min_route(create_route_matrix([[0, 0], [0, 0], [0, 0], [0, 0]]))
        expected_result = (0, 1, 0.0)
        self.assertEqual(expected_result, dots)

    def test_closest_pair_problem_with_parameter_zero_in_some_dots(self):
        dots = find_min_route(create_route_matrix([[0, 1], [1, 0], [0, 0], [2, 4], [0, 0]]))
        expected_result = (2, 4, 0.0)
        self.assertEqual(expected_result, dots)

    def test_closest_pair_problem_with_parameter_zero_in_some_dots(self):
        dots = find_min_route(create_route_matrix([[0, 1], [1, 0], [0, 0], [2, 4], [0, 0]]))
        expected_result = (2, 4, 0.0)
        self.assertEqual(expected_result, dots)


if __name__ == '__main__':
    unittest.main()

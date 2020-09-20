import unittest
from main import create_route_matrix


class CreatingMatrixTest(unittest.TestCase):

    def test_create_route_matrix_with_right_parameters(self):
        route_matrix = create_route_matrix([[1, 1], [1, 2]])
        expected_result = [[0, 1],
                           [0, 0]]  # counted by self
        self.assertEqual(expected_result, route_matrix)

    def test_create_route_matrix_with_right_parameters_and_minimal_amount_of_dots(self):
        route_matrix = create_route_matrix([[1, 1], [1, 2], [2, 2]])

        expected_result = [[0, 1, 2 ** (1 / 2)],
                           [0, 0, 1],
                           [0, 0, 0]]  # counted by self
        self.assertEqual(expected_result, route_matrix)

    def test_create_route_matrix_with_non_type_object_in_matrix(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, create_route_matrix([[1, None], [1, 2], [2, 2]]))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_create_route_matrix_with_string_object_in_matrix(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, create_route_matrix([[1, 'sc'], [1, 2], [2, 2]]))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)


if __name__ == '__main__':
    unittest.main()

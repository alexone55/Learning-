import unittest
from main import find_min_route


class FindingMinRouteTest(unittest.TestCase):

    def test_find_min_route_with_right_parameters(self):
        route_matrix = [[0, 1, 1],
                        [0, 0, (2 ** (1 / 2))],
                        [0, 0, 0]]
        dot_1, dot_2, min_route = find_min_route(route_matrix)
        expected_result = [0, 1, 1.0]
        self.assertEqual(expected_result, [dot_1, dot_2, min_route])

    def test_find_min_route_with_wrong_string_type_object_in_matrix(self):
        route_matrix = [[0, '1', 1],
                        [0, 0, (2 ** (1 / 2))],
                        [0, 0, 0]]
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, find_min_route(route_matrix))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_find_min_route_with_non_type_object_in_matrix(self):
        route_matrix = [[0, None, 1],
                        [0, 0, (2 ** (1 / 2))],
                        [0, 0, 0]]
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, find_min_route(route_matrix))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_find_min_route_with_parameter_none(self):
        route_matrix = None
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, find_min_route(route_matrix))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_find_min_route_with_string_parameter(self):
        route_matrix = 'string'
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, find_min_route(route_matrix))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_find_min_route_with_int_parameter(self):
        route_matrix = 1
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, find_min_route(route_matrix))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)


if __name__ == '__main__':
    unittest.main()

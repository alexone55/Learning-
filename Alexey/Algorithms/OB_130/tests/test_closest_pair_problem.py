import unittest
from Alexey.Algorithms.OB_130.closest_pair_problem.closest_pair_problem import lets_find_minimum_distance


class TestCollatzConjecture(unittest.TestCase):

    def test_send_one_dot_and_expect_alert_message(self):
        expect_set = "You have just one dot"
        actual_set = lets_find_minimum_distance({'A': (1, 2)})
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_type_of_data_and_expect_type_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, lets_find_minimum_distance('01003012'))
        exception_message = str(context.exception)
        self.assertEqual('This is not dict', exception_message)

    def test_send_normal_dots_and_return_normal_response(self):
        expect_set = ('C:D', 11.0)
        actual_set = lets_find_minimum_distance({'A': (1, 2), 'B': (4, 45), 'C': (13, 165), 'D': (13, 176)})
        self.assertEqual(expect_set, actual_set)

    def test_send_negative_dots_and_return_normal_response(self):
        expect_set = ('C:D', 11.0)
        actual_set = lets_find_minimum_distance({'A': (-1, -2), 'B': (-4, -45), 'C': (-13, -165), 'D': (-13, -176)})
        self.assertEqual(expect_set, actual_set)



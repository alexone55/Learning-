import unittest
from Dima.Classic_Algorithms.collatz_conjecture.collatz_conjecture import collatz_conjecture


class TestCollatzConjecture(unittest.TestCase):

    def test_collatz_conjecture_right_parameter_10(self):
        steps = collatz_conjecture(10)
        expected_result = 6
        self.assertEqual(expected_result, steps)

    def test_collatz_conjecture_border_parameter_0(self):
        steps = collatz_conjecture(0)
        expected_result = []
        self.assertEqual(expected_result, steps)

    def test_collatz_conjecture_right_parameter_27(self):
        steps = collatz_conjecture(27)
        expected_result = 111
        self.assertEqual(expected_result, steps)

    def test_collatz_conjecture_minimal_parameter(self):
        steps = collatz_conjecture(2)
        expected_result = 1
        self.assertEqual(expected_result, steps)

    def test_collatz_conjecture_none_type_object(self):
        self.assertRaises(TypeError, collatz_conjecture, None)

    def test_collatz_conjecture_string_object(self):
        self.assertRaises(TypeError, collatz_conjecture, 'asdfd')

    def test_collatz_conjecture_list_object(self):
        self.assertRaises(TypeError, collatz_conjecture, [1, 6, 4])


if __name__ == '__main__':
    unittest.main()

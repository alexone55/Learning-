import unittest
from Alexey.OB_124.collatz_conjecture.collatz_conjecture import conjecture


class TestCollatzConjecture(unittest.TestCase):

    def test_send_number_fifty_and_result_expect_set(self):
        expect_set = [25, 76, 38, 19, 58,
                      29, 88, 44, 22, 11,
                      34, 17, 52, 26, 13,
                      40, 20, 10, 5, 16,
                      8, 4, 2, 1
                      ]
        actual_set = conjecture(50)
        self.assertEqual(expect_set, actual_set)

    def test_send_number_two_hundred_and_result_expect_set(self):
        expect_set = [598, 299, 898, 449, 1348,
                      674, 337, 1012, 506, 253,
                      760, 380, 190, 95, 286,
                      143, 430, 215, 646, 323,
                      970, 485, 1456, 728, 364,
                      182, 91, 274, 137, 412,
                      206, 103, 310, 155, 466,
                      233, 700, 350, 175, 526,
                      263, 790, 395, 1186, 593,
                      1780, 890, 445, 1336, 668,
                      334, 167, 502, 251, 754,
                      377, 1132, 566, 283, 850,
                      425, 1276, 638, 319, 958,
                      479, 1438, 719, 2158, 1079,
                      3238, 1619, 4858, 2429, 7288,
                      3644, 1822, 911, 2734, 1367,
                      4102, 2051, 6154, 3077, 9232,
                      4616, 2308, 1154, 577, 1732,
                      866, 433, 1300, 650, 325, 976,
                      488, 244, 122, 61, 184, 92, 46,
                      23, 70, 35, 106, 53, 160, 80,
                      40, 20, 10, 5, 16, 8, 4, 2, 1]
        actual_set = conjecture(199)
        self.assertEqual(expect_set, actual_set)

    def test_send_one_and_result_empty_list(self):
        expect_set = []
        actual_set = conjecture(1)
        self.assertEqual(expect_set, actual_set)

    def test_send_zero_and_result_is_zero(self):
        expect_set = 0
        actual_set = conjecture(0)
        self.assertEqual(expect_set, actual_set)

    def test_send_none_and_result_is_empty_list(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, conjecture(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

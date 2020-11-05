import unittest
from Alexey.Text.quote_tracker.main.quote_tracker import quote_tracker, logic


class TestQuoteTracker(unittest.TestCase):
    def test_send_symbols_and_expect_up_message(self):
        expect_set = '+1 Up'
        actual_set = logic(2, 1)
        self.assertEqual(expect_set, actual_set)

    def test_send_symbols_and_expect_down_message(self):
        expect_set = '-1 Down'
        actual_set = logic(1, 2)
        self.assertEqual(expect_set, actual_set)

    def test_send_symbols_and_expect_equal_message(self):
        expect_set = 'Equal'
        actual_set = logic(2, 2)
        self.assertEqual(expect_set, actual_set)

    def test_send_one_argument_and_expect_error(self):
        with self.assertRaises(TypeError) as context:
            logic(2)
        exception_message = str(context.exception)
        self.assertEqual("logic() missing 1 required positional argument: 'previous'", exception_message)

    def test_send_None_type_and_expect_error(self):
        with self.assertRaises(TypeError) as context:
            logic(None, None)
        exception_message = str(context.exception)
        self.assertEqual("'<' not supported between instances of 'NoneType' and 'NoneType'", exception_message)



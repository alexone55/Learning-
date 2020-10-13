import unittest
from Alexey.Text.regex_query_tool.main.regex_query_tool import reg_expression


class TestRegexQueryTool(unittest.TestCase):
    def test_send_pattern_and_return_expect_set(self):
        expect_set = ['Georgie', 'Genia']
        actual_set = reg_expression('Ge')
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_pattern_and_expect_empty_list(self):
        expect_set = []
        actual_set = reg_expression('Po')
        self.assertEqual(expect_set, actual_set)

    def test_send_number_and_return_expect_set(self):
        expect_set = ['12', '113']
        actual_set = reg_expression('1')
        self.assertEqual(expect_set, actual_set)

    def test_send_wrong_type_of_data_and_expect_error(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, reg_expression(None))
        exception_message = str(context.exception)
        self.assertEqual('first argument must be string or compiled pattern', exception_message)

    def test_send_days_pattern_and_expect_date_(self):
        expect_set = ['ABC 67-8945 12-01-2009']
        actual_set = reg_expression('\d{2}-\d{2}-\d{4}')
        self.assertEqual(expect_set, actual_set)

import unittest
import re
from regex_query_tool_main import pattern_using_for_string


class RegexQueryToolTest(unittest.TestCase):

    def test_regex_query_tool_with_none_and_int_values(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, pattern_using_for_string(None, 2))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_regex_query_tool_with_int_values(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, pattern_using_for_string(123, 2))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_regex_query_tool_with_list_and_int_values(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, pattern_using_for_string(['1', '2', '3', '4'], 12))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_regex_query_tool_with_list_and_int_values_2(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, pattern_using_for_string(12, ['1', '2', '3', '4']))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_regex_query_tool_wrong_pattern(self):
        with self.assertRaises(re.error) as context:
            self.assertRaises(re.error, pattern_using_for_string('\qdxcw', '12-05-2007'))
        exception_message = str(context.exception)
        self.assertEqual('RegexpError', exception_message)

    def test_regex_query_tool(self):
        given_answer = pattern_using_for_string('\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
        expected_value = ['12-05-2007', '11-11-2011', '12-01-2009'], 'False'
        self.assertEqual(expected_value, given_answer)

    def test_regex_query_tool_2(self):
        given_answer = pattern_using_for_string('\d{2}-\d{2}-(\d{4})', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
        expected_value = ['2007', '2011', '2009'], 'False'
        self.assertEqual(expected_value, given_answer)

    def test_regex_query_tool_3(self):
        given_answer = pattern_using_for_string(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
        expected_value = ['@gmail.com', '@test.in', '@analyticsvidhya.com', '@rest.biz'], 'False'
        self.assertEqual(expected_value, given_answer)

    def test_regex_query_tool_4(self):
        given_answer = pattern_using_for_string('\d{2}-\d{2}-\d{4}', '12-05-2007')
        expected_value = ['12-05-2007'], 'True'
        self.assertEqual(expected_value, given_answer)

    def test_regex_query_tool_5(self):
        given_answer = pattern_using_for_string('qdxcw', '12-05-2007')
        expected_value = [], 'False'
        self.assertEqual(expected_value, given_answer)


if __name__ == '__main__':
    unittest.main()

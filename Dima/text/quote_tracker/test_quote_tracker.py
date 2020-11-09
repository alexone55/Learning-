import os
import unittest
from unittest.mock import patch
from Dima.text.quote_tracker.quote_tracker import input_tracker_parameters
from Dima.text.quote_tracker.quote_tracker import scrap


class QuoteTrackerTest(unittest.TestCase):

    @patch('Dima.text.quote_tracker.quote_tracker.get_chrome_driver')
    @patch('Dima.text.quote_tracker.quote_tracker.get_data_from_url',
           side_effect=[('NSDAP', 14.88, '2020-10-26-21.56.33'),
                        ('NSDAP', 12.23, '2020-10-26-21.56.34'),
                        ('NSDAP', 13.12, '2020-10-26-21.56.35'),
                        ('NSDAP', 14.88, '2020-10-26-21.56.36')])
    def setUp(self, mocked_get_data_from_url, mocked_chrome_driver):
        driver = mocked_chrome_driver()
        scrap('AAPl', 'test_file.csv', driver, 1)

    @patch('Dima.text.quote_tracker.quote_tracker.get_chrome_driver')
    def test_get_chromedriver(self, mock_chrome_driver):
        driver = mock_chrome_driver()
        mock_chrome_driver.assert_called_once()

    @patch('builtins.input', side_effect=('AAPL', 3))
    def test_input_tracker_parameters_using_side_effect(self, mock_input):
        expected = ('AAPL', 3)
        self.assertEqual(input_tracker_parameters(), expected)

    def test_scrap_with_mocked_get_data_from_url(self):
        with open('expected_file.csv') as expected_file:
            expected_data = expected_file.read()
        with open('test_file.csv') as actual_file:
            actual_data = actual_file.read()
        self.assertEqual(expected_data, actual_data)

    def tearDown(self):
        os.remove('test_file.csv')


if __name__ == '__main__':
    unittest.main()

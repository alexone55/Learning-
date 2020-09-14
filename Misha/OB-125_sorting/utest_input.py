import unittest
from main import check_input_data_format


class InputTest(unittest.TestCase):

    def test_input_1(self):
        if check_input_data_format('01003012') == 'Invalid data format':
            test_pass = True
        else:
            test_pass = False
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_input_2(self):
        if check_input_data_format('0hb32') == 'Invalid data format':
            test_pass = True
        else:
            test_pass = False
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_input_3(self):
        if check_input_data_format('13451') == 'Invalid data format':
            test_pass = False
        else:
            test_pass = True
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_input_4(self):
        if check_input_data_format('0') == 'Invalid data format':
            test_pass = True
        else:
            test_pass = False
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_input_5(self):
        if check_input_data_format('7') == 'Invalid data format':
            test_pass = False
        else:
            test_pass = True
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)


if __name__ == '__main__':
    unittest.main()

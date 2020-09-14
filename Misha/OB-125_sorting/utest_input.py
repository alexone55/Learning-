import unittest
from main import check_input_data_format


class InputTest(unittest.TestCase):

    def test_input1(self):
        if check_input_data_format('01003012')=='Invalid data format':
            test_pass=True
        else:
            test_pass=False
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_input2(self):
        if check_input_data_format('0hb32')=='Invalid data format':
            test_pass = True
        else:
            test_pass = False
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_input3(self):
        if check_input_data_format('13451')=='Invalid data format':
            test_pass = False
        else:
            test_pass = True
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_input4(self):
        if check_input_data_format('0')=='Invalid data format':
            test_pass = True
        else:
            test_pass = False
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)

    def test_input5(self):
        if check_input_data_format('7')=='Invalid data format':
            test_pass = False
        else:
            test_pass = True
        self.assertTrue(test_pass == True)
        self.assertFalse(test_pass == False)


if __name__ == '__main__':
    unittest.main()

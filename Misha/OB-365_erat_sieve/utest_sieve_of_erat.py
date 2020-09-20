import unittest
from main import sieve_of_eratosthenes


class EratSieveTest(unittest.TestCase):

    def test_erat_sieve_with_right_parameter_6(self):
        primes = sieve_of_eratosthenes(6)
        expected_result = [2, 3, 5]
        self.assertEqual(expected_result, primes)

    def test_erat_sieve_with_border_parameter_5(self):
        primes = sieve_of_eratosthenes(5)
        expected_result = [2, 3, 5]
        self.assertEqual(expected_result, primes)

    def test_erat_sieve_with_right_parameter_100(self):
        primes = sieve_of_eratosthenes(100)
        expected_result = \
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(expected_result, primes)

    def test_erat_sieve_with_right_parameter_199(self):
        primes = sieve_of_eratosthenes(199)
        expected_result = \
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
             101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
        self.assertEqual(expected_result, primes)

    def test_erat_sieve_with_minimal_parameter(self):
        primes = sieve_of_eratosthenes(2)
        expected_result = [2]
        self.assertEqual(expected_result, primes)

    def test_erat_sieve_with_non_type_object(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, sieve_of_eratosthenes(None))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_erat_sieve_with_string_object(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, sieve_of_eratosthenes(' wdcwd'))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)

    def test_erat_sieve_with_list_object(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, sieve_of_eratosthenes([1, 3]))
        exception_message = str(context.exception)
        self.assertEqual('TypeError', exception_message)


if __name__ == '__main__':
    unittest.main()

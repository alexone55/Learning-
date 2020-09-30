import unittest
from Dima.Classic_Algorithms.eratosthenes.prime_eratosthenes import sieve_of_eratosthenes


class EratSieveTest(unittest.TestCase):

    def test_erat_sieve_with_right_parameter_10(self):
        primes = sieve_of_eratosthenes(10)
        expected_result = [2, 3, 5, 7]
        self.assertEqual(expected_result, primes)

    def test_erat_sieve_with_border_parameter_0(self):
        primes = sieve_of_eratosthenes(0)
        expected_result = []
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

    def test_erat_sieve_with_none_type_object(self):
        self.assertRaises(TypeError, sieve_of_eratosthenes, None)

    def test_erat_sieve_with_string_object(self):
        self.assertRaises(TypeError, sieve_of_eratosthenes, 'asdfd')

    def test_erat_sieve_with_list_object(self):
        self.assertRaises(TypeError, sieve_of_eratosthenes, [1, 6, 4])

    def test_erat_sieve_with_negative_number(self):
        self.assertRaises(ValueError, sieve_of_eratosthenes, -100)


if __name__ == '__main__':
    unittest.main()

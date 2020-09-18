import unittest
from main import sieve_of_eratosthenes


class EratSieveTest(unittest.TestCase):

    def test_erat_sieve_with_right_parameter(self):
        primes = sieve_of_eratosthenes(6)
        expected_result = [2, 3, 5]
        self.assertEqual(expected_result, primes)

    def test_erat_sieve_with_border_parameter(self):
        primes = sieve_of_eratosthenes(5)
        expected_result = [2, 3, 5]
        self.assertEqual(expected_result, primes)

    def test_erat_sieve_with_minimal_parameter(self):
        primes = sieve_of_eratosthenes(2)
        expected_result = [2]
        self.assertEqual(expected_result, primes)

    def test_erat_sieve_with_non_type_object(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, sieve_of_eratosthenes(None))
        the_exception = str(context.exception)
        self.assertEqual('TypeError', the_exception)

    def test_erat_sieve_with_string_object(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, sieve_of_eratosthenes(' wdcwd'))
        the_exception = str(context.exception)
        self.assertEqual('TypeError', the_exception)

    def test_erat_sieve_with_list_object(self):
        with self.assertRaises(TypeError) as context:
            self.assertRaises(TypeError, sieve_of_eratosthenes([1, 3]))
        the_exception = str(context.exception)
        self.assertEqual('TypeError', the_exception)


if __name__ == '__main__':
    unittest.main()

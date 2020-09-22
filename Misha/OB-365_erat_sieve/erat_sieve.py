import time


def show_time_of_function_processing(func):

    def wrapper_with_arguments(arg1):
        start = time.time()
        data = func(arg1)
        end = time.time()
        print('[*] Time used: {} seconds.'.format(end - start))
        return data
    return wrapper_with_arguments


@show_time_of_function_processing
def sieve_of_eratosthenes(number_of_last_prime):
    try:
        numbers = list(range(2, number_of_last_prime + 1))
        for number in numbers:
            if number != 0:
                for expected in range(2 * number, number_of_last_prime + 1, number):
                    numbers[expected - 2] = 0
        primes = []
        for number in numbers:
            if number != 0:
                primes.append(number)
        return primes
    except TypeError:
        raise TypeError('TypeError')


def input_number_prime():
    number_of_prime = input('Enter the number to make border of the prime finding: ')
    try:
        return int(number_of_prime)
    except ValueError:
        raise ValueError('ValueError')


def main():
    number_prime = input_number_prime()
    print('Finding primes...')
    primes = sieve_of_eratosthenes(number_prime)
    print('Primes:\n', primes)


if __name__ == "__main__":
    main()

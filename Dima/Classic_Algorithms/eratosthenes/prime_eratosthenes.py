import math
from Dima.Decorators.time_decorator import timer


@timer
def sieve_of_eratosthenes(number):
    primes = []
    try:
        number = int(number)
    except ValueError:
        raise ValueError('ValueError')
    try:
        for current_number in range(2, number + 1):
            primes.append(current_number)
        current_number = 2
        while current_number <= int(math.sqrt(number)):
            if current_number in primes:
                for repeated_number in range(current_number * 2, number + 1, current_number):
                    if repeated_number in primes:
                        primes.remove(repeated_number)
            current_number = current_number + 1
        return primes
    except TypeError:
        raise TypeError('TypeError')


def main():
    number = input('Enter Number: ')
    print(sieve_of_eratosthenes(number))


if __name__ == "__main__":
    main()

import math
from Dima.Decorators.time_decorator import timer


@timer
def sieve_of_eratosthenes(number):
    primes = []
    try:
        for i in range(2, number + 1):
            primes.append(i)
        i = 2
        while i <= int(math.sqrt(number)):
            if i in primes:
                for j in range(i * 2, number + 1, i):
                    if j in primes:
                        primes.remove(j)
            i = i + 1
        return primes
    except TypeError:
        return []


def main():
    number = int(input('Enter Number: '))
    print(sieve_of_eratosthenes(number))


if __name__ == "__main__":
    main()


def main():
    n = int(input("Type number: "))
    print(factorization_func(n))


def factorization_func(n):
    if n == 0:

        return []
    i = 2
    while i <= n:
        while not n % i:
            return [i] + factorization_func(n // i)
    i += 1

    factorization_func(n)


if __name__ == '__main__':
    main()
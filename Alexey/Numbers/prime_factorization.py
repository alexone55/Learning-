def main():

    n = int(input("Type number: "))
    factorization_func(n)


def factorization_func(n):
    i = 2
    factors = []

    while i <= n:
        if n % i == 0:
            factors.append(i)
            n = n / i
        else:
            i = i + 1

    print(*factors)


if __name__ == '__main__':
    main()


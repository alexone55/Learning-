def main():
    n = int(input("Type number: "))
    i = 2
    print(factorization_func(n, i))


def factorization_func(i, n):
    if i < n:
        return []
    if i % n == 0:
        return [n] + factorization_func(i / n, 2)
    return factorization_func(i, n + 1)



if __name__ == '__main__':
    main()
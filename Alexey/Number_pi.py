def main():
    digit = int(input("Please type count of digits: "))
    number_pi(digit)


def number_pi(digit):

    pi = 1

    for i in range(1, 100000000):
        pi += ((-1) ** i) * (1 / (2 * i +1))

    result = pi * 4
    print(round(result, digit))


if __name__ == '__main__':
    main()
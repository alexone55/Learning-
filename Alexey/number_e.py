def main():
    digit = int(input("Please type count of digits: "))
    number_e(digit)


def number_e(digit):
    i = 100000000
    e = (1 + 1 / i) ** i
    print(round(e, digit))


if __name__ == '__main__':
    main()
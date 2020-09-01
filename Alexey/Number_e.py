def main():
    digit = int(input("Please type count of digits: "))
    number_e(digit)

def number_e(digit):
    e = 0

    for i in range(1, 100000000):
        e += ((1+(1/ i)) ** i)
        e = e / i

    result = e
    print(round(result, digit))


if __name__ == '__main__':
    main()
def main():
    digit = int(input("Please type count of digits: "))
    print(fibonacci(digit))


def fibonacci(digit):
    if digit == 0:
        return 0
    elif digit == 1:
        return 1
    else:
        return fibonacci(digit - 1) + fibonacci(digit - 2)


if __name__ == '__main__':
    main()

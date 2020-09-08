def main():
    answer = input("Choose operation d/m/e/a/r: ")


def divide():
    x = int(input("Type number:"))
    y = int(input("Type number:"))
    z = x / y
    print("Result is " + str(z))


def multiplying():
    x = int(input("Type number:"))
    y = int(input("Type number:"))
    z = x * y
    print("Result is " + str(z))


def extracting():
    x = int(input("Type number:"))
    y = int(input("Type number:"))
    z = x - y
    print("Result is " + str(z))


def root():
    x = int(input("Type number:"))
    z = x * x
    print("Result is " + str(z))


def adding():
    x = int(input("Type number:"))
    y = int(input("Type number:"))
    z = x + y
    print("Result is " + str(z))


if __name__ == '__main__':
    main()
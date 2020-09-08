def main():
    answer = input("Choose operation d/m/e/a/r: ")
    if answer.lower() == 'd':
        divide()
    elif answer.lower() == 'm':
        multiplying()
    elif answer.lower() == 'e':
        extracting()
    elif answer.lower() == 'a':
        adding()
    elif answer.lower() == 'r':
        root()
    else:
        print("WOW! ALIEN CALCULATION!")
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
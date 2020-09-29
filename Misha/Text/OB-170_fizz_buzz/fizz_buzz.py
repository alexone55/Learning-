def print_numbers():
    last_number = 100
    for number in range(last_number):
        if (number + 1) % 3 == 0 and (number + 1) % 5 != 0:
            print('Fizz', end=' ')
        elif (number + 1) % 5 == 0 and (number + 1) % 3 != 0:
            print('Buzz', end=' ')
        elif (number + 1) % 5 == 0 and (number + 1) % 3 == 0:
            print('FizzBuzz', end=' ')
        else:
            print(number + 1, end=' ')


def main():
    print('This is a Fizz Buzz program')
    print_numbers()


if __name__ == "__main__":
    main()

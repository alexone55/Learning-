def main():
    number = int(input())
    print(fizzbuzz_printer(number))


def fizzbuzz_printer(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return 'Not FizzBuzz'


if __name__ == '__main__':
    main()

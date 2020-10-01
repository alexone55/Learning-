def main():
    numbers = int(input())
    print(fizzbuzz_cycle(numbers))


def fizzbuzz_cycle(numbers):
    fizz_buzz_numbers = []
    for number in range(1, numbers + 1):
        fizz_buzz_numbers.append(fizzbuzz_printer(number))
    return fizz_buzz_numbers


def fizzbuzz_printer(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)


if __name__ == '__main__':
    main()

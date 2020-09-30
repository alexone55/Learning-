def main():
    numbers = int(input())
    fizzbuzz_cicle(numbers)


def fizzbuzz_cycle(numbers):

    for number in range(1, numbers + 1):
        fizzbuzz_printer(number)


def fizzbuzz_printer(number):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
    elif number % 3 == 0:
        print('Fizz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)


if __name__ == '__main__':
    main()

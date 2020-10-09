def fizz_buzz(number):
    if type(number) != int:
        raise TypeError('TypeError')
    else:
        if number % 3 == 0 and number % 5 != 0:
            return 'Fizz'
        elif number % 5 == 0 and number % 3 != 0:
            return 'Buzz'
        elif number % 5 == 0 and number % 3 == 0:
            return 'FizzBuzz'
        else:
            return 'Number'


def print_numbers():
    last_number = 100
    for number in range(last_number):
        answer = fizz_buzz(number+1)
        if answer == 'Number':
            print(number+1,end=' ')
        else:
            print(answer,end=' ')


def main():
    print('This is a Fizz Buzz program')
    print_numbers()


if __name__ == "__main__":
    main()

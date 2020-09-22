def calculate_division_by_two(number):
    if number == 1:
        print('Entered number is a power of 2.')
    elif number % 2 == 0:
        number = number / 2
        calculate_division_by_two(number)
    else:
        print('Entered number is NOT a power of 2.')


def main():
    print('This program define, if entered number is a power of 2.')
    number = int(input('Enter positive int value: '))
    calculate_division_by_two(number)


if __name__ == "__main__":
    main()

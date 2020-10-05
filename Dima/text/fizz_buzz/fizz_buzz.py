def check_fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def cycle_fizzbuzz(number):
    fizzbuzz = []
    for i in range(number+1):
        fizzbuzz.append(check_fizzbuzz(i))
    return fizzbuzz


def main():
    try:
        number = int(input('Enter your number: '))
        print(cycle_fizzbuzz(number))
    except ValueError:
        raise ValueError('Number isn`t int type: ')


if __name__ == "__main__":
    main()

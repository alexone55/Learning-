class FizzBuzzException(BaseException):

    def __init__(self, number, message="Number isn`t FizzBuzzS"):
        self.number = number
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}:  {self.number}'


def get_fizzbuzz_or_value_otherwise(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz", number
    elif number % 3 == 0:
        return "Fizz", number
    elif number % 5 == 0:
        return "Buzz", number
    else:
        raise FizzBuzzException(number)


def cycle_fizzbuzz(number):
    fizzbuzz = []
    try:
        for i in range(number+1):
            try:
                fizzbuzz.append(get_fizzbuzz_or_value_otherwise(i))
            except FizzBuzzException:
                continue
        return fizzbuzz
    except TypeError:
        raise TypeError('Number isn`t int type: ')


def main():
    try:
        number = int(input('Enter your number: '))
        print(cycle_fizzbuzz(number))
    except ValueError:
        raise ValueError('Number isn`t int type: ')


if __name__ == "__main__":
    main()

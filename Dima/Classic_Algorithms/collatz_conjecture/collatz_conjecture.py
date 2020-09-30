from Dima.Decorators.time_decorator import timer


@timer
def collatz_conjecture(number):
    try:
        step = int(0)
        if number < 1:
            return []
        while number > 1:
            if number % 2 == 0:
                number = number / 2
            else:
                number = 3 * number + 1
            step += 1
        return step
    except TypeError:
        raise TypeError('TypeError')


def main():
    number = int(27)
    print('Collatz conjecture number of steps: ', collatz_conjecture(number))


if __name__ == "__main__":
    main()

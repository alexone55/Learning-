import math


def main():
    answer = input("Which example do you want to solve: 1/2/3/4/5/6/7: ")
    x = input("Enter f(x): ")
    if x == "inf":
        x = math.inf
    elif x == "-inf":
        x = -math.inf
    else:
        x = float(x)

    if answer == '1':
        first = lambda x: (x - 2) / \
                          (x ** 2 - 3 * x + 2)
        print(first(x))
    elif answer == '2':
        second = lambda x: (x * 3 + x * 4 - 1) / \
                           (2 * x ** 5 + x - x ** 2)
        print(second(x))
    elif answer == '3':
        third = lambda x: (math.sqrt(x - 2) - math.sqrt(x))
        print(third(x))

    elif answer == '4':
        fourth = lambda x: ((7 * x - 10) /
                            (1 + 7 * x)) ** x / 3
        print(fourth(x))

    elif answer == '5':
        fifth = lambda x: math.sin(x) / x ** 3
        print(fifth(x))
    elif answer == '6':
        sixth = lambda x: math.log(x - 1 /
                                   x + 1)
        print(sixth(x))
    elif answer == '7':
        seventh = lambda x: (math.sin(x)) / (math.e ** x - 1)
        print(seventh(x))


def calc_lim(form):
    pass


if __name__ == '__main__':
    main()

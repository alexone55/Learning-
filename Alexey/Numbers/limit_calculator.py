import math
import cmath


def main():
    answer = int(input("Which problem do you want to solve from 1 to 7: "))
    x = input("Enter f(x) (if its infinity try inf or -inf): ")
    if x == "inf":
        x = math.inf
    elif x == "-inf":
        x = -math.inf
    else:
        x = float(x)
    formulas = [lambda x: ((x - 2) / (x ** 2 - 3 * x + 2)) ** 2,
                lambda x: (x * 3 + x * 4 - 1) / (2 * (x ** 5) + x - x ** 2),
                lambda x: ((x - 2) ** (1 / 2) - x ** (1 / 2)),
                lambda x: ((7 * x + 10) / (1 + 7 * x)) ** (x / 3),
                lambda x: (math.sin(x)) / (x ** 3),
                lambda x: math.log((x - 1) / (x + 1), math.e),
                lambda x: (math.sin(x)) / (math.e ** x - 1)]

    calculation = formulas[answer - 1]
    print("Limit is: " + str(round(calculation_limit(x, calculation), 1)))


def calculation_limit(x, calculation):
    limit_is = 0
    if x == 2:
        limit_is = calculation(0.000000000000000001)
        return limit_is
    elif x == -math.inf:
        try:
            list_of_arguments = [-1 * 10 ** i for i in range(14)]
            for id, i in enumerate(list_of_arguments):
                limit_is = calculation(list_of_arguments[id])
            return limit_is
        except ZeroDivisionError:
            list_of_arguments = [-1.1 * 10 ** i for i in range(14)]
            for id, i in enumerate(list_of_arguments):
                limit_is = calculation(list_of_arguments[id])
            return limit_is
    elif x == math.inf:
        list_of_arguments = [1 * 10 ** i for i in range(14)]
        for id, i in enumerate(list_of_arguments):
            limit_is = calculation(list_of_arguments[id])
        return limit_is
    else:
        list_of_arguments = [0 + 1 * 10 ** -i for i in range(14)]
        for id, i in enumerate(list_of_arguments):
            limit_is = calculation(list_of_arguments[id])
        return limit_is


if __name__ == '__main__':
    main()

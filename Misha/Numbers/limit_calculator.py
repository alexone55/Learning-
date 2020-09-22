import math


def find_limit_value(argument_list, function):
    limit = 0
    for i in range(len(argument_list)):
        limit = function(argument_list[i])
    return limit


def limit_f_1(argument):
    print('function: (x - 2) / (x ** 2 - 3 * x + 2)')
    function = lambda x: (x - 2) / (x ** 2 - 3 * x + 2)
    argument_list = [argument + 1 * 10 ** (-i) for i in range(14)]
    return find_limit_value(argument_list, function)


def limit_f_2(argument):
    function = lambda x: (x ** 3 + x ** 4 - 1) / (2 * (x ** 5) + x - x ** 2)
    argument_list = [argument - 1 * 10 ** (i) for i in range(14)]
    return find_limit_value(argument_list, function)


def limit_f_3(argument):
    function = lambda x: (x - 2) ** (1 / 2) - x ** (1 / 2)
    argument_list = [argument + 1 * 10 ** (i) for i in range(14)]
    return find_limit_value(argument_list, function)


def limit_f_4(argument):
    function = lambda x: ((7 * x + 10) / (1 + 7 * x)) ** (x / 3)
    argument_list = [argument + 1 * 10 ** i for i in range(14)]
    return find_limit_value(argument_list, function)


def limit_f_5(argument):
    function = lambda x: math.sin(x) / (x ** 3)
    argument_list = [argument + 1 * 10 ** (-i) for i in range(14)]
    return find_limit_value(argument_list, function)


def limit_f_6(argument):
    function = lambda x: math.log((x - 1) / (x + 1), math.e)
    argument_list = [argument - 1.1 * 10 ** (i) for i in range(14)]
    return find_limit_value(argument_list, function)


def limit_f_7(argument):
    function = lambda x: math.sin(x) / (math.exp(x) - 1)
    argument_list = [argument + 1 * 10 ** (-i) for i in range(14)]
    return find_limit_value(argument_list, function)


def main():
    print('This program is a limit calculator')
    """хардкода в словаре избежать не удалось, так как при подстановке 
    argument_limits[index] в функцию в словаре появлялась ошибка"""
    x_goes_to = ('2', '-inf', 'inf', 'inf', '0', '-inf', '0')
    function_number = int(input('Enter number of function (1-7): '))
    functions_map = {1: limit_f_1(2),
                     2: limit_f_2(0),
                     3: limit_f_3(0),
                     4: limit_f_4(0),
                     5: limit_f_5(0),
                     6: limit_f_6(0),
                     7: limit_f_7(0)}
    limit = round(functions_map[function_number], 2)
    if limit >= 10 ** 10:
        limit = 'inf'
    elif limit <= -(10 ** 10):
        limit = '-inf'
    print('x -> ' + x_goes_to[function_number-1])
    print('limit: ', limit)


if __name__ == "__main__":
    main()

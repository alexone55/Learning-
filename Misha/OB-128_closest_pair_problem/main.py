import re
import random
import time


def create_route_matrix(dot_list):
    route_matrix = [[0] * len(dot_list) for index in range(len(dot_list))]
    for index_row in range(len(dot_list)):
        for index_col in range(index_row, len(dot_list)):
            try:
                route_matrix[index_row][index_col] = ((dot_list[index_row][0] - dot_list[index_col][0]) ** 2 +
                                                      (dot_list[index_row][1] - dot_list[index_col][1]) ** 2) ** (1 / 2)
            except TypeError:
                raise TypeError('TypeError')
    return route_matrix


def check_input_data_format(value):
    if not re.fullmatch(r'[1-9]{1,}\d{0,}', value) or re.fullmatch(r'[1]', value) or value is None:
        return 'Invalid data format'


def generate_dot_list(amount_of_dots):
    random.seed = time.time()
    try:
        dot_list = [[0] * 2 for index in range(amount_of_dots)]
    except TypeError:
        raise TypeError('TypeError')
    for index in range(amount_of_dots):
        x = random.randint(-1 * amount_of_dots, amount_of_dots)
        y = random.randint(-1 * amount_of_dots, amount_of_dots)
        dot_list[index][0] = x
        dot_list[index][1] = y
    return dot_list


def find_min_route(route_matrix):
    int_var = int(1)
    string_var = 'qwerty'
    if route_matrix is None or type(route_matrix) == type(int_var) or type(route_matrix) == type(string_var):
        raise TypeError('TypeError')
    else:
        min_route = route_matrix[0][1]
        dot_1 = 0
        dot_2 = 1
        for index_row in range(len(route_matrix)):
            for index_col in range(len(route_matrix)):
                try:
                    if route_matrix[index_row][index_col] != 0:
                        if min_route > route_matrix[index_row][index_col]:
                            min_route = route_matrix[index_row][index_col]
                            dot_1 = index_row
                            dot_2 = index_col
                except TypeError:
                    raise TypeError('TypeError')
        return dot_1, dot_2, min_route


def main():
    amount_of_dots = input('Enter the number of dots: ')
    if check_input_data_format(amount_of_dots) != 'Invalid data format':
        dot_list = generate_dot_list(5)
        route_matrix = create_route_matrix(dot_list)
        dot_1, dot_2, min_route = find_min_route(route_matrix)
        print('Min route between dots: ')
        print('A(' + str(dot_list[dot_1][0]) + '; ' + str(dot_list[dot_1][1]) + ')')
        print('B(' + str(dot_list[dot_2][0]) + '; ' + str(dot_list[dot_2][1]) + ')')
        print('Min route', min_route)


if __name__ == "__main__":
    main()

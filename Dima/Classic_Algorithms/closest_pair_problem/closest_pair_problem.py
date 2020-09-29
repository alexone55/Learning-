import math
from Dima.Decorators.time_decorator import timer


def create_route_matrix(dot_list):
    try:
        route_matrix = [[0] * len(dot_list) for index in range(len(dot_list))]
        for index_row in range(len(dot_list)):
            for index_col in range(index_row+1, len(dot_list)):
                try:
                    route_matrix[index_row][index_col] = ((dot_list[index_row][0] - dot_list[index_col][0]) ** 2 +
                                                          (dot_list[index_row][1] - dot_list[index_col][1]) ** 2) ** (1 / 2)
                except TypeError:
                    raise TypeError('TypeError')
    except TypeError:
        raise TypeError('TypeError')
    return route_matrix


def find_min_route(route_matrix):
    if isinstance(route_matrix, list):
        min_route = route_matrix[0][1]
        dot_1 = 0
        dot_2 = 1
        for index_row in range(len(route_matrix)):
            for index_col in range(len(route_matrix)):
                try:
                    if index_row < index_col:
                        if min_route > route_matrix[index_row][index_col]:
                            min_route = route_matrix[index_row][index_col]
                            dot_1 = index_row
                            dot_2 = index_col
                except TypeError:
                    raise TypeError('TypeError')
    else:
        raise TypeError('TypeError')
    return dot_1, dot_2, min_route


@timer
def main():
    dot_list = [[0, 1], [1, 0], [0, 0], [2, 4], [0, 0]]
    route_matrix = create_route_matrix(dot_list)
    print(*dot_list)
    print('Closest pair of dots: ', find_min_route(route_matrix))


if __name__ == "__main__":
    main()


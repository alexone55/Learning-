import math


def main():
    dots = {'A': (16, 10), 'B': (136, 19), 'C': (6, 83), 'D': (8, 36)}

    print(lets_find_minimum_distance(dots))


def lets_find_minimum_distance(dots):
    min_distance = {}
    count_of_dots = len(dots)
    if isinstance(dots, dict):
        if count_of_dots > 1:
            for dot, dot_keys in zip(dots.values(), dots.keys()):
                for another_dot, another_dot_keys in zip(dots.values(), dots.keys()):
                    if dot != another_dot:
                        min_distance[str(dot_keys) + ":"
                                     + str(another_dot_keys)] = lets_find_dots_distance(dot[0], dot[1],
                                                                                        another_dot[0],
                                                                                        another_dot[1])
            return min(min_distance, key=min_distance.get), min(min_distance.values())
        else:
            alert = "You have just one dot"
            return alert
    else:
        raise TypeError('This is not dict')


def lets_find_dots_distance(x1, y1, x2, y2):
    delta_x = x1 - x2
    delta_y = y1 - y2
    distance = math.sqrt(abs(delta_x) ** 2 +
                         abs(delta_y) ** 2)
    return distance


if __name__ == '__main__':
    main()

import math


def main():
    dots = [(1, 2), (3, 6), (3, 12)]
    min_distance = { }

    for dot in dots:
        for another_dot in dots:
            if dot != another_dot:
                lets_find_dots_distance(dot[0], dot[1],
                                                        another_dot[0],
                                                        another_dot[1]))
    print(min(min_distance))


def lets_find_dots_distance(x1, y1, x2, y2):
    delta_x = x1 - x2
    delta_y = y1 - y2
    distance = math.sqrt(abs(delta_x) ** 2 +
                         abs(delta_y) ** 2)
    # print(distance)

    return distance


if __name__ == '__main__':
    main()

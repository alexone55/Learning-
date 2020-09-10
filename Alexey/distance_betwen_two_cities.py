import math


def main():
    print("Coordinates of first city x,y")
    x1 = int(input())
    y1 = int(input())
    print("Coordinates of second city x,y")
    x2 = int(input())
    y2 = int(input())
    lets_find_city_distance(x1, y1, x2, y2)


def lets_find_city_distance(x1, y1, x2, y2):
    delta_x = x1 - x2
    delta_y = y1 - y2
    distance = math.sqrt(abs(delta_x) ** 2 +
                         abs(delta_y) ** 2)

    print(distance)


if __name__ == '__main__':
    main()
def main():
    array = [2, 4, 1, 5, 7, 3, 8, 9]
    print(*array)
    print(sort(array))


def sort(array):
    for i in array:
        for id_y, y in enumerate(array):
            if array[id_y] > array[id_y + 1]:
                array[id_y], array[id_y + 1] = array[id_y + 1], array[id_y]
    return array


if __name__ == '__main__':
    main()
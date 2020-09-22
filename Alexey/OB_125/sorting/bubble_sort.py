from Alexey.OB_125.sorting.time_decorator import timer


@timer
def main():
    array = []
    print(*array)
    print(sort(array))


def sort(array):
    try:
        for i in range(len(array)-1, 0, -1):
            for y in range(i):
                if array[y] > array[y + 1]:
                    array[y], array[y + 1] = array[y + 1], array[y]
        return array
    except TypeError:
        return []


if __name__ == '__main__':
    main()

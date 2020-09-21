def main():
    array = [2, 4, 1, 5, 7, 3, 8, 9]
    print(*array)
    print(sort(array))


def sort(sorted):
    try:
        if len(sorted) > 1:
            middle = len(sorted) // 2
            left_side = sorted[:middle]
            right_side = sorted[middle:]
            left_side = sort(left_side)
            right_side = sort(right_side)

            sorted = []

            while len(left_side) > 0 \
                    and len(right_side) > 0:

                if left_side[0] < right_side[0]:
                    sorted.append(left_side[0])
                    left_side.pop(0)
                else:
                    sorted.append(right_side[0])
                    right_side.pop(0)

            for i in left_side:
                sorted.append(i)

            for i in right_side:
                sorted.append(i)
        return sorted
    except TypeError:
        return []

if __name__ == '__main__':
    main()

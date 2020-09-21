from Dima.Numbers.time_decorator import timer
import random


def merge_sort(unsorted_list):
    try:
        if len(unsorted_list) <= 1:
            return unsorted_list
        mid = len(unsorted_list) // 2
        left, right = merge_sort(unsorted_list[:mid]), merge_sort(unsorted_list[mid:])

        return merge(left, right, unsorted_list.copy())
    except TypeError:
        return [] 


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):

        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged


@timer
def main():
    unsorted_list = random.sample(range(0, 1000), 1000)
    print('Random list: ', *unsorted_list)
    print('Sorted list: ', *merge_sort(unsorted_list))


if __name__ == "__main__":
    main()

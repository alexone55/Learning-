import random
import time
import re


def bubble_sort(array_to_sort):
    arr = array_to_sort.copy()
    array_size = len(arr)
    for index_1 in range(array_size - 1):
        for index_2 in range(array_size - 1 - index_1):
            if arr[index_2] > arr[index_2 + 1]:
                arr[index_2], arr[index_2 + 1] = arr[index_2 + 1], arr[index_2]
    return arr


def merge_sort_iterative(array_to_sort):
    arr = array_to_sort.copy()
    step = 1  # sequence partition counter
    array_size = len(arr)
    temp_arr = [0] * array_size
    while step < array_size:
        res_index = 0  # result array index
        left_index = 0  # left border of sequence
        middle_index = left_index + step  # middle of sequence
        right_index = left_index + step * 2  # right border of sequence
        while left_index < array_size:  # while left border is valide
            if middle_index >= array_size:
                middle_index = array_size
            if right_index >= array_size:
                right_index = array_size
            i1 = left_index  # index of first comparsion element
            i2 = middle_index  # index of second comparsion element
            while i1 < middle_index and i2 < right_index:  #
                if arr[i1] < arr[i2]:
                    temp_arr[res_index] = arr[i1]
                    res_index += 1
                    i1 += 1
                else:  # filling the result sequence array
                    temp_arr[res_index] = arr[i2]
                    res_index += 1
                    i2 += 1
            # after the previous "while" we are filling the rest of sorting sequence array
            while i1 < middle_index:
                temp_arr[res_index] = arr[i1]
                res_index += 1
                i1 += 1
            while i2 < right_index:
                temp_arr[res_index] = arr[i2]
                res_index += 1
                i2 += 1
            # going to the next sequence to sort
            left_index += step * 2
            middle_index += step * 2
            right_index += step * 2
        arr = temp_arr.copy()  # filling the rest of result sequence
        step *= 2  # increasing the step of partition
    return arr


def check_input_data_format(value):
    if not re.fullmatch(r'[1-9]{1,}\d{0,}', value):
        return 'Invalid data format'


def main():
    random.seed = time.time()
    array_size = input('Enter the int number to set the array size: ')
    if check_input_data_format(str(array_size)) != 'Invalid data format':
        array_size = int(array_size)
        arr_to_sort = [0] * array_size
        for index in range(array_size):
            arr_to_sort[index] = random.randint(1, array_size)

        print('Array:\n', arr_to_sort)
        start = time.time()
        sorted_array = bubble_sort(arr_to_sort)
        end = time.time()
        print('Sorted Array:\n', sorted_array)
        sort_time = end - start
        print('Sort time (bubble sort): ', sort_time)  # on small values of array size (10 for example) time reach 0

        print('Array:\n', arr_to_sort)
        start = time.time()
        sorted_array = merge_sort_iterative(arr_to_sort)
        end = time.time()
        print('Sorted Array:\n', sorted_array)
        sort_time = end - start
        print('Sort time (iterative merge sort): ', sort_time)


if __name__ == "__main__":
    main()

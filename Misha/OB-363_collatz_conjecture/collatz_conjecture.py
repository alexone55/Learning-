import time
import re


def show_time_of_function_processing(func):
    def wrapper_with_arguments(arg1):
        start = time.time()
        data = func(arg1)
        end = time.time()
        print('[*] Time used: {} seconds.'.format(end - start))
        return data

    return wrapper_with_arguments


@show_time_of_function_processing
def collatz_conjecture(value):
    check_input_data_format(value)

    iterations = 0
    value = int(value)
    print('value[' + str(iterations) + ']: \t' + str(value))
    while value != 1:
        if value % 2 == 0:
            value /= 2
        else:
            value = value * 3 + 1
        iterations += 1
        print('value[' + str(iterations) + ']: \t' + str(value))
    return iterations


def check_input_data_format(value):
    if value is None or not re.fullmatch(r'[1-9]{1,}\d{0,}', value) or re.fullmatch(r'[1]', value):
        raise TypeError('Invalid data format')
    else:
        pass


def main():
    start_value = input('Enter the number to start: ')
    iterations = collatz_conjecture(start_value)
    print(str(iterations) + ' iterations to reach number 1.')
    return 0


if __name__ == "__main__":
    main()

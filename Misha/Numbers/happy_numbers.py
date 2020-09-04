def find_sum_of_digits(number, recursion_call):
    summ = 0
    # print(number,end=' ')
    for index in range(len(str(number))):
        summ += ((number % 10) ** 2)
        number = number // 10
    # print(summ)
    if summ != 1:
        # print('HUETA')
        if recursion_call < 10:
            recursion_call += 1
            summ = find_sum_of_digits(summ, recursion_call)
    # почему summ=1 но возвращается первое найденное summ
    return summ


def find_happy_number(n):
    happy_numbers_array = []
    number = 1
    while len(happy_numbers_array) != n:
        print('num in loop: ' + str(number))
        # num_in_loop=number
        recursion_call = 0  # variable to avoid endless loops
        summ = find_sum_of_digits(number, recursion_call)
        # print('nums_in_find_happy_numbers: ', end='')
        # print(number,summ)
        if summ == 1:
            happy_numbers_array.append(number)
        number += 1
    print('Happy numbers: ')
    print(happy_numbers_array)
    return 0


if __name__ == "__main__":
    print('This program finds happy numbers\n')
    print('Recursion depth is set to 10.')
    n = int(input('Enter N to find first N happy numbers: '))
    find_happy_number(n)

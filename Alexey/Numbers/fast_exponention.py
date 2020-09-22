def main():
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    o_log_n(power_of_nums(a, b))


def o_log_n(result):
    temp = result
    big_o = 0
    while temp > 1:
        temp = temp // 2
        big_o += 1
    print('Complexity is: ' + str(big_o))


def power_of_nums(a, b):
    result = 1
    if b != 0:
        for index in range(b):
            result = result * a
    print('Power of nums is ' + str(result))
    return result


if __name__ == '__main__':
    main()
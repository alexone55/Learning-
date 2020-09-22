def main():
    first_num_part_a = int(input("Enter first real number: "))
    second_num_part_a = int(input("Enter first imaginary number: "))
    first_num_part_b = int(input("Enter second real number: "))
    second_num_part_b = int(input("Enter second imaginary number: "))
    answer = input("Choose operation d/m/s/a/p: ")
    if answer.lower() == 'd':
        divide_complex(first_num_part_a,
                       second_num_part_a,
                       first_num_part_b,
                       second_num_part_b)
    elif answer.lower() == 'm':
        multiply_complex(first_num_part_a,
                         second_num_part_a,
                         first_num_part_b,
                         second_num_part_b)
    elif answer.lower() == 's':
        subtract_complex(first_num_part_a,
                         second_num_part_a,
                         first_num_part_b,
                         second_num_part_b)
    elif answer.lower() == 'a':
        add_complex(first_num_part_a,
                    second_num_part_a,
                    first_num_part_b,
                    second_num_part_b)
    elif answer.lower() == 'p':
        power_complex(first_num_part_a,
                      second_num_part_a,
                      first_num_part_b,
                      second_num_part_b)
    else:
        print("WOW! ALIEN CALCULATION!")

    print(add_complex(first_num_part_a,
                      second_num_part_a,
                      first_num_part_b,
                      second_num_part_b))


def add_complex(first_num_part_a,
                second_num_part_a,
                first_num_part_b,
                second_num_part_b):
    a = complex(first_num_part_a, second_num_part_a)
    b = complex(first_num_part_b, second_num_part_b)
    return a + b


def subtract_complex(first_num_part_a,
                     second_num_part_a,
                     first_num_part_b,
                     second_num_part_b):
    a = complex(first_num_part_a, second_num_part_a)
    b = complex(first_num_part_b, second_num_part_b)
    return a - b


def multiply_complex(first_num_part_a,
                     second_num_part_a,
                     first_num_part_b,
                     second_num_part_b):
    a = complex(first_num_part_a, second_num_part_a)
    b = complex(first_num_part_b, second_num_part_b)
    return a * b


def divide_complex(first_num_part_a,
                   second_num_part_a,
                   first_num_part_b,
                   second_num_part_b):
    a = complex(first_num_part_a, second_num_part_a)
    b = complex(first_num_part_b, second_num_part_b)
    return a / b


def power_complex(first_num_part_a,
                  second_num_part_a,
                  first_num_part_b,
                  second_num_part_b):
    a = complex(first_num_part_a, second_num_part_a)
    b = complex(first_num_part_b, second_num_part_b)
    return a ** b


if __name__ == '__main__':
    main()

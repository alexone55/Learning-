def main():
    num = int(input("Enter number: "))
    if is_happy_number(num):
        print(str(num) + " is a Happy number")
    else:
        print(str(num) + " is not a Happy number")


def num_square_sum(num):
    square_sum = 0
    while num:
        square_sum += (num % 10) * (num % 10)
        num = int(num / 10)
    return square_sum


def is_happy_number(num):
    a = num
    b = num
    while True:
        a = num_square_sum(a)
        b = num_square_sum(num_square_sum(b))
        if a != b:
            continue
        else:
            break
    return a == 1


if __name__ == '__main__':
    main()

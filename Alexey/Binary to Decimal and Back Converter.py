def main():
    answer = input("Type what you want to convert decimal or binary: d/b  ")
    num = input("Type number: ")
    if answer.lower() == 'd':
        decimal_to_binary(num)
    elif answer.lower() == 'b':
        binary_to_decimal(num)


def decimal_to_binary(num):
    print(bin(int(num)))


def binary_to_decimal(num):
    length = len(num)
    decimal = 0
    for i in range(0, length):
        decimal = decimal + int(num[i]) * (2 ** (length - i - 1))
    print(decimal)


if __name__ == "__main__":
     main()
def main():
    num = int(input("Enter number: "))
    print(conjecture(num))


def conjecture(num):
    conjecture_list = []
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            conjecture_list.append(int(num))
        elif num % 2 != 0:
            num = num * 3 + 1
            conjecture_list.append(int(num))

    return conjecture_list


if __name__ == '__main__':
    main()
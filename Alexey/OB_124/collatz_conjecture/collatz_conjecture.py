def main():
    try:
        num = int(input("Enter number: "))
    except ValueError:
        num = 0
    print(conjecture(num))


def conjecture(num):
    conjecture_list = []
    try:
        while num != 1:
            if num == 0:
                return 0
            elif num % 2 == 0:
                num = num / 2
                conjecture_list.append(int(num))
            elif num % 2 != 0:
                num = num * 3 + 1
                conjecture_list.append(int(num))

        return conjecture_list

    except TypeError:
        return conjecture_list


if __name__ == '__main__':
    main()

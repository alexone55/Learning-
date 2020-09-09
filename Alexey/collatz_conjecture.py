def main():
    num = int(input("Enter number: "))
    conjecture(num)


def conjecture(num):
    while num != 1:
        if num % 2 == 0:
          num = num / 2
        elif num % 2 != 0:
            num = num * 3 + 1
        print(int(num))


if __name__ == '__main__':
    main()
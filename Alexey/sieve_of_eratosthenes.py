def main():
    number = int(input("Enter number: "))
    eratosthenes(number)


def eratosthenes(number):
    list_of_numbers = []
    for i in range(2, number + 1):
        list_of_numbers.append(i)
    for i in list_of_numbers:
        for elem in list_of_numbers:
            if elem % i == 0 and elem != i:
                list_of_numbers.remove(elem)
    print(list_of_numbers)


if __name__ == '__main__':
    main()

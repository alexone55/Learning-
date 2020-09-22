from Alexey.OB_366.sieve_of_eratostenes.time_decorator import timer


@timer
def main():
    try:
        number = int(input("Enter number: "))
    except ValueError:
        number = 0
    print(eratosthenes(number))


def eratosthenes(number):
    list_of_numbers = []
    try:
        for i in range(2, number + 1):
            list_of_numbers.append(i)
        for i in list_of_numbers:
            for elem in list_of_numbers:
                if elem % i == 0 and elem != i:
                    list_of_numbers.remove(elem)
        return list_of_numbers

    except TypeError:
        return list_of_numbers




if __name__ == '__main__':
    main()

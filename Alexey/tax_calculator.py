def main():
    cost = int(input("Type number:"))
    tax = int(input("Type number:")) / 100
    tax_calculator(cost, tax)


def tax_calculator(cost, tax):
    percentage = cost * tax
    result = cost + percentage
    print(result)


if __name__ == '__main__':
    main()
def main():
    number = str(input("Enter credit card number: "))
    print("Your vendor is: " + str(check_vendor(number)))
    if checksum(number) == int(number[-1]):
        print('Valid card')
    else:
        print("Card is not valid")


def checksum(number):
    card = number
    card = card[:-1]
    print(card)
    meta_card = []
    meta_card2 = []

    for id, i in enumerate(card, 1):
        if id % 2 != 0:
            i = int(i) * 2
        meta_card.append(i)

    for i in meta_card:
        if int(i) > 9:
            i = i - 9
        meta_card2.append(i)
    sum_of_numbers = 0

    for i in meta_card2:
        sum_of_numbers += int(i)

    checksum = sum_of_numbers // 10
    return checksum


def check_vendor(number):
    length = len(str(number))
    vendor = ()
    if 14 <= length <= 19:

        if int(number[0]) == 4:
            vendor = "Visa"

        elif int(number[0: 2]) in range(51, 55) or \
                int(number[0: 6]) in range(222100, 272100):
            vendor = "Mastercard"

        elif int(number[0: 2]) in range(34, 38):
            vendor = "American Express"

        elif int(number[0: 4]) == 6011 or \
                int(number[0: 3]) in range(644, 650) or \
                int(number[0: 6]) in range(622126, 622926) or \
                int(number[0: 2]) == 65:
            vendor = "Discover"
        else:
            print("The number is NOT valid!")
    else:
        print("The number is NOT valid!")

    return vendor


if __name__ == '__main__':
    main()
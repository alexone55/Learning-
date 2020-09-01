def main():
    answer = input("Choose unit w/h/t: ")
    num = float(input("Number: "))
    if answer.lower() == 'w':
        wight(num)
    elif answer.lower() == 'h':
        height(num)
    elif answer.lower() == 't':
        temperature(num)
    else:
        print("WOW! You type something wrong!")


def wight(num):
    kg = num / 2.2046
    print("Your wight is: " + str(kg) + " kg")


def height(num):
    cm = num / 0.032808
    print(cm)
    print("Your height is: " + str(cm) + " cm")


def temperature(num):
    cels = 273.15 - num
    print("Your temperature is: " + str(cels))


if __name__ == '__main__':
    main()
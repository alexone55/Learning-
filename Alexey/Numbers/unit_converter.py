def main():
    answer = input("Choose unit w/h/t/s: ")
    num = float(input("Number: "))
    if answer.lower() == 'w':
        weight(num)
    elif answer.lower() == 'h':
        height(num)
    elif answer.lower() == 't':
        temperature(num)
    elif answer.lower() == 's':
        speed(num)
    else:
        print("WOW! You type something wrong!")


def weight(num):
    answer = input("What we convert to: kg or lb ")
    if answer.lower() == "kg":
        kg = num / 2.2046
        print("Your weight in kg is: " + str(kg) + " kg")
    elif answer.lower() == "lb":
        lb = num * 2.2046
        print("Your weight in lb is: " + str(lb) + " lb")
    else:
        print("WOW! ALIEN CALCULATION!")


def height(num):
    answer = input("What we convert to: m or ft ")
    if answer.lower() == "m":
        m = num / 3.2808
        print("Your height in m is: " + str(m) + " m")
    elif answer.lower() == "ft":
        ft = num * 3.2808
        print("Your height in ft is: " + str(ft) + " ft")
    else:
        print("WOW! ALIEN CALCULATION!")


def speed(num):
    answer = input("What we convert to: kmh or mph ")
    if answer.lower() == "kmh":
        kmh = num * 1.609
        print("Your speed in kmh is: " + str(kmh) + " kmh")
    elif answer.lower() == "mph":
        mph = num / 1.609
        print("Your speed in mph is: " + str(mph) + " mph")
    else:
        print("WOW! ALIEN CALCULATION!")


def temperature(num):
    answer = input("What we convert to: kelvin or celsius ")
    if answer.lower() == "celsius":
        celsius = 273.15 - num
        print("Your temperature in celsius is: " + str(celsius) + " °C")
    elif answer.lower() == "kelvin":
        kelvin = 273.15 + num
        print("Your temperature in kelvin is: " + str(kelvin) + " K")


if __name__ == '__main__':
    main()

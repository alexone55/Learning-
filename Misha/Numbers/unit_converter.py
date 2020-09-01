def menu():
    print('1. Meters-feets')
    print('2. Celsium-Fahrenheit')
    print('3. Lbs-kg')
    print('4. USD-UAH')
    num = int(input('Enter the number of menu point: '))
    return num


def convert():
    value = float(input('Enter the absolute value: '))
    units = [3.28084, 1.8, 0.453592, 27.49]
    number = menu()
    if number == 1:
        print(str(value) + ' m = ' + str(value * units[number - 1]) + ' f')
        print(str(value) + ' f = ' + str(value / units[number - 1]) + ' m')
    elif number == 2:
        print(str(value) + ' C = ' + str(value * units[number - 1] + 32) + 'F.')
        print(str(value) + ' F = ' + str(value / units[number - 1] - 32) + 'C.')
    elif number == 3:
        print(str(value) + ' LBS = ' + str(value * units[number - 1]) + ' KG')
        print(str(value) + ' KG = ' + str(value / units[number - 1]) + ' LBS')
    elif number == 4:
        print(str(value) + ' USD = ' + str(value * units[number - 1]) + ' UAH')
        print(str(value) + ' UAH = ' + str(value / units[number - 1]) + ' USD')
    return 0


if __name__ == "__main__":
    print('This program converts various units between one another.\n')
    convert()

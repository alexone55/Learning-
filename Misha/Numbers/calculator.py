def calculator():
    value_1 = float(input('Enter the first value: '))
    operator = str(input('Enter the basic operator: '))
    value_2 = float(input('Enter the second value: '))
    if operator == '+':
        result = value_1 + value_2
    elif operator == '-':
        result = value_1 - value_2
    elif operator == '/':
        result = value_1 / value_2
    else:
        result = value_1 * value_2
    print(str(value_1)+' '+operator+ ' '+str(value_2)+' = '+str(result))
    return 0


if __name__ == "__main__":
    print('THis program is a simple calculator to do basic operators\n')
    calculator()

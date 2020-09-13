def is_binary(value):
    check_var = True
    binary_digits_string = "01"
    if value.isdigit():
        if value[0] != '0':
            for i in range(len(value)):
                if str(value[i]) not in binary_digits_string:
                    check_var = False
                    break
    else:
        check_var = True
    return check_var


def main():
    string_value=input('Enter binary value: ')
    if is_binary(string_value):
        dec = 0
        for i in range(len(string_value)):
            dec += int(string_value[i]) * (2 ** (len(string_value) - i - 1))
        print('Decimal: ' + str(dec))
    else:
        print('Input Error!')
    return 0


if __name__ == "__main__":
    main()

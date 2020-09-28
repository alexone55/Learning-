def check_if_palindrome(string_value):
    if type(string_value) != str:
        raise TypeError('TypeError')
    else:
        reversed_string = ''
        string_size = len(string_value)
        for index in range(string_size):
            reversed_string += string_value[string_size - index - 1]
        if reversed_string == string_value:
            return True
        else:
            return False


def main():
    string_to_check = input('Enter string to check: ')
    given_answer = check_if_palindrome(string_to_check)
    if given_answer is True:
        print('Given string is a palindrome')
    else:
        print('Given string is NOT a palindrome')


if __name__ == "__main__":
    main()

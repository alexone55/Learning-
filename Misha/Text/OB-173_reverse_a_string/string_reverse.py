def string_reverser(string):
    if type(string) != str:
        raise TypeError('TypeError')
    else:
        reversed_string = ''
        string_size = len(string)
        print('string to reverse: [' + string + ']')
        for index in range(string_size):
            reversed_string += string[string_size - index - 1]
        print('reversed string: [' + reversed_string + ']')
        return reversed_string


def main():
    string_to_reverse = input('Enter string to reverse: ')
    reversed_string = string_reverser(string_to_reverse)


if __name__ == "__main__":
    main()

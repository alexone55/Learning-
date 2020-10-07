def reverse_a_string(reverse_this_string):
    if isinstance(reverse_this_string, str):
        return reverse_this_string[::-1]
    else:
        raise TypeError('input isn`t str type: ')


def main():
    reverse_this_string = input('Enter string to reverse: ')
    print(reverse_a_string(reverse_this_string))


if __name__ == "__main__":
    main()

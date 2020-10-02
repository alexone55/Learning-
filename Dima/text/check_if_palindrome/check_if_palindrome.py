def check_if_palindrome(palindrome):
    try:
        palindrome = palindrome.replace(" ", "")
        if palindrome == palindrome[::-1]:
            return 'Yes'
        else:
            return 'No'
    except AttributeError:
        raise AttributeError('Input isn`t string type')


def main():
    palindrome = 'abc cba'
    print(check_if_palindrome(palindrome))


if __name__ == "__main__":
    main()

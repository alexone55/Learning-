def check_if_palindrome(palindrome):
    try:
        palindrome = palindrome.strip().replace(" ", "")
        if palindrome == palindrome[::-1]:
            return True
        else:
            return False
    except AttributeError:
        raise AttributeError('Input isn`t string type')


def main():
    palindrome = 'abc c ba'
    print(check_if_palindrome(palindrome))


if __name__ == "__main__":
    main()

import re


def main():
    sentence = int(input("Please input your sentence: "))
    print(check_if_palindrome(sentence))


def check_if_palindrome(sentence):
    sentence = re.sub(r'[^\w]', '', sentence).lower()
    reversed_value = sentence[::-1]
    if sentence == reversed_value:
        return True
    else:
        return False


if __name__ == '__main__':
    main()

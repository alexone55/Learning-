import re


def main():
    sentence = int(input("Please input your sentence: "))
    print(check_if_palindrome(sentence))


def check_if_palindrome(sentence):
    sentence = re.sub(r'[^\w]', '', sentence).lower()
    if sentence == reverse(sentence):
        massage = "Congrats your sentence is palindrome!"
        return massage
    else:
        massage = "This is not palindrome=("
        return massage


def reverse(sentence):
    return sentence[::-1]


if __name__ == '__main__':
    main()

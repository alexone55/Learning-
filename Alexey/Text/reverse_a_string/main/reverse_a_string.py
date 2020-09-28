def main():
    word = input("Enter a word or number: ")
    print(reverse(word))


def reverse(word):
    return str(word[::-1])


if __name__ == '__main__':
    main()

def count_words(string):
    try:
        wordlist = string.split(' ')
    except AttributeError:
        raise AttributeError('AttributeError')
    amount_of_words = 0
    for word in wordlist:
        if (word.isdigit() != True) and (word != '-') and (word != ''):
            print(word)
            amount_of_words += 1
    return amount_of_words


def read_from_file(filename):
    try:
        f = open(str(filename), 'r', encoding='utf-8')
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    text = ''
    for line in f:
        text += line
    print(text)
    return text


def main():
    filename = input('Enter a filename: ')
    text = read_from_file(filename)
    amount_of_words = count_words(text)
    print(amount_of_words)


if __name__ == "__main__":
    main()

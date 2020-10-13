def word_to_pig_latin(word):
    if not isinstance(word, str):
        raise TypeError('Word isn`t string type: ')
    if not word.isalpha():
        raise ValueError('Word contains symbols: ')
    if len(word) > 0:
        if word[0] in "aeiou":
            if word[0].isupper():
                return word.capitalize() + 'yay'
            else:
                return word + 'yay'
        else:
            if word[0].isupper():
                return word[1:].capitalize() + word[0].lower() + 'ay'
            else:
                return word[1:] + word[0] + 'ay'
    else:
        return ''



def main():
    sentence = input('Type what you would like translated into pig-latin: ')
    print(word_to_pig_latin(sentence))


if __name__ == "__main__":
    main()

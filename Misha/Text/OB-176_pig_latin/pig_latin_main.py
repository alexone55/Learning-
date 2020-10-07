def pig_latin_transformation(word):
    word = str(word)
    if not word.isalpha():
        raise TypeError('Not a word given')
    else:
        vowels = 'aeoui'
        pig_latin_word = word
        for letter in word:
            if letter not in vowels:
                pig_latin_word = pig_latin_word[1:] + pig_latin_word[:1]
            else:
                break
        pig_latin_word += 'ay'
        return pig_latin_word


def main():
    word = input('Enter a word to transform it to pig latin: ')
    print(pig_latin_transformation(word))


if __name__ == "__main__":
    main()

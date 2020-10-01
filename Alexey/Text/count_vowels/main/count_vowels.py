def main():
    sentence = input('Input some text: ')
    print(vowel_counter(sentence))


def vowel_counter(sentence):
    count = 0
    for liter in sentence:
        if liter.lower() in "aeiou":
            count += 1
    return count


if __name__ == '__main__':
    main()

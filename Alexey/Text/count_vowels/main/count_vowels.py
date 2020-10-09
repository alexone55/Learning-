def main():
    sentence = input('Input some text: ')
    print(vowel_counter(sentence))


def vowel_counter(sentence):
    if isinstance(sentence, str):
        char_a = sentence.count('a')
        char_e = sentence.count('e')
        char_i = sentence.count('i')
        char_o = sentence.count('o')
        char_u = sentence.count('u')
        count = 0
        for char in sentence:
            if char.lower() in "aeiou":
                count += 1
        answer = str('Char A is: ' + str(char_a) +
                     '| Char E is : ' + str(char_e) +
                     '| Char I is : ' + str(char_i) +
                     '| Char O is : ' + str(char_o) +
                     '| Char U is : ' + str(char_u) +
                     '| Total: ' + str(count))
        return answer
    else:
        return 'There is no vowels here'


if __name__ == '__main__':
    main()

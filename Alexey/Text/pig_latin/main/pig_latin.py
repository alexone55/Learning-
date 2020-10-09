def main():
    sentence = input("Enter a sentence you want to convert to pig latin: ")
    print(translater(sentence))


def translater(sentence):
    sentence = sentence.lower().split()
    for id, i in enumerate(sentence):
        if sentence[id][0] in "aeiou":
            sentence[id] += 'yay'
        else:
            sentence[id] = sentence[id][1:]+sentence[id][0]
            sentence[id] += 'ay'

    sentence = ' '.join(sentence).replace(',', '').replace('.', '')

    return sentence


if __name__ == '__main__':
    main()

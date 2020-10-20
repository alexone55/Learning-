import re


def main():
    sentence = "How many words you can -  29 count?"
    print(words_counter(sentence))


def words_counter(sentence):
    sentence = re.sub(r'[^\w]', ' ', sentence)
    sentence = re.sub(r'[0-9]+', '', sentence)
    sentence = sentence.split(" ")
    counter = []
    for word in sentence:
        if word == '':
            continue
        else:
            counter.append(word)
    return len(counter)


if __name__ == '__main__':
    main()
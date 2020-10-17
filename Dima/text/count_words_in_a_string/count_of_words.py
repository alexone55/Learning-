def count_of_words_text(input_text):
    try:
        index = 0
        counter_of_words = []
        all_words = []
        lines = [line for line in input_text]
        for line in lines:
            words = []
            try:
                for word in line.split():
                    if len(word) > 1:
                        words.append(word)
                        all_words.append(word)
                    len_of_str = [index, len(words)]
                    counter_of_words.append(len_of_str)
                    index += 1
            except AttributeError:
                raise AttributeError('AttributeError, The text contains invalid symbols')
        return counter_of_words, len(all_words)
    except ValueError:
        raise ValueError('ValueError, The text contains invalid symbols')


def count_of_words_str(input_text):
    words = []
    for word in input_text.split():
        words.append(word)
    len_of_words = len(words)
    return len_of_words


def count_of_words_input(input_text):
    if isinstance(input_text, str):
        return count_of_words_str(input_text)
    else:
        try:
            counter_of_words = count_of_words_text(input_text)
            return counter_of_words
        except TypeError:
            raise TypeError('TypeError')


def main():
    try:
        try:
            input_text = open('./text.txt', 'r', encoding='utf8')
            print(count_of_words_input(input_text))
        except FileNotFoundError:
            raise FileNotFoundError('FileNotFoundError')
    except ValueError:
        raise ValueError('ValueError, encoding problems')


if __name__ == "__main__":
    main()

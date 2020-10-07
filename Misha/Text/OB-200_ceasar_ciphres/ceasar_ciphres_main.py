def ceasar_ciphres(text, move_number):
    if (type(text) != str) or (type(move_number) != int):
        raise TypeError('TypeError')
    else:
        letters = 'abcdefghijklmnopqrstuvxyz'
        text = text.lower()
        key_letters = letters[move_number:] + letters[:move_number]
        print(key_letters)
        ciphred_text = ''
        for symbol in text:
            if symbol in letters:
                ciphred_text += key_letters[letters.index(symbol)]
            else:
                ciphred_text += symbol
        return ciphred_text, key_letters


def ceasar_unciphres(key_letters, text):
    if (type(text) != str) or (type(key_letters) != str):
        raise TypeError('TypeError')
    else:
        letters = 'abcdefghijklmnopqrstuvxyz'
        text = text.lower()
        unciphred_text = ''
        for symbol in text:
            if symbol in letters:
                unciphred_text += letters[key_letters.index(symbol)]
            else:
                unciphred_text += symbol
        return unciphred_text


def main():
    english_text = 'Inquisitio Haereticae Pravitatis Sanctum Officium'
    move_number = 3
    print('This program works with Ceasar ciphres only for English alphabet')
    print('Moving value: ', move_number)
    ciphred_text, key_letters = ceasar_ciphres(move_number, english_text)
    print('Ciphred text: ', ciphred_text)
    unciphred_text = ceasar_unciphres(key_letters, ciphred_text)
    print('Unciphred text: ', unciphred_text)


if __name__ == "__main__":
    main()

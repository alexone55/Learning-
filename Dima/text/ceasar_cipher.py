class CaesarCipher:

    def __init__(self, text='abc def', key=3):
        self.text = text.lower()
        self.key = key

    def encrypt(self):
        result = ""
        for char in self.text:
            if char == " ":
                result += " "
                continue
            if ord(char) > 96:
                result += chr((ord(char) + self.key - 97) % 26 + 97)
            else:
                result += chr((ord(char) + self.key - 65) % 26 + 65)
        return result

    def decrypt(self):
        result = ""
        for char in self.text:
            if char == " ":
                result += " "
                continue
            if ord(char) > 96:
                result += chr((ord(char) - self.key - 97) % 26 + 97)
            else:
                result += chr((ord(char) - self.key - 65) % 65 + 65)
        return result


def check_if_alpha_and_spaces_only(text):
    if all(symbol.isalpha() or symbol.isspace() for symbol in text):
        return True
    else:
        raise ValueError('String contains symbols or numbers')


def check_and_return_input_to_encrypt():
    text = input('Enter message to encrypt: ')
    if not isinstance(text, str) and len(text) < 1:
        raise TypeError('Your message isn`t string type: ')
    if True:
        check_if_alpha_and_spaces_only(text)
    try:
        key = int(input('Enter encryption key: '))
    except ValueError:
        raise ValueError('Key isn`t int type: ')
    return text, key


def main():
    input_data = check_and_return_input_to_encrypt()
    print('Encrypting...')
    text_to_encrypt = CaesarCipher(input_data[0], input_data[1])
    encrypted = text_to_encrypt.encrypt()
    print('Encrypted message: ', encrypted)
    text_to_decrypt = CaesarCipher(encrypted, input_data[1])
    print('Decrypting...')
    decrypted = text_to_decrypt.decrypt()
    print('Decrypted message: ', decrypted)


if __name__ == "__main__":
    main()

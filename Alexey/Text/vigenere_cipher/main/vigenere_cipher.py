def generate_key(word, key):
    key = list(key)
    if len(word) == len(key):
        return key
    else:
        for i in range(len(word) -
                       len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def cipher_text_func(word, key):
    cipher_text = []
    for i in range(len(word)):
        x = (ord(word[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return "".join(cipher_text)


def original_text(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return "".join(orig_text)


def main():
    word = str(input("Enter a word: ")).upper()
    keyword = str(input("Enter key: ")).upper()
    key = generate_key(keyword)
    print(key)
    cipher_text = cipher_text_func(word, key)
    print("Ciphertext :", cipher_text)
    print("Original/Decrypted Text :",
          original_text(cipher_text, key))


if __name__ == "__main__":
    main()

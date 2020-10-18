def count_vowels(text):
    text = str(text).lower()
    counted_vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    sum_of_vowels = 0
    for letter in text:
        if letter in counted_vowels:
            counted_vowels[letter] += 1
            sum_of_vowels += 1
    return counted_vowels, sum_of_vowels


def main():
    text = str(input('Enter some text to count vowels in them: '))
    vowels = count_vowels(text)
    print(vowels)


if __name__ == "__main__":
    main()

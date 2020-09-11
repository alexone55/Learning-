def main():
    num = int(input("Enter number: "))
    print(num_to_words(num).lower())


def num_to_words(num):
    under_20 = ['Zero', 'One',
                'Two', 'Three',
                'Four',  'Five',
                'Six', 'Seven',
                'Eight', 'Nine',
                'Ten', 'Eleven',
                'Twelve', 'Thirteen',
                'Fourteen', 'Fifteen',
                'Sixteen', 'Seventeen',
                'Eighteen', 'Nineteen']
    tens = ['Twenty',
            'Thirty',
            'Forty',
            'Fifty',
            'Sixty',
            'Seventy',
            'Eighty',
            'Ninety']
    above_100 = {100: 'Hundred',
                 1000: 'Thousand',
                 1000000: 'Million',
                 1000000000: 'Billion'}

    if num < 20:
        return under_20[num]

    if num < 100:
        return tens[int(num / 10) - 2] \
               + ('' if num % 10 == 0 else
                  ' ' + under_20[num % 10])

    pivot = max([key for key in above_100.keys()
                 if key <= num])

    return num_to_words(int(num / pivot)) + ' ' + above_100[pivot] + (
        '' if num % pivot == 0
        else ' ' + num_to_words(num % pivot))


if __name__ == '__main__':
    main()

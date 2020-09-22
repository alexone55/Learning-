import re


def make_spell(value, digits, decimals, parts, b_parts):
    spell = ['', '', '']
    while len(value) != 9:
        value = '0' + value
    for i in range(len(spell)):
        temp_value = value[(2 - i) * len(spell):(3 - i) * len(spell)]
        if not re.fullmatch(r'[0]{3}', temp_value):
            if re.fullmatch(r'[0]{2}[0-9]', temp_value):
                spell[2 - i] = digits[int(temp_value[2])] + ' '
            elif re.fullmatch(r'[^0]\d\d', temp_value):
                spell[2 - i] = digits[int(temp_value[0])] + ' ' + b_parts[0] + ' '
                if temp_value[1] == '1':
                    spell[2 - i] += decimals[int(temp_value[2])] + ' '
                elif temp_value[1] == '0':
                    if temp_value[2] != '0':
                        spell[2 - i] += digits[int(temp_value[2])] + ' '
                else:
                    spell[2 - i] += parts[int(temp_value[1]) - 2] + ' '
                    if temp_value[2] != '0':
                        spell[2 - i] += digits[int(temp_value[2])] + ' '
            elif re.fullmatch(r'[0][^0]\d', temp_value):
                if temp_value[1] == '1':
                    spell[2 - i] += decimals[int(temp_value[2])] + ' '
                else:
                    spell[2 - i] += parts[int(temp_value[1]) - 2] + ' '
                    if temp_value[2] != '0':
                        spell[2 - i] += digits[int(temp_value[2])] + ' '
    if spell[0] != '':
        spell[0] += b_parts[2] + ' '
    if spell[1] != '':
        spell[1] += b_parts[1] + ' '
    return spell


def find_number_name():
    value = str(input('Enter a number: '))
    digits = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    decimals = ('ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                'nineteen')
    parts = ('twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')
    b_parts = ('hundred', 'thousand', 'million')
    spell = make_spell(value, digits, decimals, parts, b_parts)
    print('Number name: ', end='')
    for i in range(len(spell)):
        print(spell[i], end=' ')


if __name__ == "__main__":
    print('The program shows how to spell out entered number in English\n')
    find_number_name()

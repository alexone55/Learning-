def find_number_name():
    value = str(input('Enter a number: '))
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    decimals = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                'nineteen']
    parts = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    b_parts = ['hundred', 'thousand', 'million']
    spell = ['', '', '']
    while len(value) != 9:
        value = '0' + value
    for i in range(len(spell)):
        temp_value = value[(2 - i) * len(spell):(3 - i) * len(spell)]
        spell[2 - i] = digits[int(temp_value[0])] + ' ' + b_parts[0] + ' ' + spell[2 - i]
        if temp_value[1] == '0':
            spell[2 - i] += digits[int(temp_value[2])] + ' '
        elif temp_value[1] == '1':
            spell[2 - i] += decimals[int(temp_value[2])] + ' '
        else:
            spell[2 - i] += parts[int(temp_value[1]) - 2] + ' ' + digits[int(temp_value[2])] + ' '
    spell[0] += b_parts[2] + ' '
    spell[1] += b_parts[1] + ' '
    temp_spell = ''
    for i in range(len(spell)):
        temp_spell += spell[i]
    temp_spell = temp_spell.split(' ')
    spell = temp_spell.copy()
    for i in range(len(temp_spell)):
        if temp_spell[i] == digits[0]:
            spell.remove(temp_spell[i])
            spell.remove(temp_spell[i + 1])
    print('Number name: ', end='')
    for i in range(len(spell)):
        print(spell[i], end=' ')


if __name__=="__main__":
    print('The program shows how to spell out entered number in English\n')
    find_number_name()
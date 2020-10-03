import re


def pattern_using_for_string(pattern, string_data):
    if type(pattern) != str and type(string_data) != str:
        raise TypeError('TypeError')
    else:
        try:
            all_matches = re.findall(pattern, string_data)
            if re.fullmatch(pattern, string_data):
                fullmatch = 'True'
            else:
                fullmatch = 'False'
            print('All matches:', 'None' if all_matches is None else all_matches)
            print('Fullmatch:', fullmatch)
            return all_matches, fullmatch
        except re.error:
            raise re.error('RegexpError')


def main():
    pattern = str(input('Enter regexp: '))
    string_data = str(input('Enter string to find smth with pattern: '))
    all_matches = re.findall(pattern, string_data)
    print('All matches:', 'None' if all_matches is None else all_matches)
    print('Fullmatch:', 'True' if re.fullmatch(pattern, string_data) else 'False')
    print(pattern)


if __name__ == "__main__":
    main()

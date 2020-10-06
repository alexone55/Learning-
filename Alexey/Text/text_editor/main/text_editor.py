def main():
    command = str(input('Enter command: r/w/a or help '))
    some_text = str(input('Enter some text\n'))
    if command == 'w':
        write_file(12)
    elif command == 'a':
        edit_file(some_text)
    elif command == 'r':
        print(check_file())
    elif command == 'help':
        print('r - read')
        print('w - write')
        print('a - append')
    else:
        print('Unknown function!')


def edit_file(some_text):
    with open('new_text.txt', 'a') as file:
        file.write(some_text)


def write_file(some_text):
    with open('new_text.txt', 'w') as file:
        file.write(some_text)


def check_file():
    with open('new_text.txt', 'r') as file:
        return file.read()


if __name__ == '__main__':
    main()

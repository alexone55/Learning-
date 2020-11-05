def main():
    command = ''
    ask_for_exit = ''
    while ask_for_exit != '\q':
        command = str(input('Enter command: r/w/a or help '))
        if command == 'w':
            some_text = str(input('Enter some text\n'))
            write_file(some_text)
        elif command == 'a':
            some_text = str(input('Enter some text\n'))
            edit_file(some_text)
        elif command == 'r':
            print(check_file())

        elif command == 'help':
            print('r - read')
            print('w - write')
            print('a - append')
        else:
            print('Unknown function!')
        ask_for_exit = input('Enter \q to exit ')


def edit_file(some_text):
    with open('new_text.txt', 'a') as file:
        file.write(str(some_text))


def write_file(some_text):
    with open('new_text.txt', 'w') as file:
        file.write(str(some_text))


def check_file():
    with open('new_text.txt', 'r') as file:
        return file.read()


if __name__ == '__main__':
    main()

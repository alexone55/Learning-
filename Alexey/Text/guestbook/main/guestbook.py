from datetime import datetime
def main():
    choose_mode = str(input('Enter mod: add or show  '))
    if choose_mode == 'add':
        comment = str(input('Write a comment\n'))
        add_comment(comment)
    elif choose_mode == 'show':
        print(show_comment())


def add_comment(comment):
    with open('comment_book.txt', 'a') as file:
        file.write("\n_____________\n")
        file.write("\n")
        file.write("Create in: " + str(datetime.now()))
        file.write("\n")
        file.write(str(comment))
        file.write("\n")
        file.write("\n_____________\n")
    pass


def show_comment():
    with open('comment_book.txt', 'r') as file:
        return file.read()


if __name__ == '__main__':
    main()
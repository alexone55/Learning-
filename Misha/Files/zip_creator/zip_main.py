from zipfile import ZipFile
import os


def input_set_of_files():
    set_of_paths = []
    input_string = ' '
    while input_string != '':
        input_string = str(input('Enter path to file: '))
        set_of_paths.append(input_string)
    return set_of_paths


def check_set_of_paths(set_of_paths):
    modified_set = []
    for index in range(len(set_of_paths)):
        if os.path.exists(set_of_paths[index]):
            modified_set.append(set_of_paths[index])
    if len(modified_set) == 0:
        raise FileNotFoundError('List of paths is empty')
    else:
        return set_of_paths


def create_archive(set_of_paths, archive_name):
    set_of_paths = check_set_of_paths(set_of_paths)
    print(set_of_paths)
    with ZipFile(archive_name, "w") as newzip:
        for path_to_file in set_of_paths:
            newzip.write(path_to_file)
    print('Archive created:', archive_name)


def main():
    set_of_paths = input_set_of_files()
    create_archive(set_of_paths, 'testzip.zip')


if __name__ == "__main__":
    main()

from zipfile import ZipFile
import os
import logging


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
            print(set_of_paths[index])
    if len(modified_set) == 0:
        logging.error('List of paths is empty')
        raise FileNotFoundError('List of paths is empty')
    else:
        return modified_set


def create_archive(set_of_paths, archive_name):
    set_of_paths = check_set_of_paths(set_of_paths)
    print(set_of_paths)
    logging.info(str(set_of_paths))
    with ZipFile(archive_name, "w") as new_zip:
        for path_to_file in set_of_paths:
            new_zip.write(path_to_file)
    logging.info('Archive created:' + str(archive_name))


def main():
    logging.basicConfig(filename='zip.log', level=logging.INFO)
    set_of_paths = input_set_of_files()
    create_archive(set_of_paths, 'testzip.zip')


if __name__ == "__main__":
    main()

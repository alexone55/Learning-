from zipfile import ZipFile
import os


def main():
    archive_maker(all_files_in_folder())


def all_files_in_folder():
    current_dir = os.getcwd()
    files = []
    for filename in os.listdir(current_dir):
        files.append(filename)
    print(files)
    return files


def archive_maker(all_files_in_folder):
    with ZipFile('NewZip.zip', 'w') as zip_obj:
        for file in all_files_in_folder:
            zip_obj.write(file)
        zip_obj.close()


if __name__ == '__main__':
    main()
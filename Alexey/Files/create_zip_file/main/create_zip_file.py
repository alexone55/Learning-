from zipfile import ZipFile
import os


def main():
    file_name = str(input('Enter file name: ') + '.zip')
    archive_maker(all_files_in_folder(), file_name)


def all_files_in_folder():
    current_dir = os.getcwd()
    files = []
    for filename in os.listdir(current_dir):
        files.append(filename)
    return files


def archive_maker(all_files_in_folder, file_name='untitled.zip'):
    with ZipFile(file_name, 'w') as zip_obj:
        if len(all_files_in_folder) == 1:
            zip_obj.write(all_files_in_folder[0])
        elif len(all_files_in_folder) > 1:
            for file in all_files_in_folder:
                zip_obj.write(file)
        zip_obj.close()


if __name__ == '__main__':
    main()
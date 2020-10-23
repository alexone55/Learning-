from zipfile import ZipFile


def main():
    file_path_or_name = str(input("Enter file name or path"))
    archive_maker(file_path_or_name)
    # func which add file to archive
    # func which unpack file from archive


def archive_maker(file_path_or_name):
    with open('NewZip.zip', 'w') as zip_obj:
        zip_obj.write(file_path_or_name)


if __name__ == '__main__':
    main()
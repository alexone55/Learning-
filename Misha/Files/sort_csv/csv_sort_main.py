import csv
import os
import operator
import logging


def input_file_name():
    csv_file_name = str(input('Enter csv file name: '))
    if csv_file_name.split('.')[-1] != 'csv':
        raise TypeError('Invalid file type: got ' + csv_file_name.split('.')[-1] + ' instead of \'csv\'.')
    elif os.path.getsize(csv_file_name) == 0:
        raise OSError('File is empty.')
    else:
        return csv_file_name


def input_sort_type():
    sort_type = str(input('Enter \'1\' for downshift sort or \'0\' for upshift: '))
    if sort_type != '1' and sort_type != '0':
        raise ValueError('Incorrect input')
    else:
        if sort_type == '1':
            return True
        else:
            return False


def input_column_name(column_names):
    print('Column names:')
    for name in column_names:
        print(name)
    column_name = str(input('Choose column name from given list to sort by: '))
    if column_name not in column_names:
        raise ValueError('Column name is incorrect')
    else:
        return column_names.index(column_name)


def sort_csv(csv_file_data, sort_type_bool, column_number):
    sorted_csv_file_data = sorted(csv_file_data, key=operator.itemgetter(column_number), reverse=sort_type_bool)
    logging.info('Sorted data')
    for row in sorted_csv_file_data:
        logging.info(row)
    return sorted_csv_file_data


def write_data_to_csv_file(csv_file_name,column_names, sorted_csv_file_data):
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as csv_file:
        csv_file_data = csv.writer(csv_file, delimiter=';')
        csv_file_data.writerow(column_names)
        for row in sorted_csv_file_data:
            csv_file_data.writerow(row)
        csv_file.close()


def main():
    logging.basicConfig(filename='csv_sort.log', level=logging.INFO)
    csv_file_name = input_file_name()  # TemplateImportEmpl.csv
    sort_type_bool = input_sort_type()
    csv_file = open(csv_file_name, 'r', encoding='utf-8')
    csv_file_data = csv.reader(csv_file, delimiter=';')
    column_names = []
    for row in csv_file_data:
        column_names = row
        break
    column_number = input_column_name(column_names)
    sorted_csv_file_data = sort_csv(csv_file_data, sort_type_bool, column_number)
    csv_file.close()
    write_data_to_csv_file(csv_file_name,column_names, sorted_csv_file_data)


if __name__ == "__main__":
    main()
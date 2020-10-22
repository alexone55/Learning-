import csv
from Alexey.Algorithms.OB_125.sorting.bubble_sort import sort as bubble_sort
from Alexey.Algorithms.OB_125.sorting.merge_sort import sort as merge_sort


def main():
    file_name = str(input('Enter a file name: '))
    answer = str(input('Enter what type of sort you want: m/b '))
    if answer == 'm':
        list_of_values = csv_reader(file_name)
        sorted_values = merge_sort(list_of_values)
        write_csv(sorted_values, file_name)
    elif answer == 'b':
        list_of_values = csv_reader(file_name)
        sorted_values = bubble_sort(list_of_values)
        write_csv(sorted_values, file_name)
    else:
        print("something wrong")


def write_csv(sorted_values, file_name):

    with open(file_name, 'w', encoding='utf-16') as file:
        for row in sorted_values:
            file.write(row[0])
            file.write('\n')


def csv_reader(file_name):
    values = []
    with open(file_name, 'r', encoding='utf-16') as file:
        reader = csv.reader(file)
        for row in reader:
            values.append(row[0])
    return values


if __name__ == '__main__':
    main()
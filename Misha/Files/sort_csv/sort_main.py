import csv
import pandas


def sort_csv_file_by_column_name(dataframe, column_name, path):
    try:
        dataframe = dataframe.sort_values(column_name, kind='mergesort')
        dataframe.to_csv(path, columns=dataframe.columns, sep=';', index=False)
    except KeyError:
        raise KeyError


def read_from_file(path):
    try:
        dataframe = pandas.read_csv(path, sep=';', encoding='utf-8')
        return dataframe
    except FileNotFoundError:
        raise FileNotFoundError('No such file or directory')


def main():
    # TemplateImportEmpl.csv
    path = str(input('Enter name of csv file or path: '))
    dataframe = read_from_file(path)
    column_names = dataframe.columns



if __name__ == "__main__":
    main()

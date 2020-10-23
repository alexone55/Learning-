import csv
import sys

def sort_data(data, column, sort_type):
    sorted_data = None

    if sort_type == "ASC":
        sorted_data = sorted(data, key=lambda row:(row[column]), reverse=False)
    elif sort_type == "DESC":
        sorted_data = sorted(data, key=lambda row:(row[column]), reverse=True)

    return sorted_data

def open_file():
    with open (sys.argv[1], 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        headers = reader.fieldnames
        data = [row for row in reader]

    return headers, data

def write_file(data, headers, fname):
    with open ("{}_sorted.csv".format(fname), 'w', newline='', encoding='utf-8') as csvfile_sorted:
        writer = csv.DictWriter(csvfile_sorted, fieldnames=headers, delimiter=';')
        writer.writeheader()

        for row in data:
            writer.writerow(row)

def main():
    result = open_file()

    headers = result[0]
    data = result[1]
    types_of_sort = ("ASC", "DESC")

    filename = sys.argv[1].rsplit('.', 1)[0] # filename without extenstion
    
    print("File's columns are: {}".format(headers))
    col_to_sort = str(input("Please type column to sort: "))
    sort_type = str(input("Choose type of sort (ASC/DESC): ")).upper()

    if col_to_sort not in headers:
        raise ValueError("incorrect header name")
    elif sort_type not in types_of_sort:
        raise ValueError("incorrect sort type")

    sorted_data = sort_data(data, col_to_sort, sort_type)
    write_file(sorted_data, headers, filename)
    

if __name__ == '__main__':
    main()
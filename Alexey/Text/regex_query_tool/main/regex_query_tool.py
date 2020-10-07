def main():
    pattern = str(input("Enter a pattern: "))
    print(reg_expression(pattern))


def data_loader():
    names = []
    with open('data.txt', 'r', encoding="utf-8") as f:
        reader = f.readlines()
        for row in reader:
            names.append(row)
    return names


def reg_expression(pattern):
    names = data_loader()
    matches = []
    for name in names:
        if name.startswith(pattern):
            matches.append(name.strip("\n"))
        else:
            pass
    return matches


if __name__ == '__main__':
    main()

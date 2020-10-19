from fpdf import FPDF


def read_from_file(path):
    try:
        f = open(str(path), 'r')
        text = ''
        for line in f:
            text += line
        f.close()
        return text
    except FileNotFoundError:
        raise FileNotFoundError('No such file or directory')


def change_format_to_pdf(path):
    dot_index = 0
    for symbol_index in range(len(path)-1, 0, -1):
        if path[symbol_index] == '.':
            dot_index = symbol_index
            break
    if dot_index == 0:
        raise TypeError('Not path given')
    else:
        path = path[0:dot_index] + '.pdf'
        return path


def convert_to_pdf(text, path):
    path = change_format_to_pdf(path)
    pdf = FPDF(orientation='P', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(50, 10, txt=text, ln=1, align="C")
    pdf.output(path)


def main():
    path = str(input('Enter file name or path to file: '))
    # here are available files to test input
    #test_file.html
    #test_file.ibc
    #test_file.txt
    text = read_from_file(path)
    change_format_to_pdf(path)
    convert_to_pdf(text, path)


if __name__ == "__main__":
    main()
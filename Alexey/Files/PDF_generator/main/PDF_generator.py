from fpdf import FPDF


def main():
    file_name = str(input("Enter file name: "))
    pdf_file_writer(txt_file_reader(file_name))


def pdf_file_writer(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 12)
    pdf.multi_cell(180, 10, txt=text)
    pdf.output('output.pdf')


def txt_file_reader(file_name):
    with open(file_name, 'r') as object_from_txt:
        text_from_txt = object_from_txt.read()

    return text_from_txt


if __name__ == '__main__':
    main()

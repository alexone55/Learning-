from fpdf import FPDF


def main():
    file_name = str(input("Enter file name: "))
    pdf_file_writer(txt_file_reader(file_name))


def pdf_file_writer(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(50, 10, txt=text, ln=1, align="C")
    pdf.output('output.pdf')


def txt_file_reader(file_name):
    with open(file_name, 'r', encoding='utf-8') as object_from_txt:
        text_from_txt = object_from_txt.read()

    print(text_from_txt)
    return text_from_txt


if __name__ == '__main__':
    main()

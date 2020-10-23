from fpdf import FPDF
import sys

def open_text_file(fname):
    with open(fname, 'r') as f:
        reader = f.read().splitlines() # read all lines of the txt file w/o newlines
        data = [row for row in reader]

    return data

def create_pdf(data, fname):
    pdf = FPDF() 
    pdf.add_page()
    pdf.set_font("Arial", size = 14)

    for row in data:
        pdf.cell(40, 16, row, ln=2)

    pdf.output("{}.pdf".format(fname), 'F')

def main():
    fname_txt = input("Enter file name to convert: ")
    data = open_text_file(fname_txt)
    fname_pdf = input("Enter PDF filename: ")
    create_pdf(data, fname_pdf)

if __name__ == "__main__":
    main()
from tkinter import *
from tkinter import messagebox


def isbinary(value):
    check_var = True
    check_str = "01"
    if value.isdigit():
        if value[0] != '0':
            for i in range(len(value)):
                if str(value[i]) not in checkstr:
                    check_var = False
                    break
    else:
        check_var = True
    return check_var

"""я не понимаю как тут использовать entry_digit без добавления данной функции внутрь функции bin_to_dec_convert"""
def convert():
    value = entry_digit.get()
    if isbinary(value):
        dec = 0
        for i in range(len(value)):
            dec += int(value[i]) * (2 ** (len(value) - i - 1))
        messagebox.showinfo('result', 'Decimal: ' + str(dec))
    else:
        messagebox.showinfo('Info', 'Input Error!')
    return 0


def bin_to_dec_convert():
    root = Tk()
    root.title("Binary to Decimal Converter")
    root.geometry("270x120+70+70")
    root.resizable(False, False)

    btn_convert = Button(text="Convert", background="#87CEEB", foreground="#000000", font="Arial 10",
                         command=convert, width=10)

    lbl_digit = Label(text='Enter binary:')

    entry_digit = Entry(width=22)

    btn_convert.place(x=165, y=70)
    entry_digit.place(x=120, y=20)
    lbl_digit.place(x=20, y=20)

    root.mainloop()


if __name__ == "__main__":
    bin_to_dec_convert()

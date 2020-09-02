from tkinter import *
from tkinter import messagebox
import re


def help():
    messagebox.showinfo('Help','Entry card number in format \n\"XXXX-XXXX-XXXX-XXXX\"')
    return 0


def check():
    value = entry_cardnum.get()
    regexp = r'\d{4}[-]{1}\d{4}[-]{1}\d{4}[-]{1}\d{4}'
    if re.fullmatch(regexp, value):
        cardnum = []
        for i in range(len(value)):
            if value[i].isdigit():
                cardnum.append(int(value[i]))
        for i in range(len(cardnum)):
            if (i + 1) % 2 == 1:
                cardnum[i] *= 2
                if cardnum[i] > 9:
                    cardnum[i] = (cardnum[i] // 10) + (cardnum[i] % 10)
        if sum(cardnum) % 10 == 0:
            messagebox.showinfo('Result','Validation success!')
        else:
            messagebox.showinfo('Result', 'Validation error!')
    else:
        messagebox.showinfo('Result', 'Input error!')
    return 0


root = Tk()
root.title("Credit card validator")
root.geometry("287x120+70+70")
root.resizable(False, False)

btn_check = Button(text="Check", background="#87CEEB", foreground="#000000", font="Arial 10",
                     command=check, width=10)
btn_help = Button(text="?", background="#87CEEB", foreground="#FFFFFF", font="Arial 7",
                  command=help, width=1)

lbl_cardnum = Label(text='Card number:')

entry_cardnum = Entry(width=22)
entry_cardnum.insert(0,'4561-2612-1234-5467')

btn_check.place(x=175, y=70)
btn_help.place(x=250, y=19)
entry_cardnum.place(x=110, y=20)
lbl_cardnum.place(x=20, y=20)

root.mainloop()

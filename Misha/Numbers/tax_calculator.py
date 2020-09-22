from tkinter import *
from tkinter import messagebox


def calculate():
    cost=float(entry_cost.get())
    tax=float(entry_tax.get())
    messagebox.showinfo('Total Cost', str(cost*(tax+100)/100)+"$")
    return 0


root = Tk()
root.title("Tax Calculator")
root.geometry("280x170+70+70")
root.resizable(False, False)

btn_calculate = Button(text="Calculate", background="#87CEEB", foreground="#000000", font="Arial 10",
                      command=calculate, width=10)

lbl_cost = Label(text='Enter cost, $:')
lbl_tax = Label(text='Enter tax, %:')

entry_cost = Entry(width=22)
entry_tax = Entry(width=22)

btn_calculate.place(x=165,y=120)
entry_cost.place(x=120,y=20)
entry_tax.place(x=120,y=60)
lbl_cost.place(x=20,y=20)
lbl_tax.place(x=20,y=60)

root.mainloop()

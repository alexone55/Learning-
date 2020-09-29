import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfile, askopenfile
import os


class Main(tk.Frame):  # создание главного окна
    def __init__(self, root):
        super().__init__(root)  # super отыскивает базовый класс у класса Main

        self.file_name = None
        # settings for textbox and scrollbar
        self.scrollbar = tk.Scrollbar()
        self.text_box = tk.Text(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(command=self.text_box.yview)
        self.text_box.pack(expand=True, fill=tk.BOTH)
        self.text_box.pack_forget()

        self.main_menu = tk.Menu()

        self.file_menu = tk.Menu(tearoff=0)
        self.file_menu.add_command(label="New", command=self.create_new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_file_as)

        self.view_menu = tk.Menu(tearoff=0)
        self.view_menu.add_command(label="Zoom in")
        self.view_menu.add_command(label="Zoom out")
        self.view_menu.add_command(label="Change font")

        self.info_menu = tk.Menu(tearoff=0)
        self.info_menu.add_command(label="Guide", command=self.show_guide)
        self.info_menu.add_command(label="About program", command=self.show_info_about_program)

        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.main_menu.add_cascade(label="View", menu=self.view_menu)
        self.main_menu.add_cascade(label="Info", menu=self.info_menu)

        root.config(menu=self.main_menu)

    def open_file(self):
        self.text_box.pack(expand=True, fill=tk.BOTH)
        file_to_open = askopenfile(mode="r")
        if file_to_open is None:
            return
        else:
            self.file_name = file_to_open.name
            root.title("Text Editor 1.0 - " + self.file_name)
            data = file_to_open.read()
            self.text_box.delete('1.0', tk.END)
            self.text_box.insert('1.0', data)

    def create_new_file(self):
        self.text_box.pack(expand=True, fill=tk.BOTH)
        self.file_name = 'file.txt'
        file_to_create = open(self.file_name, 'w')
        file_to_create.close()
        root.title("Text Editor 1.0 - " + os.path.abspath(self.file_name))
        self.text_box.delete('1.0', tk.END)

    def save_file(self):
        text_box_data = self.text_box.get('1.0', tk.END)
        file_to_save = open(self.file_name, 'w')
        file_to_save.write(text_box_data)
        file_to_save.close()

    def save_file_as(self):
        file_to_save = asksaveasfile(mode='w')
        text_box_data = self.text_box.get('1.0', tk.END)
        try:
            file_to_save.write(text_box_data.rstrip())
            self.file_name = file_to_save.name
            root.title("Text Editor 1.0 - " + self.file_name)
        except Exception:
            messagebox.showerror("Oops!", "Unable to save file....")

    def show_guide(self):
        guide_text = "Welcome to the Text Editor 1.0!\n\n" \
                     "### Work with files ###\n\n" \
                     "To start using the program firstly open the file or create your own.\n" \
                     "# To create file go File->New.\n" \
                     "# To open existing file go File->Open.\n" \
                     "# To save changes in current file go File->Save.\n" \
                     "# To save changes in other file go File->Save As.\n\n" \
                     "### Visual Features ###\n\n" \
                     "---Not added yet---"
        Infobox(guide_text, 'Guide')

    def show_info_about_program(self):
        info_about_program = '### This is a Text Editor 1.0 ###'
        Infobox(info_about_program, 'Python 3.8')


class Infobox(tk.Toplevel):
    def __init__(self, info, title):
        super().__init__(root)
        self.init_infobox(info, title)

    def init_infobox(self, info, title):
        self.title(title)
        self.geometry('360x240+100+100')
        self.resizable(True, True)
        self.scrollbar_infobox = tk.Scrollbar(self)
        self.info_text_box = tk.Text(self, yscrollcommand=self.scrollbar_infobox.set)
        self.scrollbar_infobox.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar_infobox.config(command=self.info_text_box.yview)
        self.info_text_box.pack(expand=True, fill=tk.BOTH)
        self.info_text_box.insert('1.0', info)


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Text Editor 1.0")
    root.geometry("640x480+70+70")
    root.resizable(True, True)
    root.mainloop()

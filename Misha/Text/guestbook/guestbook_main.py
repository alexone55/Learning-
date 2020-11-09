import tkinter as tk
import time


class Main(tk.Frame):  # создание главного окна
    def __init__(self, root):
        super().__init__(root)  # super отыскивает базовый класс у класса Main

        self.file_name = 'comments.txt'

        # settings for textbox and scrollbar
        self.scrollbar = tk.Scrollbar()
        self.text_box = tk.Text(yscrollcommand=self.scrollbar.set, bd=2)
        self.scrollbar.place(x=381, y=0, height=200)
        self.scrollbar.config(command=self.text_box.yview, bd=5)
        self.text_box.place(x=1, y=1, height=200, width=380)

        # settings for buttons
        self.button_add_comment = tk.Button(text='Add comment', bg="AliceBlue", fg="Black", font="Arial 10", width=11,
                                            command=self.add_comment)
        self.button_add_comment.place(x=282, y=215)
        self.button_show_comment_history = tk.Button(text='Show history', bg="AliceBlue", fg="Black", font="Arial 10",
                                                     width=11,
                                                     command=self.show_comment_history)
        self.button_show_comment_history.place(x=20, y=215)

    def add_comment(self):
        text_box_data = time.asctime() + '\n\n'
        text_box_data += self.text_box.get('1.0', tk.END)
        text_box_data += '\n' + '-' * 20 + '\n\n'
        file_to_save = open(self.file_name, 'a')
        file_to_save.write(text_box_data)
        file_to_save.close()
        self.text_box.delete('1.0', tk.END)

    def show_comment_history(self):
        file_to_open = open(self.file_name, 'r')
        if file_to_open is None:
            return
        else:
            data = file_to_open.read()
            OldCommentsbox(data)


class OldCommentsbox(tk.Toplevel):
    def __init__(self, text):
        super().__init__(root)
        self.init_infobox(text)

    def init_infobox(self, text):
        self.title('Comment history')
        self.geometry('400x500+100+100')
        self.resizable(False, False)
        self.scrollbar_infobox = tk.Scrollbar(self)
        self.info_text_box = tk.Text(self, yscrollcommand=self.scrollbar_infobox.set)
        self.scrollbar_infobox.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar_infobox.config(command=self.info_text_box.yview)
        self.info_text_box.pack(expand=True, fill=tk.BOTH)
        self.info_text_box.insert('1.0', text)


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Guestbook")
    root.geometry("400x260+70+70")
    root.resizable(False, False)
    root.mainloop()

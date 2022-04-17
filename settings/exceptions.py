from tkinter import *

from tkinter import ttk


class AddException:
    def __init__(self):
        pass

    def open_window(self):
        self.app = Toplevel()
        self.app.title("Добавить исключение")
        self.app.minsize(400, 150)
        self.app.grab_set()  # Запрещаем доступ к другим окнам пока открыт диалог

        self.label = Label(self.app, text="Выберите количество изделий в разрезке:")
        self.label.pack(pady=5)

        self.combobox = ttk.Combobox(self.app, state="readonly", value=[2, 3, 4, 5])
        self.combobox.pack()
        self.frame = ttk.Frame(self.app)

        """self.btn_ok = Button(self.app, text="Ok", width=20, command=self.apply_exception)
        self.btn_ok.pack(pady=20)"""

        self.combobox.bind("<<ComboboxSelected>>", self.callback_func)

        self.app.mainloop()

    def callback_func(self, event):
        if self.frame:
            self.frame.destroy()

        self.frame = ttk.Frame(self.app)
        if self.combobox.get() != "":
            for i in range(int(self.combobox.get())):
                label = Label(self.frame, text=str(i))
                label.grid(row=0, column=i)
                cb = ttk.Combobox(self.frame, state="readonly", value=[1, 2, 3])
                cb.grid(row=1, column=i)
        self.frame.pack()

        """label_width = Label(self.app, text="Введите ширину для исключения:")
        label_width.pack(pady=10)

        width_entry = Entry(self.app)
        width_entry.pack()

        btn_save = Button(self.app, text="Добавить исключение")
        btn_save.pack(pady=10)"""


    def apply_exception(self):
        product_count = self.combobox.get()
        if product_count != "":
            print(product_count)


    def add_exception(self):
        pass


add_exception = AddException()


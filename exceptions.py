from tkinter import *
from tkinter import messagebox
from config import config as config
import re

class AddException:
    def __init__(self):
        self.list_exceptions = ['^[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?$',
                                '^[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?$',
                                '^[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?$',
                                '^[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?x[0-9]{1}(?:\.[0-9]{1,2})?$']
        self.new_exception_cut = ""
        self.new_exception_width = 0


    def add_exceptions(self):
        self.app = Tk()
        self.app.attributes("-topmost", True)
        self.app.minsize(350, 50)
        self.label_add_exceptions = Label(self.app, text="Для добавления исключения введите его как в примерах ниже: \n"
                                                    "1.8x1.6x1.6 \n"
                                                    "1.8x0.6x1.1x1.5 \n"
                                                    "1.8x0.8x0.8x0.8x0.8 \n"
                                                    "и т.д ")
        self.label_add_exceptions.pack(pady=5)

        self.label_new_exceptions = Label(self.app, text="Введите новое исключение:")
        self.entry_new_exceptions = Entry(self.app)
        self.btn_ok = Button(self.app, text="Добавить", command=self.apply_new_exception)
        self.label_new_exceptions.pack()
        self.entry_new_exceptions.pack(pady=5)
        self.btn_ok.pack()

        self.app.mainloop()

    def apply_new_exception(self):
        if self.entry_new_exceptions.get() != "":
            if self.entry_new_exceptions.get() in re.findall(self.list_exceptions[0], self.entry_new_exceptions.get()) or \
               self.entry_new_exceptions.get() in re.findall(self.list_exceptions[1], self.entry_new_exceptions.get()) or \
               self.entry_new_exceptions.get() in re.findall(self.list_exceptions[2], self.entry_new_exceptions.get()) or \
               self.entry_new_exceptions.get() in re.findall(self.list_exceptions[3], self.entry_new_exceptions.get()):
                self.new_exception_cut = self.entry_new_exceptions.get()

                self.label_new_exceptions.config(text="Введите ширину для разрезки: \n" + self.entry_new_exceptions.get())
                self.label_add_exceptions.destroy()
                self.btn_ok.destroy()
                self.entry_new_exceptions.destroy()

                self.entry_new_width_for_exception = Entry(self.app)
                self.btn_save_exception = Button(self.app, text="Добавить", command=self.save_new_exception_to_file)

                self.entry_new_width_for_exception.pack(pady=5)
                self.btn_save_exception.pack()
            else:
                messagebox.showerror("Ошибка", "Проверьте правильность ввода")
        else:
            self.app.destroy()
            messagebox.showerror("Ошибка", "Введите значение")

    def save_new_exception_to_file(self):
        if self.entry_new_width_for_exception != "":
            if str(self.entry_new_width_for_exception.get()).isdigit() and int(self.entry_new_width_for_exception.get()) > 0:
                self.new_exception_width = self.entry_new_width_for_exception.get()
                print(self.new_exception_cut)
                print(self.new_exception_width)
                config.set_new_exceptions(self.new_exception_cut, self.new_exception_width)
                self.app.destroy()
                messagebox.showinfo("Исключение", "Новое исключение добавлено")
            else:
                messagebox.showerror("Ошибка", "Проверьте корректность ввода")
        else:
            messagebox.showerror("Ошибка", "Поле не может быть пустым")


add_exception = AddException()



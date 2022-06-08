from tkinter import *
from tkinter import messagebox
from config import config as config

class ChangeCompositionName:
    def __init__(self):
        pass

    def composition_name_window(self):
        self.composition_name_window = Tk()
        self.composition_name_window.minsize(350, 50)
        self.label_prefix = Label(self.composition_name_window, text="Префикс названия компоновки")
        self.entry_prefix = Entry(self.composition_name_window)
        self.label_number = Label(self.composition_name_window, text="Номер компоновки")
        self.entry_number = Entry(self.composition_name_window)
        self.btn_ok = Button(self.composition_name_window, text="Применить", command=self.apply_prefix_and_number)

        self.label_prefix.grid(row=0, column=0)
        self.entry_prefix.grid(row=0, column=1, pady=5)
        self.label_number.grid(row=1, column=0)
        self.entry_number.grid(row=1, column=1)
        self.btn_ok.grid(row=2, column=1, pady=5)

        self.entry_prefix.insert(0, config.get_composition_prefix())
        self.entry_number.insert(0, config.get_composition_number())

        self.btn_ok.mainloop()

    def apply_prefix_and_number(self):
        if self.entry_prefix.get() != "" and str.isalpha(self.entry_prefix.get()):
            if self.entry_number.get() != "" and str(self.entry_number.get()).isdigit() and int(
                    self.entry_number.get()) >= 0:
                config.set_composition_prefix(self.entry_prefix.get())
                config.set_composition_number(self.entry_number.get())
            else:
                messagebox.showerror("Ошибка", "Номер не должен быть пустым и должен быть целым числом")
        else:
            messagebox.showerror("Ошибка", "Префикс должен быть буквенный(текстовый) и не должен быть пустым")

        self.composition_name_window.destroy()


change_composition_name = ChangeCompositionName()




from tkinter import *
from tkinter import messagebox
from config import config as config


class ChangeAdditionalFootage:
    def __int__(self):
        pass

    def set_additional_length(self):
        self.win_additional_length = Tk()
        self.win_additional_length.minsize(300, 100)
        self.label_additional_length = Label(self.win_additional_length, text="Какой % от длины рулона нужно добавить?")
        self.entry_additional_length = Entry(self.win_additional_length)
        self.btn_additional_length = Button(self.win_additional_length, text="Сохранить",
                                            command=self.apply_additional_length)

        self.label_additional_length.pack(pady=10)
        self.entry_additional_length.pack()
        self.btn_additional_length.pack(pady=10)
        self.entry_additional_length.insert(0, config.get_additional_length_percent())
        self.win_additional_length.mainloop()

    def apply_additional_length(self):
        try:
            additional_length = float(str(self.entry_additional_length.get()).replace(",", "."))
        except ValueError:
            messagebox.showerror("Ошибка", "Значение должно быть числом с плаваюшей точкой")
        else:
            if additional_length > 0:
                config.set_additional_length_percent(str(additional_length))
                messagebox.showinfo("Внимание", "Значение добавочного метража установлено на " +
                                    config.get_additional_length_percent() + "% от длины рулона")
            else:
                messagebox.showerror("Ошибка", "Значение должно быть положительным")

        self.win_additional_length.destroy()


change_additional_length = ChangeAdditionalFootage()






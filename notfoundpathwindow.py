from tkinter import *
from tkinter import filedialog as fd


class NotFoundPathWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("Не найден рисунок")
        self.app.minsize(400, 120)

    def show_label_for_track(self, row):
        label = Label(self.app, text="Дорожка: {0}, \n ширина: {1}, \n палитра: {2}, \n Не найдена! \n"
                                     "Для дальнейшей работы выберите её вручную".format(row['img_number'] +
                                                                                        row['img_code'],
                                                                                        row['img_width'],
                                                                                        row['img_palette']))
        return label

    def show_label_for_canvas(self, row):
        label = Label(self.app, text="Покрытие: {0}, \n палитра: {1}, \n Не найдено!"
                                     "Для дальнейшей работы выберите его вручную".format(row['img_number'] +
                                                                                         row['img_code'],
                                                                                         row['img_palette']))
        return label

    def run(self):
        label = Label(self.app, text="Тестовый лейбл")
        label.pack()
        self.app.mainloop()

    def destroy(self):
        self.app.destroy()

    def hide_window(self):
        self.app.withdraw()

    def show_window(self):
        self.app.deiconify()

    def open_image(self, palette_folder):
        path = fd.askopenfilename(initialdir=palette_folder, filetypes=(("PCX Files", "*.pcx"),))
        if path:
            return path
        else:
            self.app.destroy()





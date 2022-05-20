from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from parserxlsx import Parser
from mergeimages import ImageProcessing
from config import config as config
from wwexcel import ExcelProcessing
from settings.exceptions import add_exception
from settings.addnewpalette import add_palette
import os

class MainWindow:
    def __init__(self):
        self.app = Tk()
        self.app.title("Компоновщик изображений")
        self.app.minsize(600, 300)
        self.all_label = []
        self.all_combobox = []

        main_menu = Menu()

        # Меню файл
        file_menu = Menu(tearoff=0)
        file_menu.add_command(label="Открыть", command=self.get_order)
        file_menu.add_separator()
        file_menu.add_command(label="Сохранить заявку", command=self.save_order)
        file_menu.add_separator()
        file_menu.add_command(label="Выйти", state="disabled")
        main_menu.add_cascade(label="Файл", menu=file_menu)

        # Меню Настройки
        setting_menu = Menu(tearoff=0)
        setting_menu.add_command(label="Общие", state="disabled")
        setting_menu.add_separator()
        setting_menu.add_command(label="Задать шаблон именования компоновок", state="disabled")
        setting_menu.add_separator()
        setting_menu.add_command(label="Добавить палитру", command=add_palette.show)
        setting_menu.add_separator()
        setting_menu.add_command(label="Задать '%' дополнительного метража", state="disabled")
        setting_menu.add_separator()
        setting_menu.add_command(label="Добавить исключение", state="disabled")

        main_menu.add_cascade(label="Настройки", menu=setting_menu)

        self.app.config(menu=main_menu)

        # Label's (5шт)
        for i in range(5):
            label = Label(self.app, text=str(i + 1) + " в разрезке")
            label.grid(column=i, row=0, pady=10)
            self.all_label.append(label)

        # Combobox (5шт)
        for i in range(5):
            combobox = ttk.Combobox(self.app, state="readonly", width=30)
            combobox.grid(column=i, row=1)
            self.all_combobox.append(combobox)

        # Button
        button = Button(self.app, text="Добавить", command=self.new_composition)
        button.grid(column=4, row=2, pady=20)

        # Info Preview
        frame = Frame(self.app)
        scroll_v = Scrollbar(frame)
        scroll_h = Scrollbar(frame, orient=HORIZONTAL)
        scroll_v.pack(side=RIGHT, fill="y")
        scroll_h.pack(side=BOTTOM, fill="x")
        self.textbox = Text(frame, yscrollcommand=scroll_v.set, xscrollcommand=scroll_h.set, wrap=NONE)
        self.textbox.pack(fill=BOTH, expand=0)
        scroll_v.config(command=self.textbox.yview)
        scroll_h.config(command=self.textbox.xview)
        frame.grid(column=0, row=3, columnspan=5, rowspan=3, pady=20)

    def get_order(self):
        path_to_order = fd.askopenfilename(initialdir=(os.path.expanduser('~\Desktop\\')), filetypes=(("XLSX Files", "*.xlsx"),))
        if path_to_order != "":
            self.textbox.delete("1.0", "end")
            parser = Parser(path_to_order)
            self.data = parser.check_empty_path()
            self.palette_number = parser.get_palette_number()
            self.refresh_combobox()
            self.xlsx_file = ExcelProcessing(self.palette_number)

    def save_order(self):
        path = fd.asksaveasfilename(initialdir=(os.path.expanduser('~\Desktop\\')), filetypes=(("XLSX Files", "*.xlsx"),))
        self.xlsx_file.save_template(path)

    def refresh_combobox(self):
        combobox_values = [str(i["img_row"]) + ") " +
                           str(i["img_number"]) +
                           str(i["img_code"]) + " " +
                           str(i["img_type"]) + " " +
                           str(i["img_width"]) for i in self.data["result"] if int(i["img_count_roll"]) > 0]

        for i in self.all_combobox:
            i["value"] = combobox_values

    def new_composition(self):
        self.images_for_composition = []

        # Получаем значения из combobox и добавляем в список
        for i in self.all_combobox:
            if i.get() != "":
                row = int(i.get().split(")")[0])
                for j in self.data["result"]:
                    if int(j["img_row"] == row):
                        self.images_for_composition.append(j)
                print(i.get())
                i.set("")

        # Добавляем текст предпросмотра до изменений в массиве
        self.append_preview_text()

        # Получаем минимальное значение длины рулона из списка изображений для компоновки
        # И отнимаем это значение у всех изображений из компоновки
        all_count_roll = [int(i["img_count_roll"]) for i in self.images_for_composition]
        for i in self.images_for_composition:
            i["img_count_roll"] = int(i["img_count_roll"]) - min(all_count_roll)

        # Вносим изменения из списка для компоновки в основной массив данных
        for i in self.images_for_composition:
            for j in self.data["result"]:
                if i["img_row"] == j["img_row"]:
                    j["img_count_roll"] = i["img_count_roll"]

        self.refresh_combobox()

        abc = ImageProcessing(self.images_for_composition)
        abc.merge_images()
        count_pixels = abc.get_count_pixels(self.xlsx_file.count_colors)
        self.xlsx_file.append_colors_value(self.xlsx_file.count_colors, count_pixels)
        abc.save_composition(self.palette_number)

    def append_preview_text(self):
        images_name = "+".join([i["img_number"] + i["img_code"] for i in self.images_for_composition])
        images_width = "+".join([i["img_width"] for i in self.images_for_composition])
        images_length = [(float(i["img_length_roll"]) * float(i["img_count_roll"])) +
                         ((float(i["img_length_roll"]) * float(i["img_count_roll"])) / 100 *
                         float(config.get_additional_length_percent())) for i in self.images_for_composition]

        preview_text = "| " + config.get_composition_prefix() + config.get_composition_number() + \
                       " | " + images_name + " | " + images_width + " | " + str("{0:.2f}".format(min(images_length))) + \
                       "м" + " |" + '\n'
        self.textbox.insert(END, preview_text)
        self.textbox.see("end")

        self.xlsx_file.append_composition_info((config.get_composition_prefix() + config.get_composition_number()),
                                               images_name, images_width, str("{0:.2f}".format(min(images_length))))

    def run(self):
        self.app.mainloop()


if __name__ == "__main__":
    a = MainWindow()
    a.run()



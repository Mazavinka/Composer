from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

class AddPalette:
    def __init__(self):
        pass

    def create_main_window(self):
        self.app = Toplevel()
        self.app.title("Добавить палитру")
        self.app.minsize(400, 300)
        self.app.attributes("-topmost", True)

        self.nb = ttk.Notebook(self.app)
        self.nb.pack(fill='both', expand=True)

        self.five_colors_frame = Frame(self.app)
        self.ten_colors_frame = Frame(self.app)
        self.nb.add(self.five_colors_frame, text="5 цветов")
        self.nb.add(self.ten_colors_frame, text="10 цветов")

        self.all_five_colors_entry = []
        self.all_ten_colors_entry = []

    def five_colors_palette_window(self):
        frame_palette = Frame(self.five_colors_frame)
        label_palette = Label(frame_palette, text="Введите номер палитры:")
        label_palette.pack(side="left")
        self.five_palette_number = Entry(frame_palette)
        self.five_palette_number.pack(side="right", pady=10)
        frame_palette.pack()
        for i in range(2, 7):
            frame = Frame(self.five_colors_frame)
            label = Label(frame, text="Краска[" + str(i) + "]")
            label.pack(side="left", padx=5, pady=5)
            entry = Entry(frame)
            entry.pack(side="right")
            frame.pack()

            self.all_five_colors_entry.append(entry)

        btn = Button(self.five_colors_frame, text="Добавить", command=self.add_five_colors_palette)
        btn.pack()

    def ten_colors_palette_window(self):
        frame_palette = Frame(self.ten_colors_frame)
        label_palette = Label(frame_palette, text="Введите номер палитры:")
        label_palette.pack(side="left")
        self.ten_palette_number = Entry(frame_palette)
        self.ten_palette_number.pack(side="right", pady=10)
        frame_palette.pack()

        for i in range(2, 12):
            frame = Frame(self.ten_colors_frame)
            label = Label(frame, text="Краска[" + str(i) + "]")
            label.pack(side="left", padx=5, pady=5)
            entry = Entry(frame)
            entry.pack(side="right")
            frame.pack()

            self.all_ten_colors_entry.append(entry)

        btn = Button(self.ten_colors_frame, text="Добавить", command=self.add_ten_colors_palette)
        btn.pack()


    def add_five_colors_palette(self):
        if self.five_palette_number != "" and str(self.five_palette_number.get()).isdigit():
            for i in self.all_five_colors_entry:
                print(i.get())
            print(self.five_palette_number.get())
        else:
            mb.showerror("Внимание", "Введите номер палитры (Номер палитры должен быть числом)")

    def add_ten_colors_palette(self):
        if self.ten_palette_number != "" and str(self.ten_palette_number.get()).isdigit():
            for i in self.all_ten_colors_entry:
                print(i.get())
            print(self.ten_palette_number.get())
        else:
            mb.showerror("Внимание", "Введите номер палитры (Номер палитры должен быть числом)")

    def show(self):
        self.create_main_window()
        self.five_colors_palette_window()
        self.ten_colors_palette_window()
        self.app.mainloop()


#Проверить существует ли такой номер палитры уже готовый, если да, то не вносить сразу, а спросить перезаписать ли цвета на новые(тогда проверка на количество у)

add_palette = AddPalette()


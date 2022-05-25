import configparser
from tkinter import messagebox


class ConfigPalette:

    def __init__(self):
        self.palette_config = self.get_palette_config()
        self.five_colors_list = ["first", "second", "third", "fourth", "fifth"]
        self.ten_colors_list = ["first", "second", "third", "fourth", "fifth",
                                "sixth", "seventh", "eighth", "ninth", "tenth"]

    def get_palette_config(self):
        config = configparser.ConfigParser()
        config.read("config/palette_colors.ini", encoding="ANSI")
        return config

    def add_five_palette_colors(self, palette, first_color, second_color, third_color, fourth_color, fifth_color):
        if palette not in self.palette_config and str(palette).isdigit():
            self.palette_config.add_section(palette)

            for i, x in zip([first_color, second_color, third_color, fourth_color, fifth_color], self.five_colors_list):
                if i != "":
                    self.palette_config.set(palette, x, i)
                else:
                    self.palette_config.set(palette, x, "-----")

            with open("config/palette_colors.ini", "w") as configfile:
                self.palette_config.write(configfile)

            messagebox.showinfo(title=None, message="Палитра %s добавлена" % palette)
        else:
            answer_rewrite_colors = messagebox.askyesno(title=None, message="Палитра %s уже существует. Желаете перезаписать цвета для неё?" % palette)
            if answer_rewrite_colors:
                for i, x in zip([first_color, second_color, third_color, fourth_color, fifth_color],
                                self.five_colors_list):
                    if i != "":
                        self.palette_config.set(palette, x, i)
                    else:
                        self.palette_config.set(palette, x, "-----")

                with open("config/palette_colors.ini", "w") as configfile:
                    self.palette_config.write(configfile)

                messagebox.showinfo(title=None, message="Палитра %s добавлена" % palette)

    def add_ten_palette_colors(self, palette, first_color, second_color, third_color, fourth_color, fifth_color,
                               sixth_color, seventh_color, eighth_color, ninth_color, tenth_color):
        if palette not in self.palette_config and str(palette).isdigit():
            self.palette_config.add_section(palette)

            for i, x in zip([first_color, second_color, third_color, fourth_color, fifth_color,
                             sixth_color, seventh_color, eighth_color, ninth_color, tenth_color], self.ten_colors_list):
                if i != "":
                    self.palette_config.set(palette, x, i)
                else:
                    self.palette_config.set(palette, x, "-----")

            with open("config/palette_colors.ini", "w") as configfile:
                self.palette_config.write(configfile)

            messagebox.showinfo(title=None, message="Палитра %s добавлена" % palette)
        else:
            answer_rewrite_colors = messagebox.askyesno(title=None, message="Палитра %s уже существует. Желаете перезаписать цвета для неё?" % palette)
            if answer_rewrite_colors:
                for i, x in zip([first_color, second_color, third_color, fourth_color, fifth_color,
                                 sixth_color, seventh_color, eighth_color, ninth_color, tenth_color],
                                self.ten_colors_list):
                    if i != "":
                        self.palette_config.set(palette, x, i)
                    else:
                        self.palette_config.set(palette, x, "-----")

                with open("config/palette_colors.ini", "w") as configfile:
                    self.palette_config.write(configfile)

                messagebox.showinfo(title=None, message="Палитра %s добавлена" % palette)





palette_config = ConfigPalette()

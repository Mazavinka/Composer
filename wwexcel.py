from config import config as config
from openpyxl import load_workbook
from openpyxl.styles import Font


class ExcelProcessing:
    def __init__(self, palette_number):
        self.palette_number = palette_number
        self.count_colors = 0
        self.template = load_workbook(self.get_template())
        self.sheet = self.template.active
        self.row_in_file = 5

        self.second_color = 0.0
        self.third_color = 0.0
        self.fourth_color = 0.0
        self.fifth_color = 0.0
        self.sixth_color = 0.0
        self.seventh_color = 0.0
        self.eighth_color = 0.0
        self.ninth_color = 0.0
        self.tenth_color = 0.0
        self.eleventh_color = 0.0

        self.sum_second_colors = 0.0
        self.sum_third_colors = 0.0
        self.sum_fourth_colors = 0.0
        self.sum_fifth_colors = 0.0
        self.sum_sixth_colors = 0.0
        self.sum_seventh_colors = 0.0
        self.sum_eighth_colors = 0.0
        self.sum_ninth_colors = 0.0
        self.sum_tenth_colors = 0.0
        self.sum_eleventh_colors = 0.0

        self.all_images_length = []
        self.composition_length = 0

    def get_template(self):
        colors = []
        for i in config.palette_config:
            if self.palette_number == i:
                for j in config.palette_config[i].values():
                    colors.append(j)
                    self.colors_name = colors

        if len(colors) > 5:
            self.count_colors = 10
            return "templates/ten_template.xlsx"
        else:
            self.count_colors = 5
            return "templates/five_template.xlsx"

    def append_colors_name(self):
        self.sheet["E4"].value = self.colors_name[0]
        self.sheet["F4"].value = self.colors_name[1]
        self.sheet["G4"].value = self.colors_name[2]
        self.sheet["H4"].value = self.colors_name[3]
        self.sheet["I4"].value = self.colors_name[4]

        if len(self.colors_name) > 5:
            self.sheet["J4"].value = self.colors_name[5]
            self.sheet["K4"].value = self.colors_name[6]
            self.sheet["L4"].value = self.colors_name[7]
            self.sheet["M4"].value = self.colors_name[8]
            self.sheet["N4"].value = self.colors_name[9]

    def append_palette_number(self):
        self.sheet["B3"] = self.palette_number

    def append_composition_info(self, composition_name, images_name, images_width, images_length):
        self.sheet["A" + str(self.row_in_file)].value = composition_name
        self.sheet["B" + str(self.row_in_file)].value = images_name
        self.sheet["C" + str(self.row_in_file)].value = images_width
        self.sheet["D" + str(self.row_in_file)].value = images_length
        self.all_images_length.append(float(images_length))
        self.composition_length = float(images_length)
        print(self.composition_length)

    def append_colors_value(self, colors_count, pixels):
        all_pixels = pixels["pixels_count"][0]["all_pixels"]
        second_color = "{0:.2f}".format(pixels["pixels_count"][0]["second_color"] / all_pixels * 100)
        third_color = "{0:.2f}".format(pixels["pixels_count"][0]["third_color"] / all_pixels * 100)
        fourth_color = "{0:.2f}".format(pixels["pixels_count"][0]["fourth_color"] / all_pixels * 100)
        fifth_color = "{0:.2f}".format(pixels["pixels_count"][0]["fifth_color"] / all_pixels * 100)
        sixth_color = "{0:.2f}".format(pixels["pixels_count"][0]["sixth_color"] / all_pixels * 100)

        self.sheet["E" + str(self.row_in_file)].value = second_color
        self.sheet["F" + str(self.row_in_file)].value = third_color
        self.sheet["G" + str(self.row_in_file)].value = fourth_color
        self.sheet["H" + str(self.row_in_file)].value = fifth_color
        self.sheet["I" + str(self.row_in_file)].value = sixth_color

        """self.second_color += float(second_color)
        self.third_color += float(third_color)
        self.fourth_color += float(fourth_color)
        self.fifth_color += float(fifth_color)
        self.sixth_color += float(sixth_color)"""

        seventh_color = ""
        eighth_color = ""
        ninth_color = ""
        tenth_color = ""
        eleventh_color = ""

        if colors_count > 5:
            seventh_color = "{0:.2f}".format(pixels["pixels_count"][0]["seventh_color"] / all_pixels * 100)
            eighth_color = "{0:.2f}".format(pixels["pixels_count"][0]["eighth_color"] / all_pixels * 100)
            ninth_color = "{0:.2f}".format(pixels["pixels_count"][0]["ninth_color"] / all_pixels * 100)
            tenth_color = "{0:.2f}".format(pixels["pixels_count"][0]["tenth_color"] / all_pixels * 100)
            eleventh_color = "{0:.2f}".format(pixels["pixels_count"][0]["eleventh_color"] / all_pixels * 100)
            self.sheet["J" + str(self.row_in_file)].value = seventh_color
            self.sheet["K" + str(self.row_in_file)].value = eighth_color
            self.sheet["L" + str(self.row_in_file)].value = ninth_color
            self.sheet["M" + str(self.row_in_file)].value = tenth_color
            self.sheet["N" + str(self.row_in_file)].value = eleventh_color

            """self.seventh_color += float(seventh_color)
            self.eighth_color += float(eighth_color)
            self.ninth_color += float(ninth_color)
            self.tenth_color += float(tenth_color)
            self.eleventh_color += float(eleventh_color)"""

        self.row_in_file += 1

        # Краска №2
        self.second_color = "{0:.2f}".format(self.composition_length * float(second_color) * 0.08)
        self.sum_second_colors += float(self.second_color)
        self.sheet["E" + str(self.row_in_file)].value = self.sum_second_colors

        # Краска №3
        self.third_color = "{0:.2f}".format(self.composition_length * float(third_color) * 0.08)
        self.sum_third_colors += float(self.third_color)
        self.sheet["F" + str(self.row_in_file)].value = self.sum_third_colors

        # Краска №4
        self.fourth_color = "{0:.2f}".format(self.composition_length * float(fourth_color) * 0.08)
        self.sum_fourth_colors += float(self.fourth_color)
        self.sheet["G" + str(self.row_in_file)].value = self.sum_fourth_colors

        # Краска №5
        self.fifth_color = "{0:.2f}".format(self.composition_length * float(fifth_color) * 0.08)
        self.sum_fifth_colors += float(self.fifth_color)
        self.sheet["H" + str(self.row_in_file)].value = self.sum_fifth_colors

        # Краска №6
        self.sixth_color = "{0:.2f}".format(self.composition_length * float(sixth_color) * 0.08)
        self.sum_sixth_colors += float(self.sixth_color)
        self.sheet["I" + str(self.row_in_file)].value = self.sum_sixth_colors

        if colors_count > 5:
            # Краска №7
            self.seventh_color = "{0:.2f}".format(self.composition_length * float(seventh_color) * 0.08)
            self.sum_seventh_colors += float(self.seventh_color)
            self.sheet["J" + str(self.row_in_file)].value = self.sum_seventh_colors

            # Краска №8
            self.eighth_color = "{0:.2f}".format(self.composition_length * float(eighth_color) * 0.08)
            self.sum_eighth_colors += float(self.eighth_color)
            self.sheet["K" + str(self.row_in_file)].value = self.sum_eighth_colors

            # Краска №9
            self.ninth_color = "{0:.2f}".format(self.composition_length * float(ninth_color) * 0.08)
            self.sum_ninth_colors += float(self.ninth_color)
            self.sheet["L" + str(self.row_in_file)].value = self.sum_ninth_colors

            # Краска №10
            self.tenth_color = "{0:.2f}".format(self.composition_length * float(tenth_color) * 0.08)
            self.sum_tenth_colors += float(self.tenth_color)
            self.sheet["M" + str(self.row_in_file)].value = self.sum_tenth_colors

            # Краска №11
            self.eleventh_color = "{0:.2f}".format(self.composition_length * float(eleventh_color) * 0.08)
            self.sum_eleventh_colors += float(self.eleventh_color)
            self.sheet["N" + str(self.row_in_file)].value = self.sum_eleventh_colors


        """self.sheet["E" + str(self.row_in_file)].value = self.second_color
        self.sheet["F" + str(self.row_in_file)].value = self.third_color
        self.sheet["G" + str(self.row_in_file)].value = self.fourth_color
        self.sheet["H" + str(self.row_in_file)].value = self.fifth_color
        self.sheet["I" + str(self.row_in_file)].value = self.sixth_color

        if colors_count > 5:
            self.sheet["J" + str(self.row_in_file)].value = self.seventh_color
            self.sheet["K" + str(self.row_in_file)].value = self.eighth_color
            self.sheet["L" + str(self.row_in_file)].value = self.ninth_color
            self.sheet["M" + str(self.row_in_file)].value = self.tenth_color
            self.sheet["N" + str(self.row_in_file)].value = self.eleventh_color"""

        """# Среднее арифметическое по всем длинам для химиков
        avg = float(sum(self.all_images_length) / len(self.all_images_length))
        self.sheet["D" + str(self.row_in_file)].value = "{0:.2f}".format(avg)"""

        """# Рассчет по формуле для химиков (сколько красок варить)
        self.row_in_file += 1
        how_much_second_color = "{0:.2f}".format(((avg * 4) / 50) * self.second_color)
        how_much_third_color = "{0:.2f}".format(((avg * 4) / 50) * self.third_color)
        how_much_fourth_color = "{0:.2f}".format(((avg * 4) / 50) * self.fourth_color)
        how_much_fifth_color = "{0:.2f}".format(((avg * 4) / 50) * self.fifth_color)
        how_much_sixth_color = "{0:.2f}".format(((avg * 4) / 50) * self.sixth_color)
        self.sheet["E" + str(self.row_in_file)].value = how_much_second_color
        self.sheet["F" + str(self.row_in_file)].value = how_much_third_color
        self.sheet["G" + str(self.row_in_file)].value = how_much_fourth_color
        self.sheet["H" + str(self.row_in_file)].value = how_much_fifth_color
        self.sheet["I" + str(self.row_in_file)].value = how_much_sixth_color

        if colors_count > 5:
            how_much_seventh_color = "{0:.2f}".format(((avg * 4) / 50) * self.seventh_color)
            how_much_eighth_color = "{0:.2f}".format(((avg * 4) / 50) * self.eighth_color)
            how_much_ninth_color = "{0:.2f}".format(((avg * 4) / 50) * self.ninth_color)
            how_much_tenth_color = "{0:.2f}".format(((avg * 4) / 50) * self.tenth_color)
            how_much_eleventh_color = "{0:.2f}".format(((avg * 4) / 50) * self.eleventh_color)
            self.sheet["J" + str(self.row_in_file)].value = how_much_seventh_color
            self.sheet["K" + str(self.row_in_file)].value = how_much_eighth_color
            self.sheet["L" + str(self.row_in_file)].value = how_much_ninth_color
            self.sheet["M" + str(self.row_in_file)].value = how_much_tenth_color
            self.sheet["N" + str(self.row_in_file)].value = how_much_eleventh_color

        self.row_in_file -= 1"""

    def save_template(self, path):
        self.append_palette_number()
        self.append_colors_name()
        self.template.save(path + ".xlsx")


if __name__ == "__main__":
    a = ExcelProcessing("51")







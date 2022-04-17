from PIL import Image
import os
from config import config as config


class ImageProcessing:
    def __init__(self, images_for_composition):
        self.images_for_composition = images_for_composition
        self.width_for_canvas = {"5": 4980, "2.5": 2480, "4": 3968, "3": 2976, "2": 1984, "3.5": 3472,
                                 "1.9": 1884, "1.8": 1786, "1.7": 1686, "1.6": 1588, "1.5": 1488,
                                 "1.4": 1388,
                                 "1.3": 1290, "1.2": 1190, "1.1": 1092, "1": 992, "0.9": 892, "0.8": 794,
                                 "0.7": 694, "0.65": 645, "0.6": 596, "0.5": 496, }
        self.general_width = self.set_general_width()
        self.count_images_in_composition = len(images_for_composition)

    def get_palette(self):
        palette = Image.open(self.images_for_composition[0]["img_full_path"]).getpalette()
        return palette

    def get_max_height(self):
        pass

    def set_general_width(self):
        width_for_composition_len = {1: 4984, 2: 4967, 3: 4970, 4: 4973, 5: 4976, }
        if self.is_exception() is None:
            for key in width_for_composition_len:
                if key == len(self.images_for_composition):
                    return width_for_composition_len.get(key)
        else:
            return self.is_exception()

    def is_canvas(self, canvas):
        x_offset = 0
        for i in self.width_for_canvas:
            if canvas["img_width"] == i:
                width_for_canvas = self.width_for_canvas.get(i)
                image_original = Image.open(canvas["img_full_path"])
                image_width = image_original.size[0]
                image_length = image_original.size[1]
                new_image = Image.new("P", (width_for_canvas, image_length))

                while width_for_canvas > 0:
                    new_image.paste(image_original, (x_offset, 0))
                    x_offset += image_width
                    width_for_canvas -= image_width
                x_offset = 0
                return new_image

    def is_track(self, track):
        original_image = Image.open(track["img_full_path"])
        return original_image

    def is_exception(self):
        cutting = "x".join([i["img_width"] for i in self.images_for_composition])
        for i in config.get_exceptions_width()["EXCEPTIONS"]:
            if cutting == i:
                return int(config.get_exceptions_width()["EXCEPTIONS"][i])



    def merge_images(self):
        images = []
        x_offset = 2  # Отступ чтобы не задеть боковую линию (side_line)
        palette = self.get_palette()
        cut_line = 3  # Линия разрезки

        for i in self.images_for_composition:
            if i["img_type"].lower() == "покрытие":
                images.append(self.is_canvas(i))
            elif i["img_type"].lower() == "дорожка":
                images.append(self.is_track(i))

        list_of_height = [i.size[1] for i in images]
        max_height = max(list_of_height)

        side_line = Image.new("P", (2, max_height), color=3)
        self.result = Image.new("P", (self.general_width, max_height))

        # Вставляем боковые линии для апрета в начало и в конец изображения
        self.result.paste(side_line)
        self.result.paste(side_line, (self.general_width-2, 0))

        # Добавляем к итоговому изображению изображения из списка
        for i in images:
            self.result.paste(i, (x_offset, 0))
            img_width = i.size[0]
            x_offset += img_width + cut_line

        self.result.putpalette(palette)

    def get_count_pixels(self, colors_count):
        second_color_in_palette = 0
        third_color_in_palette = 0
        fourth_color_in_palette = 0
        fifth_color_in_palette = 0
        sixth_color_in_palette = 0
        seventh_color_in_palette = 0
        eighth_color_in_palette = 0
        ninth_color_in_palette = 0
        tenth_color_in_palette = 0
        eleventh_color_in_palette = 0

        for pixel in self.result.getdata():
            if pixel == 2:
                second_color_in_palette += 1
            elif pixel == 3:
                third_color_in_palette += 1
            elif pixel == 4:
                fourth_color_in_palette += 1
            elif pixel == 5:
                fifth_color_in_palette += 1
            elif pixel == 6:
                sixth_color_in_palette += 1

            if colors_count > 5:
                if pixel == 7:
                    seventh_color_in_palette += 1
                if pixel == 8:
                    eighth_color_in_palette += 1
                if pixel == 9:
                    ninth_color_in_palette += 1
                if pixel == 10:
                    tenth_color_in_palette += 1
                if pixel == 11:
                    eleventh_color_in_palette += 1

        result = {"pixels_count": [{
            "second_color": second_color_in_palette,
            "third_color": third_color_in_palette,
            "fourth_color": fourth_color_in_palette,
            "fifth_color": fifth_color_in_palette,
            "sixth_color": sixth_color_in_palette,
            "seventh_color": seventh_color_in_palette,
            "eighth_color": eighth_color_in_palette,
            "ninth_color": ninth_color_in_palette,
            "tenth_color": tenth_color_in_palette,
            "eleventh_color": eleventh_color_in_palette,
            "all_pixels": self.result.size[0] * self.result.size[1]
        }]}

        return result

    def save_composition(self, palette_number):
        os.makedirs(os.path.expanduser('~\Desktop\\') + palette_number, exist_ok=True)
        self.result.save(os.path.expanduser('~\Desktop\\') + palette_number
                         + "\\"
                         + config.get_composition_prefix()
                         + config.get_composition_number()
                         + ".pcx")
        config.autoincrement_composition_number()



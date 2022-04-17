import configparser


class ConfigComposer:
    def __init__(self):
        self.config = self.get_config()
        self.palette_config = self.get_palette_config()

    def get_config(self):
        config = configparser.ConfigParser()
        config.read("config/settings.ini", encoding="ANSI")
        return config

    def get_palette_config(self):
        palette_config = configparser.ConfigParser()
        palette_config.read("config/palette_colors.ini", encoding="ANSI")
        return palette_config

    def get_exceptions_width(self):
        exceptions = configparser.ConfigParser()
        exceptions.read("config/exceptions.ini", encoding="ANSI")
        return exceptions

    def get_composition_number(self):
        number = self.config["SETTINGS"]["number_of_compose"]
        return number

    def set_composition_number(self, value):
        self.config.set("SETTINGS", "number_of_compose", str(value))
        with open("config/settings.ini", "w") as configfile:
            self.config.write(configfile)

    def get_composition_prefix(self):
        prefix = self.config["SETTINGS"]["prefix_compose_name"]
        return prefix

    def set_composition_prefix(self, value):
        self.config.set("SETTINGS", "prefix_compose_name", value)
        with open("config/settings.ini", "w") as configfile:
            self.config.write(configfile)

    def get_server_folder(self):
        folder = self.config["SETTINGS"]["server_dir"]
        return folder

    def set_server_folder(self, value):
        self.config.set("SETTINGS", "server_dir", value)
        with open("config/settings.ini", "w") as configfile:
            self.config.write(configfile)

    def get_additional_length_percent(self):
        percent = self.config["SETTINGS"]["additional_length_percent"]
        return percent

    def set_additional_length_percent(self, value):
        self.config.set("SETTINGS", "additional_length_percent", value)
        with open("config/settings.ini", "w") as configfile:
            self.config.write(configfile)

    def autoincrement_composition_number(self):
        number = int(self.get_composition_number()) + 1
        self.config.set("SETTINGS", "number_of_compose", str(number))
        with open("config/settings.ini", "w") as configfile:
            self.config.write(configfile)


config = ConfigComposer()

if __name__ == "__main__":
    for i in config.palette_config["51"]:
        print(i)

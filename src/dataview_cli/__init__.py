from . import stylesheets as stylesheets


class Terminal:
    def __init__(self, colormode: int = 0):
        """
        :param colormode: 0 = dark, 1 = light, 2 = colorful
        """
        self.__colormode = colormode

        if colormode == 0:
            print(stylesheets.Mode0.RESET)
        if colormode == 1:
            print(stylesheets.Mode1.RESET)

    def set_colormode(self, colormode: int):
        """

        :param colormode:
        :return:
        """
        if colormode == 0:
            print(stylesheets.Mode0.RESET)
        if colormode == 1:
            print(stylesheets.Mode1.RESET)
        self.__colormode = colormode


class JsonTree:
    def __init__(self, json_data: dict, title: str = "Unnamed json tree"):
        self.__title = title
        self.json_data = json_data

    def __iterate_json(self, json_dict: dict, colors: list, result="", iteration=0, spacing="    "):
        color = colors[iteration % (len(colors))]

        for k, v in json_dict.items():
            if isinstance(v, dict):
                result += f"{color}{spacing * iteration}┗ ['{k}']{stylesheets.General.RESET}\n"
                result = self.__iterate_json(v, colors, result, iteration=iteration + 1)
                continue
            elif isinstance(v, list):
                result += f"{color}{spacing * iteration}┗ ['{k}']{stylesheets.General.RESET}\n"
                for ii, li in enumerate(v):
                    if isinstance(li, dict):
                        result += f"{colors[((iteration + 1) % len(colors))]}{spacing * (iteration + 1)}┗  [{ii}]{stylesheets.General.RESET}\n"
                        result = self.__iterate_json(li, colors, result, iteration=iteration + 2)
                        continue
                    else:
                        result += f"{colors[((iteration + 1) % len(colors))]}{spacing * (iteration + 1)}┗  [{ii}]{stylesheets.General.RESET}{li}\n"
                continue
            else:
                result += f"{color}{spacing * iteration}┗ ['{k}']{stylesheets.General.RESET}{v}\n"
        return result

    def __str__(self):
        return self.__iterate_json(self.json_data, result=f"{stylesheets.General.UNDERLINE}{stylesheets.General.BOLD}{self.__title}{stylesheets.General.RESET}\n\n",
                                   colors=[stylesheets.General.Foreground.BLUE,
                                           stylesheets.General.Foreground.GREEN,
                                           stylesheets.General.Foreground.CYAN,
                                           stylesheets.General.Foreground.MAGENTA])


class PointMatrix:
    def __init__(self, x_name: str, y_name: str, x_axis: tuple = (0, 20), x_step: int = 2, y_axis: tuple = (0, 10),
                 y_step: int = 2):
        self.__datasets = []
        self.__x_axis = x_axis
        self.__y_axis = y_axis
        self.__x_name = x_name
        self.__y_name = y_name

    def add_dataset(self, name: str, points: list):
        for point in points:
            if not isinstance(point[0], int) or not isinstance(point[1], int):
                return False, f"{point} is not typeof integer"
            if not self.__x_axis[0] < point[0] < self.__x_axis[1] or not self.__y_axis[0] < point[1] < self.__y_axis[1]:
                return False, f"{point} is not in range"

        self.__datasets.append({
            "name": name,
            "points": points})

    def __str__(self):
        __grid = []
        __datasets = self.__datasets

        fg_colors = stylesheets.General.Foreground
        colors = [fg_colors.BLUE, fg_colors.GREEN, fg_colors.RED, fg_colors.MAGENTA, fg_colors.YELLOW, fg_colors.CYAN]
        for i, dataset in enumerate(__datasets):
            __datasets[i]["color"] = colors[i]

        for i in range(self.__y_axis[0], self.__y_axis[1]):
            __row = []
            for ii in range(self.__x_axis[0], self.__x_axis[1]):
                __row.append(str(" "))
            __grid.append(__row)

        __legend = f"{stylesheets.General.BOLD}{stylesheets.General.UNDERLINE}Legend{stylesheets.General.RESET}\n"
        for dataset in __datasets:
            __legend = f"{__legend}{dataset['color']}✦{stylesheets.General.RESET} = {dataset['name']}\n"
            for point in dataset["points"]:
                __grid[point[1]][point[0]] = f'{dataset["color"]}✦{stylesheets.General.RESET}'

        __diagram = f""
        __result = f"{self.__y_name}\n"
        for row in __grid:
            __result = f"{__result}   ┫"
            for cell in row:
                __result = f"{__result} {cell}  "
            __result = __result + "\n"
        __result = __result + "   ┗━"

        for i in range(self.__x_axis[0], self.__x_axis[1]):
            __result = __result + "┳━━"

        __result = f"{__result}\n\n\n{__legend}"

        return __result

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
# print(f"""
#     {TerminalColor.BOLD}{TerminalColor.UNDERLINE}Unbenanntes Diagramm{TerminalColor.END}
# zeit in s
#   ┃
# 3 ┫    {TerminalColor.RED}✦{TerminalColor.END}   {TerminalColor.BLUE}✦{TerminalColor.END}
#   ┃
# 2 ┫         {TerminalColor.RED}✦{TerminalColor.END}
#   ┃         {TerminalColor.BLUE}✦{TerminalColor.END}
# 1 ┫   {TerminalColor.BLUE}✦{TerminalColor.END}              {TerminalColor.RED}✦{TerminalColor.END}
#   ┗━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳  strecke in m
#     1  2  3  4  5  6  7  8
#
# ┏━━━━━━━━┓
# ┃{TerminalColor.BOLD}Legende{TerminalColor.END}┃
# ┃{TerminalColor.RED}✦{TerminalColor.END} = Versuch 1┃
# ┃{TerminalColor.BLUE}✦{TerminalColor.END} = Versuch 2┃
# ┗━━━━━━━━┛""")
#
# print(f"""
#     {TerminalColor.BOLD}{TerminalColor.UNDERLINE}Unbenanntes Diagramm{TerminalColor.END}
# zeit in s
#   ^
# 3 ┫           {TerminalColor.GREEN}█{TerminalColor.END}
#   ┃     {TerminalColor.BLUE}█{TerminalColor.END}     {TerminalColor.GREEN}█{TerminalColor.END}
# 2 ┫  {TerminalColor.RED}█{TerminalColor.END}  {TerminalColor.BLUE}█{TerminalColor.END}     {TerminalColor.GREEN}█{TerminalColor.END}
#   ┃  {TerminalColor.RED}█{TerminalColor.END}  {TerminalColor.BLUE}█{TerminalColor.END}     {TerminalColor.GREEN}█{TerminalColor.END}
# 1 ┫  {TerminalColor.RED}█{TerminalColor.END}  {TerminalColor.BLUE}█{TerminalColor.END}  {TerminalColor.CYAN}█{TerminalColor.END}  {TerminalColor.GREEN}█{TerminalColor.END}
#   ┗━━┳━━┳━━┳━━┳━━
#      {TerminalColor.RED}A{TerminalColor.END}  {TerminalColor.BLUE}B{TerminalColor.END}  {TerminalColor.CYAN}C{TerminalColor.END}  {TerminalColor.GREEN}D{TerminalColor.END}
#
# """)
#
#
# print(f"""
#     {TerminalColor.BOLD}{TerminalColor.UNDERLINE}Unbenannter Tree{TerminalColor.END}
#
# {TerminalColor.BLUE}['data']{TerminalColor.END}
#     {TerminalColor.GREEN}┗ [1]{TerminalColor.END}201
#     {TerminalColor.GREEN}┗ [2]{TerminalColor.END}konnte nicht zugestellt werden
#     {TerminalColor.GREEN}┗ [3]{TerminalColor.END}
#        {TerminalColor.CYAN}┗ ['string']{TerminalColor.END}alles ist super
#        {TerminalColor.CYAN}┗ ['header']{TerminalColor.END}nicht bekannt
# """)
#

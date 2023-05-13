class General:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    FRAMED = "\033[51m"
    ENCIRCLED = "\033[52m"
    OVERLINED = "\033[53m"

    class Foreground:
        BLACK = "\033[90m"
        RED = "\033[91m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        BLUE = "\033[94m"
        MAGENTA = "\033[95m"
        CYAN = "\033[96m"
        WHITE = "\033[97m"

    class Background:
        BLACK = "\033[100m"
        RED = "\033[101m"
        GREEN = "\033[102m"
        YELLOW = "\033[103m"
        BLUE = "\033[104m"
        MAGENTA = "\033[105m"
        CYAN = "\033[106m"
        WHITE = "\033[107m"


class Mode0:
    """Dark mode"""
    RESET = "\033[0m\033[40m\033[97m"

    class Foreground:
        BLACK = "\033[90m"
        RED = "\033[91m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        BLUE = "\033[94m"
        MAGENTA = "\033[95m"
        CYAN = "\033[96m"
        WHITE = "\033[97m"

    class Background:
        BLACK = "\033[40m"
        RED = "\033[41m"
        GREEN = "\033[42m"
        YELLOW = "\033[43m"
        BLUE = "\033[44m"
        MAGENTA = "\033[45m"
        CYAN = "\033[46m"
        WHITE = "\033[47m"


class Mode1:
    """Light mode"""
    RESET = "\033[0m\033[107m\033[30m"

    class Foreground:
        BLACK = "\033[30m"
        RED = "\033[31m"
        GREEN = "\033[32m"
        YELLOW = "\033[33m"
        BLUE = "\033[34m"
        MAGENTA = "\033[35m"
        CYAN = "\033[36m"
        WHITE = "\033[37m"

    class Background:
        BLACK = "\033[100m"
        RED = "\033[101m"
        GREEN = "\033[102m"
        YELLOW = "\033[103m"
        BLUE = "\033[104m"
        MAGENTA = "\033[105m"
        CYAN = "\033[106m"
        WHITE = "\033[107m"

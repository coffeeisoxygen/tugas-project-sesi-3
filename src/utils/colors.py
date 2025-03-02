class Colors:
    # Foreground colors (text)
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright foreground colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

    # Text styles
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    ITALIC = "\033[3m"

    # Reset
    RESET = "\033[0m"

    @staticmethod
    def colorize(
        text: str,
        color: str = "",
        bg_color: str = "",
        bold: bool = False,
        underline: bool = False,
        italic: bool = False,
    ) -> str:
        """Apply colors and styles to text"""
        result = ""
        if color:
            result += color
        if bg_color:
            result += bg_color
        if bold:
            result += Colors.BOLD
        if underline:
            result += Colors.UNDERLINE
        if italic:
            result += Colors.ITALIC

        result += text + Colors.RESET
        return result

    @staticmethod
    def title(text: str) -> str:
        """Format text as a title"""
        return Colors.colorize(text, Colors.BRIGHT_CYAN, bold=True)

    @staticmethod
    def subtitle(text: str) -> str:
        """Format text as a subtitle"""
        return Colors.colorize(text, Colors.BRIGHT_GREEN, bold=True)

    @staticmethod
    def highlight(text: str) -> str:
        """Highlight important text"""
        return Colors.colorize(text, Colors.BRIGHT_YELLOW)

    @staticmethod
    def code(text: str) -> str:
        """Format text as code"""
        return Colors.colorize(text, Colors.BRIGHT_MAGENTA, italic=True)

    @staticmethod
    def error(text: str) -> str:
        """Format error messages"""
        return Colors.colorize(text, Colors.BRIGHT_RED, bold=True)

    @staticmethod
    def success(text: str) -> str:
        """Format success messages"""
        return Colors.colorize(text, Colors.BRIGHT_GREEN, bold=True)

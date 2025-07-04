class ColoredText:
    END       = '\33[0m'
    
    BLACK     = '\33[30m'
    RED       = '\33[31m'
    GREEN     = '\33[32m'
    YELLOW    = '\33[33m'
    BLUE      = '\33[34m'
    VIOLET    = '\33[35m'
    BEIGE     = '\33[36m'
    WHITE     = '\33[37m'
    GREY      = '\33[90m'

class ColoredBackground:
    END       = '\033[0m'

    BLACK     = '\33[40m'
    RED       = '\33[41m'
    GREEN     = '\33[42m'
    YELLOW    = '\33[43m'
    BLUE      = '\33[44m'
    VIOLET    = '\33[45m'
    BEIGE     = '\33[46m'
    WHITE     = '\33[47m'
    GREY      = '\33[100m'

class FormatedText:
    END       = '\033[0m'

    BOLD      = '\33[1m'
    ITALIC    = '\33[3m'
    URL       = '\33[4m'
    BLINK     = '\33[5m'
    BLINK2    = '\33[6m'
    SELECTED  = '\33[7m'

class TextAlign:
    RIGHT     = 'right'
    LEFT      = 'left'
    CENTER    = 'center'

    def set_text_align(text: str, space: int, align: str, fill_char: str = ' ') -> str:
        if align == TextAlign.RIGHT:
            return text.rjust(space, fill_char)
        elif align == TextAlign.LEFT:
            return text.ljust(space, fill_char)
        elif align == TextAlign.CENTER:
            return text.center(space, fill_char)
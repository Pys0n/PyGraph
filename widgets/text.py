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
        '''
        Sets the text align of an text
        '''
        if not isinstance(text, str):
            raise TypeError('Excpected str, got '+type(text).__name__)
        if not isinstance(space, int):
            raise TypeError('Excpected int, got '+type(space).__name__)
        if not isinstance(align, str):
            raise TypeError('Excpected str, got '+type(align).__name__)
        if not isinstance(fill_char, str):
            raise TypeError('Excpected str, got '+type(fill_char).__name__)
        if not isinstance(fill_char, str):
            raise ValueError('Excpected str with a length of 1, got a length of '+len(fill_char))

        if align == TextAlign.RIGHT:
            return text.rjust(space, fill_char)
        elif align == TextAlign.LEFT:
            return text.ljust(space, fill_char)
        elif align == TextAlign.CENTER:
            return text.center(space, fill_char)
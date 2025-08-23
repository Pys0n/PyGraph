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
        

def make_text_horizontal(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError('Excpected text to be a str, got '+type(text).__name__)
    
    return '\n'.join(list(text))


def make_text_backwards(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError('Excpected text to be a str, got '+type(text).__name__)

    text_list = list(text)
    text_list.reverse()
    return ''.join(text_list)


class Text:
    def __init__(self, text: str, *, width: int = -1, height: int = 1, optimal_height: bool = True) -> None:
        '''
        Formates text for the terminal
        '''
        if not isinstance(text, str):
            raise TypeError('Excpected text to be a str, got '+type(text).__name__)
        if not isinstance(width, int):
            raise TypeError('Excpected width to be a int, got '+type(width).__name__)
        if not isinstance(height, int):
            raise TypeError('Excpected height to be a int, got '+type(height).__name__)
        if not isinstance(optimal_height, bool):
            raise TypeError('Excpected optimal_height to be a bool, got '+type(optimal_height).__name__)
        if width <= 0 and width != -1:
            raise ValueError('Excpected width to be 1 or higher, got'+str(width))
        if height <= 0 and height != -1:
            raise ValueError('Excpected height to be 1 or higher, got'+str(height))


        self.text: str = text
        self.width: int = width if width != -1 else len(text)
        self.height: int = height
        self.optimal_height: int = optimal_height


    def copy(self) -> any:
        '''
        Returns a copy of this object
        '''
        text = Text(self.text, width=self.width, height=self.height, optimal_height=self.optimal_height)
        return text
    

    def get_width(self) -> int:
        '''
        Returns the width of the text
        '''
        return self.width


    def get_height(self) -> int:
        '''
        Returns the height of the text
        '''
        return self.height


    def get_text(self) -> str:
        '''
        Returns the text of the object
        '''
        return self.text


    def set_width(self, width: int) -> None:
        '''
        Sets the width of the text
        '''
        if not isinstance(width, int):
            raise TypeError('Excpected width to be a int, got '+type(width).__name__)
        if width <= 0:
            raise ValueError('Excpected width to be 1 or higher, got'+str(width))

        self.width = width


    def set_height(self, height: int) -> None:
        '''
        Sets the height of the text, sets optimal height to False
        '''
        if not isinstance(height, int):
            raise TypeError('Excpected height to be a int, got '+type(height).__name__)
        if height <= 0:
            raise ValueError('Excpected height to be 1 or higher, got'+str(height))
        
        self.height = height
        self.optimal_height = False


    def set_optimal_height(self, optimal_height: bool = True) -> None:
        '''
        Sets the height of the text to the optimal height
        '''
        if not isinstance(optimal_height, bool):
            raise TypeError('Excpected optimal_height to be a bool, got '+type(optimal_height).__name__)
        
        self.optimal_height = optimal_height


    def set_text(self, text: str) -> None:
        '''
        Sets the text of the object
        '''
        if not isinstance(text, str):
            raise TypeError('Excpected text to be a str, got '+type(text).__name__)
        
        self.text = text

    
    def get_formated_text(self) -> str:
        '''
        Returns the formated text
        '''
        return str(self)


    def get_str(self) -> str:
        '''
        Returns the formated text
        '''
        return str(self)


    def print(self) -> None:
        '''
        Prints the formated text into the terminal
        '''
        print(self.get_str())


    def __str__(self) -> None:
        text = self.text.strip()
        text = text.replace('\n', '')
        text = text.split(' ')

        text_parts = ['']

        i = 0
        while True:
            text_parts.append('')
            while text != []:
                if len(text_parts[i]) + len(' '+text[0]) <= self.width and len(text_parts[i]) != 0:
                    text_parts[i] += ' '+text[0]
                    text.pop(0)
                    continue
                elif len(text_parts[i]) + len(text[0]) <= self.width and len(text_parts[i]) == 0:
                    text_parts[i] += text[0]
                    text.pop(0)
                    continue
                elif len(text_parts[i]) == 0 and len(text[0]) > self.width:
                    text_parts[i] += text[0][:self.width]
                    text[0] = text[0][self.width:]
                break
            if text_parts[-2] == '':
                break
            i += 1

        while text_parts[-1].strip() == '':
            text_parts.pop(-1)

        if self.height < len(text_parts) and not self.optimal_height:
            while self.height <= len(text_parts):
                text_parts.pop(-1)
            text_parts.append('...')
        else:
            while self.height > len(text_parts) and not self.optimal_height:
                text_parts.append('')

        return '\n'.join(text_parts)
    

    def __copy__(self) -> any:
        return self.copy()
    

    def __deepcopy__(self) -> any:
        return self.copy()
from widgets.text import TextAlign


class RectangleBorder:
    ASCII               = ("|", "-", "+", "+", "+", "+")
    BASIC               = ("|", "—", "+", "+", "+", "+")
    LIGHT               = ("│", "─", "┌", "┐", "└", "┘")
    HEAVY               = ("┃", "━", "┏", "┓", "┗", "┛")
    DOUBLE              = ("║", "═", "╔", "╗", "╚", "╝")
    LIGHT_ARC           = ("│", "─", "╭", "╮", "╰", "╯")
    LIGHT_DASHED        = ("┊", "╌", "┌", "┐", "└", "┘")
    HEAVY_DASHED        = ("┋", "╍", "┏", "┓", "┗", "┛")
    NO_BORDER           = (" ", " ", " ", " ", " ", " ")
    MY_STYLES           = {}


    def create_style_from_tuple(self, name: str, style: tuple) -> None:
        '''
        Creates a border style from a tuple
        '''
        if not isinstance(style, tuple) and not isinstance(style, list):
            raise TypeError('Expected style to be a tuple, got '+type(style).__name__)
        if len(style) != 6:
            raise ValueError('Excpected style to be a tuple with length 6')
        for item in style:
            if not isinstance(item, str):
                raise TypeError('Expected style to be a tuple of strings, got tuple of '+type(item).__name__)
            if len(item) != 1:
                raise ValueError('Excpected style to be a tuple of single characters or symbols')
        
        self.MY_STYLES[name] = style


    def create_style(self, name: str, horizontal_line: str, vertical_line: str, upper_left_corner: str,
                     upper_right_corner: str, lower_left_corner: str, lower_right_corner: str) -> None:
        
        self.MY_STYLES[name] = (horizontal_line, vertical_line, upper_left_corner,
                                upper_right_corner, lower_left_corner, lower_right_corner)
        
        for style in self.MY_STYLES[name]:
            if not isinstance(style, str):
                return TypeError('Excpected argument at position '+str(self.MY_STYLES[name].index(style)+2)+' to be a string, got '+type(style).__name__)
            if len(style) != 1:
                raise ValueError('Excpected argument at position '+str(self.MY_STYLES[name].index(style)+2)+' to be a single character or symbol')




class Rectangle:
    
    def __init__(self, width: int, height: int, *, border_chars: tuple[str] = RectangleBorder.LIGHT, fill_char: str = ' ', text: str = '', align: str = TextAlign.LEFT) -> None:
        '''
        Creates a rectangle in the terminal
        '''
        if not isinstance(width, int):
            raise TypeError('Excpected width to be an int, got '+type(width).__name__)
        if width <= 1:
            raise ValueError('Excpected width to be 2 or higher, got '+str(width))
        if not isinstance(height, int):
            raise TypeError('Excpected height to be an int, got '+type(height).__name__)
        if height <= 1:
            raise ValueError('Excpected height to be 2 or higher, got '+str(height))
        if not isinstance(border_chars, tuple) and not isinstance(border_chars, list):
            raise TypeError('Excpected border_chars to be a tuple, got '+type(border_chars).__name__)
        if len(border_chars) != 6:
            raise TypeError('Excpected border_chars to have a length of 6, got '+str(len(border_chars)))
        for item in border_chars:
            if not isinstance(item, str):
                raise TypeError('Excpected index '+str(border_chars.index(item))+' border_chars to be a str, got '+type(border_chars).__name__)
            if len(item) != 1:
                raise TypeError('Excpected index '+str(border_chars.index(item))+' border_chars to have a length of 1, got '+str(len(item)))
        if not isinstance(fill_char, str):
            raise TypeError('Excpected fill_char to be a str, got '+type(fill_char).__name__)
        if len(fill_char) != 1:
            raise ValueError('Excpected fill_char to have a length of 1, got '+str(len(fill_char)))
        if not isinstance(text, str):
            raise TypeError('Excpected text to be an str, got '+type(text).__name__)
        if not isinstance(align, str):
            raise TypeError('Excpected align to be a str, got '+type(align).__name__)
        
        self.width: int = width
        self.height: int = height
        self.border_chars: tuple[str] = tuple(border_chars)
        self.fill_char: str = fill_char
        self.text: str = text
        self.align: str = align


    def copy(self) -> any:
        '''
        Returns a copy of this rectangle
        '''
        rect = Rectangle(self.width, self.height, border_chars=self.border_chars, fill_char=self.fill_char, text=self.text, align=self.align)
        return rect


    def set_width(self, width: int) -> None:
        '''
        Sets the width of the rectangle to the value of width
        '''
        if not isinstance(width, int):
            raise TypeError('Excpected width to be an int, got '+type(width).__name__)
        if width <= 1:
            raise TypeError('Excpected width to be 2 or higher, got '+str(width))

        self.width = width


    def set_height(self, height: int) -> None:
        '''
        Sets the height of the rectangle to the value of height
        '''
        if not isinstance(height, int):
            raise TypeError('Excpected height to be an int, got '+type(height).__name__)
        if height <= 1:
            raise TypeError('Excpected height to be 2 or higher, got '+str(height))

        self.height = height


    def set_border_chars(self, border_chars: tuple[str]) -> None:
        '''
        Sets the symbols of the border to the values in border_char
        '''
        if not isinstance(border_chars, tuple) and not isinstance(border_chars, list):
            raise TypeError('Excpected border_chars to be a tuple, got '+type(border_chars).__name__)
        if len(border_chars) != 6:
            raise TypeError('Excpected border_chars to have a length of 6, got '+str(len(border_chars)))
        for item in border_chars:
            if not isinstance(item, str):
                raise TypeError('Excpected index '+str(border_chars.index(item))+' border_chars to be a str, got '+type(border_chars).__name__)
            if len(item) != 1:
                raise TypeError('Excpected index '+str(border_chars.index(item))+' border_chars to have a length of 1, got '+str(len(item)))
            
        self.border_chars = border_chars


    def set_fill_char(self, fill_char: str) -> None:
        '''
        Sets the symbol to fill the rectangle to the value of fill_char
        '''
        if not isinstance(fill_char, str):
            raise TypeError('Excpected fill_char to be a str, got '+type(fill_char).__name__)
        if len(fill_char) != 1:
            raise TypeError('Excpected fill_char to have a length of 1, got '+str(len(fill_char)))

        self.fill_char = fill_char


    def set_text(self, text: str) -> None:
        '''
        Sets the text of the border to the value of text
        '''
        if not isinstance(text, str):
            raise TypeError('Excpected text to be a str, got '+type(text).__name__)
        
        self.text = text


    def set_align(self, align: str) -> None:
        '''
        Sets the align of the text in the rectangle
        '''
        if not isinstance(align, str):
            raise TypeError('Excpected align to be a str, got '+type(align).__name__)
        
        self.align = align


    def get_width(self) -> int:
        '''
        Returns the width of the rectangle
        '''
        return self.width
    

    def get_height(self) -> int:
        '''
        Returns the height of the rectangle
        '''
        return self.height
    

    def get_border_chars(self) -> int:
        '''
        Returns the border_chars of the rectangle
        '''
        return self.border_chars
    

    def get_fill_char(self) -> int:
        '''
        Returns the fill_char of the rectangle
        '''
        return self.fill_char
    

    def get_text(self) -> str:
        '''
        Returns the text of the rectangle
        '''
        return self.text
    

    def get_align(self) -> str:
        '''
        Returns the text align of the rectangle
        '''
        return self.align


    def draw(self):
        '''
        Prints the rectangle to the terminal
        '''
        print(self.get_str())


    def get_str(self) -> str:
        '''
        Returns the rectangle as string
        '''
        return str(self)
    

    def __str__(self) -> str:
        rectangle = ''


        text = self.text.strip()
        text = text.replace('\n', '')
        text = text.split(' ')

        text_parts = ['']

        i = 0
        while True:
            text_parts.append('')
            while text != []:
                if len(text_parts[i]) + len(' '+text[0]) <= self.width-4 and len(text_parts[i]) != 0:
                    text_parts[i] += ' '+text[0]
                    text.pop(0)
                    continue
                elif len(text_parts[i]) + len(text[0]) <= self.width-4 and len(text_parts[i]) == 0:
                    text_parts[i] += text[0]
                    text.pop(0)
                    continue
                elif len(text_parts[i]) == 0 and len(text[0]) > self.width-4:
                    text_parts[i] += text[0][:self.width-4]
                    text[0] = text[0][self.width-4:]
                break
            if text_parts[-2] == '':
                break
            i += 1

        while text_parts[-1] == '':
            text_parts.pop(-1)

        if self.height-2 < len(text_parts):
            while self.height-2 <= len(text_parts):
                text_parts.pop(-1)
            text_parts.append('...')
        else:
            while self.height-2 > len(text_parts):
                text_parts.append('')

        rectangle += self.border_chars[2] + self.border_chars[1] * (self.width-2) + self.border_chars[3] + '\n'
        for i in range(self.height-2):
            rectangle += self.border_chars[0] + self.fill_char
            if self.align == TextAlign.CENTER:
                rectangle += text_parts[i].center(self.width-4, self.fill_char)
            elif self.align == TextAlign.RIGHT:
                rectangle += text_parts[i].rjust(self.width-4, self.fill_char)
            elif self.align == TextAlign.LEFT:
                rectangle += text_parts[i].ljust(self.width-4, self.fill_char)
            rectangle += self.fill_char + self.border_chars[0] + '\n'
        rectangle += self.border_chars[4] + self.border_chars[1] * (self.width-2) + self.border_chars[5]

        return rectangle
    

    def __copy__(self) -> any:
        return self.copy()
    

    def __deepcopy__(self) -> any:
        return self.copy()



class Line:
    def __init__(self, startx: int, starty: int, endx: int, endy: int, *, symbol: str = '#') -> None:
        '''
        Creates a straight line in the terminal
        '''
        if not isinstance(startx, int):
            raise TypeError('Excpected startx to be an int, got '+type(startx).__name__)
        if not isinstance(starty, int):
            raise TypeError('Excpected starty to be an int, got '+type(starty).__name__)
        if not isinstance(endx, int):
            raise TypeError('Excpected endx to be an int, got '+type(endx).__name__)
        if not isinstance(endy, int):
            raise TypeError('Excpected endy to be an int, got '+type(endy).__name__)
        if not isinstance(symbol, str):
            raise TypeError('Excpected symbol to be an str, got '+type(symbol).__name__)
        if len(symbol) != 1:
            raise ValueError('Excpected symbol to have a length of 1, got '+str(len(symbol)))   

        self.startx: int = startx
        self.starty: int = starty
        self.endx: int = endx
        self.endy: int = endy
        self.symbol: str = symbol


    def copy(self) -> any:
        '''
        Returns a copy of this line
        '''
        line = Line(self.startx, self.starty, self.endx, self.endy, symbol=self.symbol)
        return line


    def get_start_pos(self) -> tuple[int]:
        '''
        Returns the start position as tuple
        '''
        return (self.startx, self.starty)
    

    def get_end_pos(self) -> tuple[int]:
        '''
        Returns the end position as tuple
        '''
        return (self.endx, self.endy)
    

    def get_symbol(self) -> str:
        '''
        Returns the symbol of the line
        '''
        return self.symbol
    

    def get_gradient(self) -> float:
        '''
        Returns the gradient of the line
        Returns None if the angle is 90°
        '''
        try:
            return (self.endy-self.starty)/(self.endx-self.startx)
        except ZeroDivisionError:
            return None


    def set_start_pos(self, startx: int, starty: int) -> None:
        '''
        Sets the start position to (startx, starty)
        '''
        if not isinstance(startx, int):
            raise TypeError('Excpected startx to be an int, got '+type(startx).__name__)
        if not isinstance(starty, int):
            raise TypeError('Excpected starty to be an int, got '+type(starty).__name__)

        self.startx = startx
        self.starty = starty
    

    def set_end_pos(self, endx: int, endy: int) -> None:
        '''
        Sets the end position to (endx, endy)
        '''
        if not isinstance(endx, int):
            raise TypeError('Excpected endx to be an int, got '+type(endx).__name__)
        if not isinstance(endy, int):
            raise TypeError('Excpected endy to be an int, got '+type(endy).__name__)

        self.endx = endx
        self.endy = endy
    

    def set_symbol(self, symbol: str) -> None:
        '''
        Sets the symbol of the line
        '''
        if not isinstance(symbol, str):
            raise TypeError('Excpected symbol to be an str, got '+type(symbol).__name__)
        if len(symbol) != 1:
            raise ValueError('Excpected symbol to have a length of 1, got '+str(len(symbol))) 
          
        self.symbol = symbol

    
    def draw(self) -> None:
        '''
        Prints the line to the terminal
        '''
        print(self.get_str())


    def get_str(self) -> str:
        '''
        Returns the line as multiline string
        '''
        return str(self)


    def __str__(self) -> str:
        try:
            m = (self.endy-self.starty)/(self.endx-self.startx)
        except ZeroDivisionError:
            m = '90'
        
        endx, startx = self.endx, self.startx

        if self.endy < self.starty:
            endy, starty = self.starty, self.endy
        else:
            endy, starty = self.endy, self.starty

        line = []

        lines = max(starty, endy)+1 + (0 if min(starty, endy) >= 0 else abs(min(starty, endy)))

        for _ in range(lines):
            if min(startx, endx) < 0:
                line.append([' ']*(max(startx, endx)+abs(min(startx, endx))+1))
            else:
                line.append([' ']*(max(startx, endx)+1))

        line[starty][startx] = self.symbol
        line[endy][endx] = self.symbol

        x = startx
        y = starty
        while x < endx or y < endy:
            if m != '90':
                x += 1
                y += m
                if len(line)-1 < int(y) or len(line[int(y)])-1 < x or x < 0 or y < 0:
                    break
                line[int(y)][x] = self.symbol
            else:
                y += 1
                if len(line)-1 < int(y) or len(line[int(y)])-1 < x or x < 0 or y < 0:
                    break
                line[int(y)][x] = self.symbol


        for i, row in enumerate(line):
            if not self.symbol in row and i != 0 and i > starty:
                line[i] = line[i-1] 

        line_str = ''

        for row in line:
            line_str += ''.join(row) + '\n'

        return line_str[:len(line_str)-1]
    

    def __copy__(self) -> any:
        return self.copy()
    

    def __deepcopy__(self) -> any:
        return self.copy()
from widgets.text import *
import json, pathlib


class BorderStyle:
    ASCII               = ("-", "|", "+", "+", "+", "+", "+", "+", "+", "+", "+")
    BASIC               = ("—", "|", "+", "+", "+", "+", "+", "+", "+", "+", "+")
    LIGHT               = ("─", "│", "┌", "┬", "┐", "├", "┼", "┤", "└", "┴", "┘")
    HEAVY               = ("━", "┃", "┏", "┳", "┓", "┣", "╋", "┫", "┗", "┻", "┛")
    DOUBLE              = ("═", "║", "╔", "╦", "╗", "╠", "╬", "╣", "╚", "╩", "╝")
    LIGHT_ARC           = ("─", "│", "╭", "┬", "╮", "├", "┼", "┤", "╰", "┴", "╯")
    LIGHT_DASHED        = ("╌", "┊", "┌", "┬", "┐", "├", "┼", "┤", "└", "┴", "┘")
    HEAVY_DASHED        = ("╍", "┋", "┏", "┳", "┓", "┣", "╋", "┫", "┗", "┻", "┛")
    HORIZONTAL_LIGHT    = ("─", " ", "─", "─", "─", "─", "─", "─", "─", "─", "─")
    VERTICAL_LIGHT      = (" ", "│", "│", "│", "│", "│", "│", "│", "│", "│", "│")
    HORIZONTAL_HEAVY    = ("━", " ", "━", "━", "━", "━", "━", "━", "━", "━", "━")
    VERTICAL_HEAVY      = (" ", "┃", "┃", "┃", "┃", "┃", "┃", "┃", "┃", "┃", "┃")
    NO_BORDER           = (" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ")
    MY_STYLES           = {}


    def create_style_from_tuple(self, name: str, style: tuple) -> None:
        if len(style) != 11:
            raise ValueError('Excpected a tuple with length 11')
        
        self.MY_STYLES[name] = style


    def create_style(self, name: str, vertical_line: str, horizontal_line: str, upper_left_corner: str,
                     upper_T_corner: str, upper_right_corner: str, left_T_corner: str,
                     X_cross: str, right_T_corner: str, lower_left_corner: str,
                     lower_T_corner: str, lower_right_corner: str) -> None:
        self.MY_STYLES[name] = (vertical_line, horizontal_line, upper_left_corner,
                                upper_T_corner, upper_right_corner, left_T_corner,
                                X_cross, right_T_corner, lower_left_corner,
                                lower_T_corner, lower_right_corner)


class TableStyle:
    DEFAULT                             = 'default'
    WITHOUT_HEADER_ROW                  = 'without_header_row'
    WITHOUT_FIRST_COLUMN                = 'without_first_column'
    WITHOUT_HEADER_ROW_AND_FIRST_COLUMN = 'without_header_row_and_first_column'
    WITHOUT_BORDER                      = 'without_border'
    ONLY_BORDER                         = 'only_border'


class TableValues:
    def __init__(self, header_row: list = [], first_column: list = []):
        self.header_row: list[list[str, int, TextAlign]] = header_row
        self.first_column: list[list[str, int, TextAlign]] = first_column
        self.values: dict[tuple[int, int], list[str, int, TextAlign]] = {}


    def set_header_row(self, header_row: list) -> None:
        '''
        Sets the header row of your TableValues
        '''
        for i in range(len(header_row)):
            header_row[i] = [header_row[i], len(header_row[i]), TextAlign.RIGHT]
        self.header_row = header_row


    def set_first_column(self, first_column: list) -> None:
        '''
        Sets the first column of your TableValues
        '''
        for i in range(len(first_column)):
            first_column[i] = [first_column[i], len(first_column[i]), TextAlign.RIGHT]
        self.first_column = first_column


    def set_first_column_align_at_position(self, pos: int, align: TextAlign) -> None:
        '''
        Sets the align for an first column item
        '''
        self.first_column[pos][2] = align


    def set_header_row_align_at_position(self, pos: int, align: TextAlign) -> None:
        '''
        Sets the align for an header row item
        '''
        self.header_row[pos][2] = align

    
    def set_first_column_align(self, align: TextAlign) -> None:
        '''
        Sets the align for the first column
        '''
        for i in range(len(self.first_column)):
            self.first_column[i][2] = align


    def set_header_row_align(self, align: TextAlign) -> None:
        '''
        Sets the align for the header row
        '''
        for i in range(len(self.header_row)):
            self.header_row[i][2] = align

    
    def set_text_at_cell(self, row: int, column: int, text: str) -> None:
        '''
        Changes the text of the cell at the position
        '''
        self.values[(row, column)] = [text, len(text), TextAlign.RIGHT]

    
    def set_align_at_cell(self, row: int, column: int, align: TextAlign) -> None:
        '''
        Sets the align of the cell at the position
        '''
        self.values[(row, column)][2] = align
    
    
    def set_align(self, align: TextAlign) -> None:
        '''
        Sets the align of all cells
        '''
        for col_index in range(len(self.first_column)):
            for row_index in range(len(self.header_row)):
                self.values[(row_index, col_index)][2] = align


    def get_text_from_cell(self, row: int, column: int) -> str:
        '''
        Returns the text of the cell at the position
        '''
        return self.values[(row, column)][0]
    

    def get_textlength_from_cell(self, row: int, column: int) -> int:
        '''
        Returns the length of the cell at the position
        '''
        return self.values[(row, column)][1]


    def get_align_from_cell(self, row: int, column: int) -> TextAlign:
        '''
        Returns the align of the cell at the position
        '''
        return self.values[(row, column)][2]
    

class Table:
    '''
    Creates a new Table object.

    Parameters:
        - `title`  str, the title of your table
        - `columns`  int, the amount of columns of your table
        - `rows`  int, the amount of rows of your table
    '''


    def __init__(self, title: str = '', columns: int = 0, rows: int = 0, *, values: TableValues = TableValues(), style: TableStyle = TableStyle.DEFAULT, borderstyle: BorderStyle = BorderStyle.LIGHT, default_cell_length: int = 6, hide_title: bool = False) -> None:
        self.title: str = title
        self.columns: int = columns
        self.rows: int = rows
        self.values: TableValues = values
        self.style: TableStyle = style
        self.borderstyle: BorderStyle = borderstyle
        self.default_cell_length: int = default_cell_length
        self.hide_title: bool = hide_title


    def set_title(self, title: str) -> None:
        '''
        Sets the title of your Table

        Parameters:
            - `title`  str, the title of your table
        '''
        self.title = title


    def set_columns(self, columns: int) -> None:
        '''
        Sets the amount of columns of your Table

        Parameters:
            - `columns`  int, the amount of columns of your table
        '''
        self.columns = columns


    def set_rows(self, rows: int) -> None:
        '''
        Sets the amount of rows of your Table

        Parameters:
            - `rows`  int, the amount of rows of your table
        '''
        self.rows = rows


    def set_values(self, values: TableValues) -> None:
        '''
        Sets the Table values
        '''
        self.values = values
        if self.rows != len(values.first_column):
            self.rows = len(values.first_column)
        if self.columns != len(values.header_row):
            self.columns = len(values.header_row)


    def set_default_cell_length(self, default_cell_length: int) -> None:
        '''
        Sets the default length of all cells
        '''
        self.default_cell_length = default_cell_length


    def set_cell_color(self, row, column, color: ColoredText) -> None:
        '''
        Sets the color of the cell at the position
        '''
        self.values.values[(row, column)][0] = color + self.values.get_text_from_cell(row, column) + ColoredText.END


    def set_header_row_color(self, color: ColoredText) -> None:
        '''
        Sets the color of the header row
        '''
        for i in range(len(self.values.header_row)):
            self.values.header_row[i][0] = color + self.values.header_row[i][0] + color


    def set_first_column_color(self, color: ColoredText) -> None:
        '''
        Sets the color of the first column
        '''
        for i in range(len(self.values.first_column)):
            self.values.first_column[i][0] = color + self.values.first_column[i][0] + color


    def set_border_style(self, borderstyle: BorderStyle) -> None:
        '''
        Sets the style of the border
        '''
        self.borderstyle = borderstyle


    def set_hide_title(self, hide_title: bool) -> None:
        '''
        Hide or shows the title of the table
        '''
        self.hide_title = hide_title

    
    def set_style(self, style: TableStyle) -> None:
        '''
        Sets the style of the table
        '''
        self.style = style


    def get_longest_row_length(self) -> int:
        '''
        Returns the length of the longest text in any cell
        '''
        longest_row_length = self.default_cell_length
        for col_index in range(self.columns):
            for row_index in range(self.rows):
                row_length = self.values.get_textlength_from_cell(row_index, col_index)
                if row_length > longest_row_length:
                    longest_row_length = row_length
        for item in self.values.header_row + self.values.first_column:
            if item[1] > longest_row_length:
                longest_row_length = item[1]
        return longest_row_length


    def get_str(self) -> str:
        '''
        Returns the table as string
        '''
        return str(self)


    def get_list(self) -> list:
        '''
        Returns the table as list
        '''
        list_of_content = [self.title]

        header_content = [' ']
        for item in self.values.header_row:
            header_content.append(item[0])

        list_of_content.append(header_content)

        for i in range(len(self.values.first_column)):
            line = [self.values.first_column[i][0]]
            for x in range(len(self.values.header_row)):
                line.append(self.values.values[(x, i)][0])

            list_of_content.append(line)

        return list_of_content
    

    def get_tuple(self) -> tuple:
        '''
        Returns the table as tuple
        '''
        tuple_of_content = [self.title]

        header_content = [' ']
        for item in self.values.header_row:
            header_content.append(item[0])

        tuple_of_content.append(tuple(header_content))

        for i in range(len(self.values.first_column)):
            line = [self.values.first_column[i][0]]
            for x in range(len(self.values.header_row)):
                line.append(self.values.values[(x, i)][0])

            tuple_of_content.append(tuple(line))

        return tuple(tuple_of_content)
    

    def get_dict(self) -> dict:
        '''
        Returns the table as dictionary
        '''
        dict_of_content = {'title': self.title,
                           'header_row': self.values.header_row.copy(),
                           'first_column': self.values.first_column.copy(),
                           'values': self.values.values.copy()}

        return dict_of_content


    def create_from_dict(self, dict_of_content: dict) -> None:
        '''
        Creates the table from the data in the dict
        '''
        self.set_title(dict_of_content['title'])

        values = TableValues(header_row=dict_of_content['header_row'],
                             first_column=dict_of_content['first_column'])
        values.values = dict_of_content['values']

        self.set_values(values)


    def create_from_list(self, list_of_content: list) -> None:
        '''
        Creates the table from the data in the list
        '''
        self.set_title(list_of_content[0])

        header_row = []
        for item in list_of_content[1][1:]:
            header_row.append([item, len(item), TextAlign.RIGHT])

        first_column = []
        values = {}
        for row_index in range(2, len(list_of_content)):
            first_column.append([list_of_content[row_index][0], len(list_of_content[row_index][0]), TextAlign.RIGHT])

            for column_index in range(1, len(list_of_content[row_index])):
                text = list_of_content[row_index][column_index]
                values[(row_index-2, column_index-1)] = [text, len(text), TextAlign.RIGHT]

        tablevalues = TableValues(header_row=header_row,
                             first_column=first_column)
        tablevalues.values = values

        self.set_values(tablevalues)


    def create_from_tuple(self, tuple_of_content: tuple) -> None:
        '''
        Creates the table from the data in the tuple
        '''
        self.set_title(tuple_of_content[0])

        header_row = []
        for item in tuple_of_content[1][1:]:
            header_row.append([item, len(item), TextAlign.RIGHT])

        first_column = []
        values = {}
        for row_index in range(2, len(tuple_of_content)):
            first_column.append([tuple_of_content[row_index][0], len(tuple_of_content[row_index][0]), TextAlign.RIGHT])

            for column_index in range(1, len(tuple_of_content[row_index])):
                text = tuple_of_content[row_index][column_index]
                values[(row_index-2, column_index-1)] = [text, len(text), TextAlign.RIGHT]

        tablevalues = TableValues(header_row=header_row,
                             first_column=first_column)
        tablevalues.values = values

        self.set_values(tablevalues)


    def is_title_hidden(self) -> bool:
        '''
        Returns the state of `hide_title`
        '''
        return self.hide_title


    def save_in_file(self, filename: str = 'Table') -> None:
        '''
        Saves the table in the file .`filename`.table
        '''
        if not pathlib.Path(f'.{filename}.table').exists():
            with open(f'.{filename}.table', 'w', encoding='utf-8') as file:
                file.write(str(self.get_dict()))
        
        else:
            num = 1
            while pathlib.Path(f'.{filename}{num}.table').exists():
                num += 1
            with open(f'.{filename}{num}.table', 'w', encoding='utf-8') as file:
                file.write(str(self.get_dict()))


    def load_from_file(self, filename: str) -> None:
        '''
        Loads the table from the file .`filename`.table
        '''
        
        if pathlib.Path(f'.{filename}.table').exists():
            with open(f'.{filename}.table', 'r', encoding='utf-8') as file:
                self.create_from_dict(eval(file.read()))
        else:
            raise FileNotFoundError(f'The file .{filename}.table does not exist')


    def print(self) -> None:
        '''
        Prints your Table
        '''
        print(self.get_str())

    
    def __str__(self) -> str:
        table = ''

        longest_row_length = self.get_longest_row_length()

        if not self.hide_title:
            title_length = longest_row_length * (self.rows+1) + self.rows+2
            title = self.title
            title = title.center(title_length)
            
            table += FormatedText.BOLD + title.title() + FormatedText.BOLD + '\n\n'

        if self.style != TableStyle.WITHOUT_BORDER:
            if self.style not in [TableStyle.WITHOUT_FIRST_COLUMN, TableStyle.WITHOUT_HEADER_ROW_AND_FIRST_COLUMN]:
                if self.style == TableStyle.ONLY_BORDER:
                    table += self.borderstyle[2] + (self.borderstyle[0] * longest_row_length + self.borderstyle[0]) * (self.columns) + self.borderstyle[0] * longest_row_length + self.borderstyle[4] + '\n'
                else:
                    table += self.borderstyle[2] + (self.borderstyle[0] * longest_row_length + self.borderstyle[3]) * (self.columns) + self.borderstyle[0] * longest_row_length + self.borderstyle[4] + '\n'
            else:
                table += self.borderstyle[2] + (self.borderstyle[0] * longest_row_length + self.borderstyle[3]) * (self.columns-1) + self.borderstyle[0] * longest_row_length + self.borderstyle[4] + '\n'
        
        if self.style not in [TableStyle.WITHOUT_HEADER_ROW, TableStyle.WITHOUT_HEADER_ROW_AND_FIRST_COLUMN]:
            if self.style not in [TableStyle.WITHOUT_FIRST_COLUMN, TableStyle.WITHOUT_HEADER_ROW_AND_FIRST_COLUMN]:
                if self.style != TableStyle.WITHOUT_BORDER:
                    table += self.borderstyle[1] + ' ' * longest_row_length
                else:
                    table += ' ' * longest_row_length

            for item in self.values.header_row:
                text = TextAlign.set_text_align(item[0], longest_row_length, item[2])
                if self.style != TableStyle.ONLY_BORDER:
                    table += self.borderstyle[1] + FormatedText.BOLD + text + FormatedText.END
                else:
                    table += ' ' + FormatedText.BOLD + text + FormatedText.END

            if self.style != TableStyle.WITHOUT_BORDER:
                table += self.borderstyle[1] + '\n'
            else:
                table += '\n'

        for print_row in range(self.rows*2+1):
            if print_row == self.rows*2:
                if self.style != TableStyle.WITHOUT_BORDER:
                    if self.style not in [TableStyle.WITHOUT_FIRST_COLUMN, TableStyle.WITHOUT_HEADER_ROW_AND_FIRST_COLUMN]:
                        if self.style == TableStyle.ONLY_BORDER:
                            table += self.borderstyle[8] + (self.borderstyle[0] * longest_row_length + self.borderstyle[0]) * (self.columns) + self.borderstyle[0] * longest_row_length + self.borderstyle[10] + '\n'
                        else:
                            table += self.borderstyle[8] + (self.borderstyle[0] * longest_row_length + self.borderstyle[9]) * (self.columns) + self.borderstyle[0] * longest_row_length + self.borderstyle[10] + '\n'
                    else:
                        table += self.borderstyle[8] + (self.borderstyle[0] * longest_row_length + self.borderstyle[9]) * (self.columns-1) + self.borderstyle[0] * longest_row_length + self.borderstyle[10] + '\n'
            elif print_row % 2 == 0:
                if self.style in [TableStyle.WITHOUT_HEADER_ROW, TableStyle.WITHOUT_HEADER_ROW_AND_FIRST_COLUMN]:
                    if print_row != 0:
                        if self.style == TableStyle.ONLY_BORDER:
                            table += self.borderstyle[1] + (' ' * (longest_row_length + 1)) * (self.columns) + ' ' * longest_row_length + self.borderstyle[1] + '\n'
                        elif self.style not in [TableStyle.WITHOUT_FIRST_COLUMN, TableStyle.WITHOUT_HEADER_ROW_AND_FIRST_COLUMN]:
                            table += (self.borderstyle[5] if self.style != TableStyle.WITHOUT_BORDER else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if self.style != TableStyle.WITHOUT_BORDER else '') + '\n'
                        else:
                            table += (self.borderstyle[5] if self.style != TableStyle.WITHOUT_BORDER else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns-1) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if self.style != TableStyle.WITHOUT_BORDER else '') + '\n'
                else:
                    if self.style == TableStyle.ONLY_BORDER:
                        table += self.borderstyle[1] + (' ' * (longest_row_length + 1)) * (self.columns) + ' ' * longest_row_length + self.borderstyle[1] + ' \n'
                    elif self.style not in [TableStyle.WITHOUT_FIRST_COLUMN, TableStyle.WITHOUT_HEADER_ROW_AND_FIRST_COLUMN]:
                        table += (self.borderstyle[5] if self.style != TableStyle.WITHOUT_BORDER else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if self.style != TableStyle.WITHOUT_BORDER else '') + '\n'
                    else:
                        table += (self.borderstyle[5] if self.style != TableStyle.WITHOUT_BORDER else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns-1) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if self.style != TableStyle.WITHOUT_BORDER else '') + '\n'
            else:
                if self.style not in [TableStyle.WITHOUT_FIRST_COLUMN, TableStyle.WITHOUT_HEADER_ROW_AND_FIRST_COLUMN]:
                    item = self.values.first_column[print_row//2]
                    text = TextAlign.set_text_align(item[0], longest_row_length, item[2])
                    if self.style != TableStyle.WITHOUT_BORDER:
                        table += self.borderstyle[1] + FormatedText.BOLD + text + FormatedText.END
                    else:
                        table += FormatedText.BOLD + text + FormatedText.END
                    

                for x in range(self.columns):
                    text = self.values.get_text_from_cell(print_row//2, x)
                    text = TextAlign.set_text_align(text, longest_row_length, self.values.get_align_from_cell(print_row//2, x))
                    if self.style != TableStyle.ONLY_BORDER:
                        table += self.borderstyle[1] + text
                    else:
                        table += ' ' + text

                if self.style != TableStyle.WITHOUT_BORDER:
                    table += self.borderstyle[1] + '\n'
                else:
                    table += '\n'

        return table
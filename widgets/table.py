from widgets.text import *
import pathlib, os, copy


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
        '''
        Creates a border style from a tuple
        '''
        if not isinstance(style, tuple) and not isinstance(style, list):
            raise TypeError('Expected style to be a tuple, got '+type(style).__name__)
        if len(style) != 11:
            raise ValueError('Excpected style to be a tuple with length 11')
        for item in style:
            if not isinstance(item, str):
                raise TypeError('Expected style to be a tuple of strings, got tuple of '+type(item).__name__)
            if len(item) != 1:
                raise ValueError('Excpected style to be a tuple of single characters or symbols')
        
        self.MY_STYLES[name] = style


    def create_style(self, name: str, vertical_line: str, horizontal_line: str, upper_left_corner: str,
                     upper_T_corner: str, upper_right_corner: str, left_T_corner: str,
                     X_cross: str, right_T_corner: str, lower_left_corner: str,
                     lower_T_corner: str, lower_right_corner: str) -> None:
        self.MY_STYLES[name] = (vertical_line, horizontal_line, upper_left_corner,
                                upper_T_corner, upper_right_corner, left_T_corner,
                                X_cross, right_T_corner, lower_left_corner,
                                lower_T_corner, lower_right_corner)
        for style in self.MY_STYLES[name]:
            if not isinstance(style, str):
                return TypeError('Excpected argument at position '+str(self.MY_STYLES[name].index(style)+2)+' to be a string, got '+type(style).__name__)
            if len(style) != 1:
                raise ValueError('Excpected argument at position '+str(self.MY_STYLES[name].index(style)+2)+' to be a single character or symbol')



class TableStyle:
    DEFAULT                             = 'default'
    WITHOUT_HEADER_ROW                  = 'without_header_row'
    WITHOUT_FIRST_COLUMN                = 'without_first_column'
    WITHOUT_BORDER                      = 'without_border'
    ONLY_BORDER                         = 'only_border'


class TableValues:
    def __init__(self, header_row: list = None, first_column: list = None):
        if header_row and not isinstance(header_row, list):
            raise TypeError('Excpected header_row to be a list, got '+type(header_row).__name__)
        if first_column and not isinstance(first_column, list):
            raise TypeError('Excpected first_column to be a list, got '+type(first_column).__name__)

        self.header_row: list[list[str, int, str]] = header_row if header_row else []
        self.first_column: list[list[str, int, str]] = first_column if first_column else []
        self.values: dict[tuple[int, int], list[str, int, str]] = {}

        self.align = TextAlign.RIGHT
        self.first_column_align = TextAlign.RIGHT
        self.header_row_align = TextAlign.RIGHT

    
    def help(self) -> None:
        '''
        Prints an overview of all methods in the terminal
        '''
        print(os.system('python3 -c "from widgets.table import TableValues; help(TableValues)"'))


    def set_header_row(self, header_row: list) -> None:
        '''
        Sets the header row of your TableValues
        '''
        if not isinstance(header_row, list) and not isinstance(header_row, tuple):
            raise TypeError('Excpected header_row to be a list, got '+type(header_row).__name__)
        for item in header_row:
            if not isinstance(item, str):
                raise TypeError('Excpected item at index '+str(header_row.index(item))+' to be a str, got '+type(item).__name__)
        
        for i in range(len(header_row)):
            header_row[i] = [header_row[i], len(header_row[i]), self.header_row_align]
        self.header_row = header_row


    def set_first_column(self, first_column: list) -> None:
        '''
        Sets the first column of your TableValues
        '''
        if not isinstance(first_column, list) and not isinstance(first_column, tuple):
            raise TypeError('Excpected first_column to be alist, got '+type(first_column).__name__)
        for item in first_column:
            if not isinstance(item, str):
                raise TypeError('Excpected item at index '+str(first_column.index(item))+' to be a str, got '+type(item).__name__)
        
        for i in range(len(first_column)):
            first_column[i] = [first_column[i], len(first_column[i]), self.first_column_align]
        self.first_column = first_column


    def set_first_column_align_at_position(self, pos: int, align: str) -> None:
        '''
        Sets the align for an first column item
        '''
        if not isinstance(pos, int):
            raise TypeError('Excpected pos to be an int, got '+type(pos).__name__)
        if not isinstance(align, str):
            raise TypeError('Excpected align to be a str, got '+type(align).__name__)

        self.first_column[pos][2] = align


    def set_header_row_align_at_position(self, pos: int, align: str) -> None:
        '''
        Sets the align for an header row item
        '''
        if not isinstance(pos, int):
            raise TypeError('Excpected pos to be an int, got '+type(pos).__name__)
        if not isinstance(align, str):
            raise TypeError('Excpected align to be a str, got '+type(align).__name__)
        
        self.header_row[pos][2] = align

    
    def set_first_column_align(self, align: str) -> None:
        '''
        Sets the align for the first column
        '''
        if not isinstance(align, str):
            raise TypeError('Excpected align to be a str, got '+type(align).__name__)
        
        for i in range(len(self.first_column)):
            self.first_column[i][2] = align
        
        self.first_column_align = align


    def set_header_row_align(self, align: str) -> None:
        '''
        Sets the align for the header row
        '''
        if not isinstance(align, str):
            raise TypeError('Excpected align to be a str, got '+type(align).__name__)
        
        for i in range(len(self.header_row)):
            self.header_row[i][2] = align
        
        self.header_row_align = align

    
    def set_text_at_cell(self, row: int, column: int, text: str) -> None:
        '''
        Changes the text of the cell at the position
        '''
        if not isinstance(row, int):
            raise TypeError('Excpected row to be an int, got '+type(row).__name__)
        if not isinstance(column, int):
            raise TypeError('Excpected column to be an int, got '+type(column).__name__)
        if not isinstance(text, str):
            raise TypeError('Excpected text to be a str, got '+type(text).__name__)
        
        self.values[(row, column)] = [text, len(text), self.align]

    
    def set_align_at_cell(self, row: int, column: int, align: str) -> None:
        '''
        Sets the align of the cell at the position
        '''
        if not isinstance(row, int):
            raise TypeError('Excpected row to be an int, got '+type(row).__name__)
        if not isinstance(column, int):
            raise TypeError('Excpected column to be an int, got '+type(column).__name__)
        if not isinstance(align, str):
            raise TypeError('Excpected align to be a str, got '+type(align).__name__)
        
        self.values[(row, column)][2] = align
    
    
    def set_align(self, align: str) -> None:
        '''
        Sets the align of all cells
        '''
        if not isinstance(align, str):
            raise TypeError('Excpected align to be a str, got '+type(align).__name__)
        
        for key in self.values.keys():
            self.values[key][2] = align

        self.align = align


    def get_text_from_cell(self, row: int, column: int) -> str:
        '''
        Returns the text of the cell at the position
        '''
        if not isinstance(row, int):
            raise TypeError('Excpected row to be an int, got '+type(row).__name__)
        if not isinstance(column, int):
            raise TypeError('Excpected column to be an int, got '+type(column).__name__)
        
        return self.values[(row, column)][0]
    

    def get_cell_with_text(self, text: str) -> tuple[int, int] | None:
        '''
        Returns the first position of the text
        Returns None if the text don't appears in the table
        '''
        if not isinstance(text, str):
            raise TypeError('Excpected text to be a str, got '+type(text).__name__)

        for key in self.values.keys():
            if self.values[key][0] == text:
                return key


    def get_textlength_from_cell(self, row: int, column: int) -> int:
        '''
        Returns the length of the cell at the position
        '''
        if not isinstance(row, int):
            raise TypeError('Excpected row to be an int, got '+type(row).__name__)
        if not isinstance(column, int):
            raise TypeError('Excpected column to be an int, got '+type(column).__name__)
        
        return self.values[(row, column)][1]


    def get_align_from_cell(self, row: int, column: int) -> str:
        '''
        Returns the align of the cell at the position
        '''
        if not isinstance(row, int):
            raise TypeError('Excpected row to be an int, got '+type(row).__name__)
        if not isinstance(column, int):
            raise TypeError('Excpected column to be an int, got '+type(column).__name__)
        
        return self.values[(row, column)][2]
    

    def get_text_from_row(self, row: int) -> list[str, list[str]]:
        '''
        Returns the text of the first column and all texts of the row as list
        '''
        if not isinstance(row, int):
            raise TypeError('Excpected row to be an int, got '+type(row).__name__)
        
        texts = []

        for col in range(len(self.header_row)):
            texts.append(self.values[(row, col)][0])

        return [self.first_column[row][0], texts]
    

    def get_text_from_column(self, column: int) -> list[str, list[str]]:
        '''
        Returns the text of the header row and all texts of the column as list
        '''
        if not isinstance(column, int):
            raise TypeError('Excpected column to be an int, got '+type(column).__name__)
        
        texts = []
        
        for row in range(len(self.first_column)):
            texts.append(self.values[(row, column)][0])

        return [self.header_row[column][0], texts]
    

    def is_numeric_row(self, row: int) -> bool:
        '''
        Returns `True` if the row only includ intergers and floats
        '''
        if not isinstance(row, int):
            raise TypeError('Excpected row to be an int, got '+type(row).__name__)
        
        for col in range(len(self.header_row)):
            if self.values[(row, col)][0].count('.') > 1:
                return False
            elif self.values[(row, col)][0].count('.') == 1 and len(self.values[(row, col)][0]) == 1:
                return False
            for letter in self.values[(row, col)][0].strip():
                if letter not in '1234567890.':
                    return False
        return True


    def is_numeric_column(self, column: int) -> bool:
        '''
        Returns `True` if the column only includ intergers and floats
        '''
        if not isinstance(column, int):
            raise TypeError('Excpected column to be an int, got '+type(column).__name__)

        for row in range(len(self.first_column)):
            if self.values[(row, column)][0].count('.') > 1:
                return False
            elif self.values[(row, column)][0].count('.') == 1 and len(self.values[(row, column)][0]) == 1:
                return False
            for letter in self.values[(row, column)][0].strip():
                if letter not in '1234567890.':
                    return False
        return True
    

    def add_row(self, first_column_value: str = ' ', values: list[str] = [' ']) -> None:
        '''
        Adds a new row to the end of the table
        '''
        if not isinstance(first_column_value, str):
            raise TypeError('Excpected first_column_value to be a str, got '+type(first_column_value).__name__)
        if len(values) != len(self.header_row):
            raise ValueError(f'Expected values to have {len(self.header_row)} values, got {len(values)}')
        if not isinstance(values, list) and not isinstance(values, tuple):
            raise TypeError('Excpected values to be a list, got '+type(values).__name__)
        for item in values:
            if not isinstance(item, str):
                raise TypeError('Excpected index '+str(values.index(item))+' of values to be a str, got '+type(item).__name__)

        if values == [' ']:
            values *= len(self.header_row)
    
        for column in range(len(self.header_row)):
            self.values[(len(self.first_column), column)] = [values[column], len(values[column]), self.align]
        
        self.first_column.append([first_column_value, len(first_column_value), self.first_column_align])


    def insert_row(self, index: int = 0, first_column_value: str = ' ', values: list[str] = [' ']) -> None:
        '''
        Inserts a new row at the index `index` of the table
        '''
        if not isinstance(index, int):
            raise TypeError('Excpected index to be an int, got '+type(index).__name__)
        if index < 0 or index > len(self.header_row):
            raise ValueError('Excpected index with a value between 0 and '+str(len(self.header_row)))
        if not isinstance(first_column_value, str):
            raise TypeError('Excpected first_column_value to be a str, got '+type(first_column_value).__name__)
        if len(values) != len(self.header_row):
            raise ValueError(f'Expected values to have {len(self.header_row)} values, got {len(values)}')
        if not isinstance(values, list) and not isinstance(values, tuple):
            raise TypeError('Excpected values to be a list, got '+type(values).__name__)
        for item in values:
            if not isinstance(item, str):
                raise TypeError('Excpected index '+str(values.index(item))+' of values to be a str, got '+type(item).__name__)

        if values == [' ']:
            values *= len(self.header_row)
    
        new_values = {}
        for key, value in self.values.items():
            if key[0] >= index:
                new_key = (key[0]+1, key[1])
            else:
                new_key = key
            new_values[new_key] = value

        for column in range(len(self.header_row)):
            new_values[(index, column)] = [values[column], len(values[column]), self.align]
        
        self.first_column.insert(index, [first_column_value, len(first_column_value), self.first_column_align])
        self.values = new_values


    def delete_row(self, index: int) -> None:
        '''
        Deletes the row at the index `index` of the table
        '''
        if not isinstance(index, int):
            raise TypeError('Excpected index to be an int, got '+type(index).__name__)
        if index < 0 or index > len(self.header_row):
            raise ValueError('Excpected index with a value between 0 and '+str(len(self.header_row)))
        
        new_values = {}
        for key, value in self.values.items():
            if key[0] > index:
                new_key = (key[0]-1, key[1])
            else:
                new_key = key
            new_values[new_key] = value
        
        self.first_column.pop(index)
        self.values = new_values


    def swap_rows(self, index1: int, index2: int) -> None:
        '''
        Swap the rows at the index `index1` and at the index `index2` of the table
        '''
        if not isinstance(index1, int):
            raise TypeError('Excpected index1 to be an int, got '+type(index1).__name__)
        if index1 < 0 or index1 > len(self.header_row):
            raise ValueError('Excpected index1 with a value between 0 and '+str(len(self.header_row)))
        if not isinstance(index2, int):
            raise TypeError('Excpected index2 to be an int, got '+type(index2).__name__)
        if index2 < 0 or index2 > len(self.header_row):
            raise ValueError('Excpected index2 with a value between 0 and '+str(len(self.header_row)))


        for column_index in range(len(self.header_row)):
            self.values[(index1, column_index)], self.values[(index2, column_index)] = self.values[(index2, column_index)], self.values[(index1, column_index)]
        
        self.first_column[index1], self.first_column[index2] = self.first_column[index2], self.first_column[index1]


    def add_column(self, header_row_value: str = ' ', values: list[str] = [' ']) -> None:
        '''
        Adds a new column to the end of the table
        '''
        if not isinstance(header_row_value, str):
            raise TypeError('Excpected header_row_value to be a str, got '+type(header_row_value).__name__)
        if len(values) != len(self.first_column):
            raise ValueError(f'Expected values to have {len(self.first_column)} values, got {len(values)}')
        if not isinstance(values, list) and not isinstance(values, tuple):
            raise TypeError('Excpected values to be a list, got '+type(values).__name__)
        for item in values:
            if not isinstance(item, str):
                raise TypeError('Excpected index '+str(values.index(item))+' of values to be a str, got '+type(item).__name__)
            
        if values == [' ']:
            values *= len(self.first_column)
    
        for row in range(len(self.first_column)):
            self.values[(row, len(self.header_row))] = [values[row], len(values[row]), self.align]
        
        self.header_row.append([header_row_value, len(header_row_value), self.first_column_align])


    def insert_column(self, index: int = 0, header_row_value: str = ' ', values: list[str] = [' ']) -> None:
        '''
        Inserts a new column at the index `index` of the table
        '''
        if not isinstance(index, int):
            raise TypeError('Excpected index to be an int, got '+type(index).__name__)
        if index < 0 or index > len(self.first_column):
            raise ValueError('Excpected index with a value between 0 and '+str(len(self.first_column)))
        if not isinstance(header_row_value, str):
            raise TypeError('Excpected header_row_value to be a str, got '+type(header_row_value).__name__)
        if len(values) != len(self.first_column):
            raise ValueError(f'Expected values to have {len(self.first_column)} values, got {len(values)}')
        if not isinstance(values, list) and not isinstance(values, tuple):
            raise TypeError('Excpected values to be a list, got '+type(values).__name__)
        for item in values:
            if not isinstance(item, str):
                raise TypeError('Excpected index '+str(values.index(item))+' of values to be a str, got '+type(item).__name__)
            
        if values == [' ']:
            values *= len(self.first_column)
    
        new_values = {}
        for key, value in self.values.items():
            if key[1] >= index:
                new_key = (key[0], key[1]+1)
            else:
                new_key = key
            new_values[new_key] = value

        for row in range(len(self.first_column)):
            new_values[(row, index)] = [values[row], len(values[row]), self.align]
        
        self.header_row.insert(index, [header_row_value, len(header_row_value), self.first_column_align])
        self.values = new_values


    def delete_column(self, index: int) -> None:
        '''
        Deletes the column at the index `index` of the table
        '''
        if not isinstance(index, int):
            raise TypeError('Excpected index to be an int, got '+type(index).__name__)
        if index < 0 or index > len(self.header_row):
            raise ValueError('Excpected index with a value between 0 and '+str(len(self.header_row)))
        
        new_values = {}
        for key, value in self.values.items():
            if key[1] > index:
                new_key = (key[0], key[1]-1)
            else:
                new_key = key
            new_values[new_key] = value
        
        self.header_row.pop(index)
        self.values = new_values


    def swap_columns(self, index1: int, index2: int) -> None:
        '''
        Swap the columns at the index `index1` and at the index `index2` of the table
        '''
        if not isinstance(index1, int):
            raise TypeError('Excpected index1 to be an int, got '+type(index1).__name__)
        if index1 < 0 or index1 > len(self.header_row):
            raise ValueError('Excpected index1 with a value between 0 and '+str(len(self.header_row)))
        if not isinstance(index2, int):
            raise TypeError('Excpected index2 to be an int, got '+type(index2).__name__)
        if index2 < 0 or index2 > len(self.header_row):
            raise ValueError('Excpected index2 with a value between 0 and '+str(len(self.header_row)))
        
        for row_index in range(len(self.first_column)):
            self.values[(row_index, index1)], self.values[(row_index, index2)] = self.values[(row_index, index2)], self.values[(row_index, index1)]
        
        self.header_row[index1], self.header_row[index2] = self.header_row[index2], self.header_row[index1]


    def count(self, text: str, *, search_in_first_column: bool = False, search_in_header_row: bool = False) -> int:
        '''
        Counts how often the text appears in the table
        '''
        if not isinstance(text, str):
            raise TypeError('Excpected text to be a str, got '+type(text).__name__)
        if not isinstance(search_in_first_column, bool):
            raise TypeError('Excpected search_in_first_column to be a bool, got '+type(search_in_first_column).__name__)
        if not isinstance(search_in_header_row, bool):
            raise TypeError('Excpected search_in_header_row to be a bool, got '+type(search_in_header_row).__name__)

        texts = []
        for item in self.values.values():
            texts.append(item[0])
        
        count = texts.count(text)

        if search_in_first_column:
            first_column_texts = []
            for item in self.first_column:
                first_column_texts.append(item[0])
            count += first_column_texts.count(text)

        if search_in_header_row:
            header_row_texts = []
            for item in self.header_row:
                header_row_texts.append(item[0])
            count += header_row_texts.count(text)

        return count


    def sum_row(self, row: int) -> float:
        '''
        Sums all values is this row
        The row must be numeric (`is_numeric_row()`)
        '''
        if not isinstance(row, int):
            raise TypeError('Excpected row to be an int, got '+type(row).__name__)
        if not self.is_numeric_row(row):
            raise ValueError(f'The row {row} is not numeric ( check with is_numeric_row() )')
        
        sum = 0
        for col in range(len(self.header_row)):
            sum += float(self.values[(row, col)][0])

        return sum


    def sum_column(self, column: int) -> float:
        '''
        Sums all values is this column
        The column must be numeric (`is_numeric_column()`)
        '''
        if not isinstance(column, int):
            raise TypeError('Excpected column to be an int, got '+type(column).__name__)
        if not self.is_numeric_column(column):
            raise ValueError(f'The column {column} is not numeric ( check with is_numeric_column() )')
        
        sum = 0
        for row in range(len(self.first_column)):
            sum += float(self.values[(row, column)][0])

        return sum


    def copy(self) -> any:
        '''
        Creates a copy of this object and returns it
        '''
        new_table_values = TableValues(first_column=copy.deepcopy(self.first_column), header_row=copy.deepcopy(self.header_row))

        new_table_values.values = copy.deepcopy(self.values)
        new_table_values.align = self.align
        new_table_values.first_column_align = self.first_column_align
        new_table_values.header_row_align = self.header_row_align

        return new_table_values



class Table:
    '''
    Creates a new Table object.
    '''

    def __init__(self, title: str = '', columns: int = 0, rows: int = 0, *, values: TableValues = None, style: list[str] = [TableStyle.DEFAULT], borderstyle: tuple[str] = BorderStyle.LIGHT, default_cell_length: int = 6, hide_title: bool = False) -> None:
        if not isinstance(title, str):
            raise TypeError('Excpected title to be a str, got '+type(title).__name__)
        if not isinstance(columns, int):
            raise TypeError('Excpected columns to be an int, got '+type(columns).__name__)
        if not isinstance(rows, int):
            raise TypeError('Excpected rows to be an int, got '+type(rows).__name__)
        if not isinstance(values, TableValues) and values:
            raise TypeError('Excpected values to be TableValues, got '+type(values).__name__)
        if not isinstance(style, list):
            raise TypeError('Excpected style to be a list, got '+type(style).__name__)
        if not isinstance(borderstyle, list) and not isinstance(borderstyle, tuple):
            raise TypeError('Excpected borderstyle to be a tuple, got '+type(borderstyle).__name__)
        if len(borderstyle) != 11:
            raise ValueError('Excpected borderstyle to have a length of 11, got '+str(len(borderstyle)))
        if not isinstance(default_cell_length, int):
            raise TypeError('Excpected default_cell_length to be an int, got '+type(default_cell_length).__name__)
        if default_cell_length <= 0:
            raise ValueError('Excpected default_cell_length to be 1 or higher, got '+str(default_cell_length))
        if not isinstance(hide_title, bool):
            raise TypeError('Excpected hide_title to be a bool, got '+type(hide_title).__name__)

        self.title: str = title
        self.columns: int = columns
        self.rows: int = rows
        self.values: TableValues = values if values else TableValues()
        self.style: list[str] = style
        self.borderstyle: tuple[str] = borderstyle
        self.default_cell_length: int = default_cell_length
        self.hide_title: bool = hide_title
        self.hidden_rows: list[tuple[int, int]] = []
        self.hidden_columns: list[tuple[int, int]] = []
        self.sum_row: bool = False
        self.sum_row_columns: list = []
        self.sorted_row_indexes: list[int] = [x for x in range(self.rows)]
        self.sorted_column_indexes: list[int] = [x for x in range(self.columns)]


    def help(self) -> None:
        '''
        Prints an overview of all methods in the terminal
        '''
        print(os.system('python3 -c "from widgets.table import Table; help(Table)"'))


    def set_title(self, title: str) -> None:
        '''
        Sets the title of your Table
        '''
        if not isinstance(title, str):
            raise TypeError('Excpected tiel to be a str, got '+type(title).__name__)
        
        self.title = title


    def set_columns(self, columns: int) -> None:
        '''
        Sets the amount of columns of your Table
        '''
        if not isinstance(columns, int):
            raise TypeError('Excpected columns to be an int, got '+type(columns).__name__)

        self.columns = columns


    def set_rows(self, rows: int) -> None:
        '''
        Sets the amount of rows of your Table
        '''
        if not isinstance(rows, int):
            raise TypeError('Excpected rows to be an int, got '+type(rows).__name__)
        
        self.rows = rows


    def set_values(self, values: TableValues) -> None:
        '''
        Sets the Table values
        '''
        if not isinstance(values, TableValues):
            raise TypeError('Excpected values to be TableValues, got '+type(values).__name__)
        
        self.values = values
        self.rows = len(values.first_column)
        self.columns = len(values.header_row)

        self.sorted_row_indexes = [x for x in range(self.rows)]
        self.sorted_column_indexes = [x for x in range(self.columns)]


    def set_default_cell_length(self, default_cell_length: int) -> None:
        '''
        Sets the default length of all cells
        '''
        if not isinstance(default_cell_length, int):
            raise TypeError('Excpected default_cell_length to be an int, got '+type(default_cell_length).__name__)
        if default_cell_length <= 0:
            raise ValueError('Excpected default_cell_length to be 1 or higher')
        
        self.default_cell_length = default_cell_length


    def set_cell_color(self, row: int, column: int, color: ColoredText) -> None:
        '''
        Sets the color of the cell at the position
        '''
        if not isinstance(row, int):
            raise TypeError('Excpected row to be an int, got '+type(row).__name__)
        if not isinstance(column, int):
            raise TypeError('Excpected column to be an int, got '+type(column).__name__)
        if not isinstance(color, ColoredText) and not isinstance(color, str):
            raise TypeError('Excpected color to be a ColoredText, got '+type(color).__name__)
        
        self.values.values[(row, column)][0] = color + self.values.get_text_from_cell(row, column) + ColoredText.END


    def set_header_row_color(self, color: ColoredText) -> None:
        '''
        Sets the color of the header row
        '''
        if not isinstance(color, ColoredText) and not isinstance(color, str):
            raise TypeError('Excpected color to be a ColoredText, got '+type(color).__name__)
        
        for i in range(len(self.values.header_row)):
            self.values.header_row[i][0] = color + self.values.header_row[i][0] + color


    def set_first_column_color(self, color: ColoredText) -> None:
        '''
        Sets the color of the first column
        '''
        if not isinstance(color, ColoredText) and not isinstance(color, str):
            raise TypeError('Excpected color to be a ColoredText, got '+type(color).__name__)
        
        for i in range(len(self.values.first_column)):
            self.values.first_column[i][0] = color + self.values.first_column[i][0] + color


    def set_border_style(self, borderstyle: tuple) -> None:
        '''
        Sets the style of the border
        '''
        if not isinstance(borderstyle, list) and not isinstance(borderstyle, tuple):
            raise TypeError('Excpected borderstyle to be a tuple, got '+type(borderstyle).__name__)
        if len(borderstyle) != 11:
            raise ValueError('Excpected borderstyle to have a length of 11, got '+str(len(borderstyle)))

        self.borderstyle = borderstyle


    def set_style(self, style: str) -> None:
        '''
        Sets the style of the table
        '''
        if not isinstance(style, str):
            raise TypeError('Excpected style to be a str, got '+type(style).__name__)
        
        self.style = [style]


    def set_styles(self, styles: list[str]) -> None:
        '''
        Sets the styles of the table
        '''
        if not isinstance(styles, list):
            raise TypeError('Excpected styles to be a list, got '+type(styles).__name__)
        for item in styles:
            if not isinstance(item, str):
                raise TypeError('Excpected styles to be a list of str, got list of '+type(item).__name__)
        
        self.style = styles


    def set_hide_title(self, hide_title: bool) -> None:
        '''
        Hide or shows the title of the table
        '''
        if not isinstance(hide_title, bool):
            raise TypeError('Excpected hide_title to be a bool, got '+type(hide_title).__name__)

        self.hide_title = hide_title


    def hide_row(self, row_index: int) -> None:
        '''
        Mark the row as hidden
        '''
        if not isinstance(row_index, int):
            raise TypeError('Excpected row_index to be an int, got '+type(row_index).__name__)
        
        self.hidden_rows.append(row_index)


    def hide_rows(self, row_indexes: list[int]) -> None:
        '''
        Mark the rows as hidden
        '''
        if not isinstance(row_indexes, list):
            raise TypeError('Excpected row_indexes to be an list, got '+type(row_indexes).__name__)
        for item in row_indexes:
            if not isinstance(item, int):
                raise TypeError('Excpected row_indexes to be a list of int, got list of '+type(item).__name__)
        
        self.hidden_rows += row_indexes


    def hide_column(self, column_index: int) -> None:
        '''
        Mark the column as hidden
        '''
        if not isinstance(column_index, int):
            raise TypeError('Excpected column_index to be an int, got '+type(column_index).__name__)
        
        self.hidden_columns.append(column_index)


    def hide_columns(self, column_indexes: list[int]) -> None:
        '''
        Mark the columns as hidden
        '''
        if not isinstance(column_indexes, list):
            raise TypeError('Excpected column_indexes to be a list, got '+type(column_indexes).__name__)
        for item in column_indexes:
            if not isinstance(item, int):
                raise TypeError('Excpected column_indexes to be a list of int, got list of '+type(item).__name__)
            
        self.hidden_columns += column_indexes


    def show_row(self, row_index: int) -> None:
        '''
        Unmark the row as hidden
        '''
        if not isinstance(row_index, int):
            raise TypeError('Excpected row_index to be an int, got '+type(row_index).__name__)
        
        if row_index in self.hidden_rows:
            self.hidden_rows.remove(row_index)


    def show_rows(self, row_indexes: list[int]) -> None:
        '''
        Unmark the rows as hidden
        '''
        if not isinstance(row_indexes, list):
            raise TypeError('Excpected row_indexes to be a list, got '+type(row_indexes).__name__)
        for item in row_indexes:
            if not isinstance(item, int):
                raise TypeError('Excpected row_indexes to be a list of int, got list of '+type(item).__name__)
            
        for index in row_indexes:
            if index in self.hide_rows:
                self.hidden_rows.remove(index)


    def show_column(self, column_index: int) -> None:
        '''
        Unmark the column as hidden
        '''
        if not isinstance(column_index, int):
            raise TypeError('Excpected column_index to be an int, got '+type(column_index).__name__)
        
        if column_index in self.hidden_columns:
            self.hidden_columns.remove(column_index)


    def show_columns(self, column_indexes: list[int]) -> None:
        '''
        Unmark the columns as hidden
        '''
        if not isinstance(column_indexes, list):
            raise TypeError('Excpected column_indexes to be a list, got '+type(column_indexes).__name__)
        for item in column_indexes:
            if not isinstance(item, int):
                raise TypeError('Excpected column_indexes to be a list of int, got list of '+type(item).__name__)
            
        for index in column_indexes:
            if index in self.hide_columns:
                self.hidden_columns.remove(index)

    
    def show_sum_row(self, columns: list[int]) -> None:
        '''
        Adds a row with the sums of the columns in `columns` to the end of the table
        '''
        if not isinstance(columns, list) and not isinstance(columns, tuple):
            raise TypeError('Excpected columns to be a list, got '+type(columns).__name__)
        for item in columns:
            if not isinstance(item, int):
                raise TypeError('Excpected columns to be a list of int, got list of '+type(item).__name__)
        for col in columns:
            if not self.values.is_numeric_column(col):
                raise ValueError(f'The column {col} is not a numeric column ( check with is_numeric_column() )')

        self.sum_row = True
        
        self.sum_row_columns = columns


    def hide_sum_row(self) -> None:
        '''
        Removes the row with the sums of the columns in `columns` at the end of the table
        '''
        self.sum_row = False


    def get_values(self) -> TableValues:
        '''
        Returns the tables values
        '''
        return self.values


    def get_hidden_rows(self) -> list[int]:
        '''
        Returns a list of all hidden rows
        '''
        return self.hidden_rows


    def get_hidden_columns(self) -> list[int]:
        '''
        Returns a list of all hidden columns
        '''
        return self.hidden_columns
    

    def get_longest_cell_length(self) -> int:
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
                line.append(self.values.values[(i, x)][0])

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
                line.append(self.values.values[(i, x)][0])

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


    def is_title_hidden(self) -> bool:
        '''
        Returns the state of `hide_title`
        '''
        return self.hide_title
    

    def is_row_hidden(self, row_index: int) -> bool:
        '''
        Returns True if the row at the index `row_index` is hidden
        '''
        if not isinstance(row_index, int):
            raise TypeError('Excpected row_index to be an int, got '+type(row_index).__name__)
        
        return row_index in self.hidden_rows
    
    
    def is_column_hidden(self, column_index: int) -> bool:
        '''
        Returns True if the column at the index `column_index` is hidden
        '''
        if not isinstance(column_index, int):
            raise TypeError('Excpected column_index to be an int, got '+type(column_index).__name__)
        
        return column_index in self.hidden_columns
    

    def is_sum_row_hidden(self) -> bool:
        '''
        Returns True if the sum row is hidden
        '''
        return not self.sum_row


    def sort_by_row(self, row_index: int, reverse: bool = False) -> None:
        '''
        Sorts the table data by the row at the index `row_index`
        '''
        if not isinstance(row_index, int):
            raise TypeError('Excpected row_index to be an int, got '+type(row_index).__name__)
        if not isinstance(reverse, bool):
            raise TypeError('Excpected reverse to be a bool, got '+type(reverse).__name__)

        self.sorted_column_indexes = []

        row_texts = []
        row_items = []
        for col_index in range(self.columns):
            row_texts.append(self.values.values[(row_index, col_index)][0])
            row_items.append([self.values.values[(row_index, col_index)][0], col_index])
        
        row_texts.sort(reverse=reverse)

        for text in row_texts:
            for item in row_items:
                if text == item[0]:
                    if item[1] not in self.sorted_column_indexes:
                        self.sorted_column_indexes.append(item[1])
                    else:
                        while item[1] in self.sorted_column_indexes:
                            item[1] += 1
                        self.sorted_column_indexes.append(item[1])


    def sort_by_column(self, column_index: int, reverse: bool = False) -> None:
        '''
        Sorts the table data by the col at the index `col_index`
        '''
        if not isinstance(column_index, int):
            raise TypeError('Excpected column_index to be an int, got '+type(column_index).__name__)
        if not isinstance(reverse, bool):
            raise TypeError('Excpected reverse to be a bool, got '+type(reverse).__name__)
        
        self.sorted_row_indexes = []

        col_texts = []
        col_items = []
        for row_index in range(self.rows):
            col_texts.append(self.values.values[(row_index, column_index)][0])
            col_items.append([self.values.values[(row_index, column_index)][0], row_index])
        
        col_texts.sort(reverse=reverse)

        for text in col_texts:
            for item in col_items:
                if text == item[0]:
                    if item[1] not in self.sorted_row_indexes:
                        self.sorted_row_indexes.append(item[1])
                    else:
                        while item[1] in self.sorted_row_indexes:
                            item[1] += 1
                        self.sorted_row_indexes.append(item[1])


    @classmethod
    def create_from_dict(cls, dict_of_content: dict) -> any:
        '''
        Creates a table from the data in the dict
        '''
        if not isinstance(dict_of_content, dict):
            raise TypeError('Excpected dict_of_content to be a dict, got '+type(dict_of_content).__name__)
        if list(dict_of_content.keys()).sort() != ['title', 'header_row', 'first_column', 'values'].sort():
            raise KeyError('Excpected dict_of_contents to have the keys: title, header_row, first_column, values')
        if not isinstance(dict_of_content['title'], str):
            raise TypeError('Excpected key "title" to be a str, got '+type(dict_of_content['title']).__name__)
        if not isinstance(dict_of_content['header_row'], list) and not isinstance(dict_of_content['header_row'], tuple):
            raise TypeError('Excpected key "header_row" to be a list, got '+type(dict_of_content['header_row']).__name__)
        if not isinstance(dict_of_content['first_column'], list) and not isinstance(dict_of_content['first_column'], tuple):
            raise TypeError('Excpected key "first_column" to be a list, got '+type(dict_of_content['first_column']).__name__)
        if not isinstance(dict_of_content['values'], dict):
            raise TypeError('Excpected key "title" to be a dict, got '+type(dict_of_content['values']).__name__)

        table = Table()
        table.set_title(dict_of_content['title'])

        values = TableValues(header_row=dict_of_content['header_row'],
                             first_column=dict_of_content['first_column'])
        values.values = dict_of_content['values']

        table.set_values(values)

        return table


    @classmethod
    def create_from_list(cls, list_of_content: list) -> any:
        '''
        Creates a table from the data in the list
        '''
        if not isinstance(list_of_content, list):
            raise TypeError('Excpected list_of_content to be a list, got '+type(list_of_content).__name__)
        if not isinstance(list_of_content[0], str):
            raise TypeError('Excpected index 0 of list_of_content to be a str, got '+type(list_of_content[0]).__name__)
        for item in list_of_content[1:]:
            if not isinstance(item, list) and not isinstance(item, tuple):
                raise TypeError('Excpected index 1 and higher of list_of_content to be lists, got '+type(item).__name__)
        
        table = Table()
        table.set_title(list_of_content[0])

        header_row = []
        for item in list_of_content[1][1:]:
            header_row.append([item, len(item), table.values.header_row_align])

        first_column = []
        values = {}
        for row_index in range(2, len(list_of_content)):
            first_column.append([list_of_content[row_index][0], len(list_of_content[row_index][0]), table.values.first_column_align])

            for column_index in range(1, len(list_of_content[row_index])):
                text = list_of_content[row_index][column_index]
                values[(row_index-2, column_index-1)] = [text, len(text), table.values.align]

        tablevalues = TableValues(header_row=header_row,
                             first_column=first_column)
        tablevalues.values = values

        table.set_values(tablevalues)

        return Table


    @classmethod
    def create_from_tuple(cls, tuple_of_content: tuple) -> any:
        '''
        Creates a table from the data in the tuple
        '''
        if not isinstance(tuple_of_content, tuple):
            raise TypeError('Excpected tuple_of_content to be a tuple, got '+type(tuple_of_content).__name__)
        if not isinstance(tuple_of_content[0], str):
            raise TypeError('Excpected index 0 of tuple_of_content to be a str, got '+type(tuple_of_content[0]).__name__)
        for item in tuple_of_content[1:]:
            if not isinstance(item, list) and not isinstance(item, tuple):
                raise TypeError('Excpected index 1 and higher of tuple_of_content to be lists, got '+type(item).__name__)
            
        table = Table()
        table.set_title(tuple_of_content[0])

        header_row = []
        for item in tuple_of_content[1][1:]:
            header_row.append([item, len(item), table.values.header_row_align])

        first_column = []
        values = {}
        for row_index in range(2, len(tuple_of_content)):
            first_column.append([tuple_of_content[row_index][0], len(tuple_of_content[row_index][0]), table.values.first_column_align])

            for column_index in range(1, len(tuple_of_content[row_index])):
                text = tuple_of_content[row_index][column_index]
                values[(row_index-2, column_index-1)] = [text, len(text), table.values.align]

        tablevalues = TableValues(header_row=header_row,
                             first_column=first_column)
        tablevalues.values = values

        table.set_values(tablevalues)

        return table

    
    def convert_to_markdown(self, filename: str = 'Table') -> None:
        '''
        Saves the table as markdown table in `filename`.md
        '''
        if not isinstance(filename, str):
            raise TypeError('Excpected filename to be a str, got '+type(filename).__name__)
        if len(filename) == 0:
            raise ValueError('Excpected filename to have a length of 1 or higher, not 0')

        md_header = [' ']
        for item in self.values.header_row:
            md_header.append(item[0])

        md_rows = []
        for row in range(self.rows):
            md_row = []
            md_row.append(self.values.first_column[row][0])
            
            for col in range(self.columns):
                md_row.append(self.values.values[(row, col)][0])
            
            md_rows.append(md_row)

        if not pathlib.Path(f'{filename}.md').exists():
            num = ''

        else:
            num = 1
            while pathlib.Path(f'{filename}{num}.md').exists():
                num += 1

        with open(f'{filename}{num}.md', 'w', encoding='utf-8') as file:
            file.write('|' + '|'.join(md_header) + '|\n')
            file.write('|---' * len(md_header) + '|\n')
            for row in md_rows:
                file.write('|' + '|'.join(row) + '|\n')


    def convert_to_html(self, filename: str = 'Table') -> None:
        '''
        Saves the table as markdown table in `filename`.html
        '''
        if not isinstance(filename, str):
            raise TypeError('Excpected filename to be a str, got '+type(filename).__name__)
        if len(filename) == 0:
            raise ValueError('Excpected filename to have a length of 1 or higher, not 0')
        
        html_header = [[' ', 'right']]
        for item in self.values.header_row:
            html_header.append([item[0], item[2]])

        html_rows = []
        for row in range(self.rows):
            html_row = []
            html_row.append([self.values.first_column[row][0], self.values.first_column[row][2]])
            
            for col in range(self.columns):
                html_row.append([self.values.values[(row, col)][0], self.values.values[(row, col)][2]])
            
            html_rows.append(html_row)

        if not pathlib.Path(f'{filename}.html').exists():
            num = ''

        else:
            num = 1
            while pathlib.Path(f'{filename}{num}.html').exists():
                num += 1

        with open(f'{filename}{num}.html', 'w', encoding='utf-8') as file:
            file.write('<table>\n')
            file.write('  <tr>\n')
            for item in html_header:
                file.write(f'    <td style="text-align: {item[1]}">{item[0]}</td>\n')
            file.write('  </tr>\n')
            for row in html_rows:
                file.write('  <tr>\n')
                for item in row:
                    file.write(f'    <td style="text-align: {item[1]}">{item[0]}</td>\n')
                file.write('  </tr>\n')
            file.write('</table>\n')


    def save_in_file(self, filename: str = 'Table') -> None:
        '''
        Saves the table in the file .`filename`.table
        '''
        if not isinstance(filename, str):
            raise TypeError('Excpected filename to be a str, got '+type(filename).__name__)
        if len(filename) == 0:
            raise ValueError('Excpected filename to have a length of 1 or higher, not 0')

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
        if not isinstance(filename, str):
            raise TypeError('Excpected filename to be a str, got '+type(filename).__name__)
        if len(filename) == 0:
            raise ValueError('Excpected filename to have a length of 1 or higher, not 0')
        
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
        for hidden_row in self.hidden_rows:
            while self.hidden_rows.count(hidden_row) > 1:
                self.hidden_rows.remove(hidden_row)

        for hidden_column in self.hidden_columns:
            while self.hidden_columns.count(hidden_column) > 1:
                self.hidden_columns.remove(hidden_column)

        table = ''

        longest_row_length = self.get_longest_cell_length()

        if not self.hide_title:
            title_length = longest_row_length * (self.rows+1) + self.rows+2
            title = self.title
            title = title.center(title_length)
            
            table += FormatedText.BOLD + title.title() + FormatedText.BOLD + '\n\n'

        if TableStyle.WITHOUT_BORDER not in self.style:
            if TableStyle.WITHOUT_FIRST_COLUMN not in self.style:
                if TableStyle.ONLY_BORDER in self.style:
                    table += self.borderstyle[2] + (self.borderstyle[0] * longest_row_length + self.borderstyle[0]) * (self.columns-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + self.borderstyle[4] + '\n'
                else:
                    table += self.borderstyle[2] + (self.borderstyle[0] * longest_row_length + self.borderstyle[3]) * (self.columns-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + self.borderstyle[4] + '\n'
            else:
                if TableStyle.ONLY_BORDER in self.style:
                    table += self.borderstyle[2] + (self.borderstyle[0] * longest_row_length + self.borderstyle[0]) * (self.columns-1-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + self.borderstyle[4] + '\n'
                else:
                    table += self.borderstyle[2] + (self.borderstyle[0] * longest_row_length + self.borderstyle[3]) * (self.columns-1-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + self.borderstyle[4] + '\n'
        
        if TableStyle.WITHOUT_HEADER_ROW not in self.style:
            if TableStyle.WITHOUT_FIRST_COLUMN not in self.style:
                if TableStyle.WITHOUT_BORDER not in self.style:
                    table += self.borderstyle[1] + ' ' * longest_row_length
                else:
                    table += ' ' * longest_row_length

            for item_index in self.sorted_column_indexes:
                if item_index in self.hidden_columns:
                    continue
                text = TextAlign.set_text_align(self.values.header_row[item_index][0], longest_row_length, self.values.header_row[item_index][2])
                if TableStyle.ONLY_BORDER not in self.style:
                    table += self.borderstyle[1] + FormatedText.BOLD + text + FormatedText.END
                else:
                    table += ' ' + FormatedText.BOLD + text + FormatedText.END

            if TableStyle.WITHOUT_BORDER not in self.style:
                table += self.borderstyle[1] + '\n'
            else:
                table += '\n'

        print_rows = []
        for index in self.sorted_row_indexes:
            print_rows.append(0)
            print_rows.append(index*2+1)
        print_rows.append(self.rows*2)

        for index, print_row in enumerate(print_rows):
            if print_row == self.rows*2:    # lowest border piece/ outer border (and sum row)
                
                if self.sum_row:
                    if TableStyle.WITHOUT_HEADER_ROW in self.style:
                        if print_row != 0:
                            if TableStyle.ONLY_BORDER in self.style:
                                table += self.borderstyle[1] + (' ' * (longest_row_length + 1)) * (self.columns-len(self.hidden_columns)) + ' ' * longest_row_length + self.borderstyle[1] + '\n'
                            elif TableStyle.WITHOUT_FIRST_COLUMN not in self.style:
                                table += (self.borderstyle[5] if TableStyle.WITHOUT_BORDER not in self.style else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'
                            else:
                                table += (self.borderstyle[5] if TableStyle.WITHOUT_BORDER not in self.style else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns-1-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'
                    else:
                        if TableStyle.WITHOUT_FIRST_COLUMN not in self.style:
                            if TableStyle.ONLY_BORDER in self.style:
                                table += (self.borderstyle[1] if TableStyle.WITHOUT_BORDER not in self.style else '') + (' ' * (longest_row_length + 1)) * (self.columns-len(self.hidden_columns)) + ' ' * longest_row_length + (self.borderstyle[1] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'
                            else:
                                table += (self.borderstyle[5] if TableStyle.WITHOUT_BORDER not in self.style else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'
                        else:
                            if TableStyle.ONLY_BORDER in self.style:
                                table += (self.borderstyle[1] if TableStyle.WITHOUT_BORDER not in self.style else '') + (' ' * (longest_row_length + 1)) * (self.columns-1-len(self.hidden_columns)) + ' ' * longest_row_length + (self.borderstyle[1] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'
                            else:
                                table += (self.borderstyle[5] if TableStyle.WITHOUT_BORDER not in self.style else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns-1-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'


                    if TableStyle.WITHOUT_FIRST_COLUMN not in self.style and print_row//2 not in self.hidden_rows:
                        if TableStyle.WITHOUT_BORDER not in self.style:
                            table += self.borderstyle[1] + FormatedText.BOLD + 'SUM'.center(longest_row_length) + FormatedText.END
                        else:
                            table += FormatedText.BOLD + 'SUM'.center(longest_row_length) + FormatedText.END
                        

                    for x in self.sorted_column_indexes:
                        if x in self.sum_row_columns:
                            if TableStyle.ONLY_BORDER not in self.style:
                                table += self.borderstyle[1] + str(self.values.sum_column(x)).center(longest_row_length)
                            else:
                                table += ' ' + str(self.values.sum_column(x)).center(longest_row_length)
                        else:
                            if TableStyle.ONLY_BORDER not in self.style:
                                table += self.borderstyle[1] + ' '.center(longest_row_length)
                            else:
                                table += ' '.center(longest_row_length)

                    if print_row//2 in self.hidden_rows:
                        pass
                    elif TableStyle.WITHOUT_BORDER not in self.style:
                        table += self.borderstyle[1] + '\n'
                    else:
                        table += '\n'


                if TableStyle.WITHOUT_BORDER not in self.style:
                    if TableStyle.WITHOUT_FIRST_COLUMN not in self.style:
                        if TableStyle.ONLY_BORDER in self.style:
                            table += self.borderstyle[8] + (self.borderstyle[0] * longest_row_length + self.borderstyle[0]) * (self.columns-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + self.borderstyle[10] + '\n'
                        else:
                            table += self.borderstyle[8] + (self.borderstyle[0] * longest_row_length + self.borderstyle[9]) * (self.columns-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + self.borderstyle[10] + '\n'
                    else:
                        if TableStyle.ONLY_BORDER in self.style:
                            table += self.borderstyle[8] + (self.borderstyle[0] * longest_row_length + self.borderstyle[0]) * (self.columns-1-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + self.borderstyle[10] + '\n'
                        else:
                            table += self.borderstyle[8] + (self.borderstyle[0] * longest_row_length + self.borderstyle[9]) * (self.columns-1-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + self.borderstyle[10] + '\n'
            
            elif print_row % 2 == 0:        # border between cells
                if int(print_row / 2) in self.hidden_rows:
                    continue
                
                if TableStyle.WITHOUT_HEADER_ROW in self.style and index == 0:
                    continue

                elif TableStyle.WITHOUT_FIRST_COLUMN not in self.style:
                    if TableStyle.ONLY_BORDER in self.style:
                        table += (self.borderstyle[1] if TableStyle.WITHOUT_BORDER not in self.style else '') + (' ' * (longest_row_length + 1)) * (self.columns-len(self.hidden_columns)) + ' ' * longest_row_length + (self.borderstyle[1] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'
                    else:
                        table += (self.borderstyle[5] if TableStyle.WITHOUT_BORDER not in self.style else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'
                else:
                    if TableStyle.ONLY_BORDER in self.style:
                        table += (self.borderstyle[1] if TableStyle.WITHOUT_BORDER not in self.style else '') + (' ' * (longest_row_length + 1)) * (self.columns-1-len(self.hidden_columns)) + ' ' * longest_row_length + (self.borderstyle[1] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'
                    else:
                        table += (self.borderstyle[5] if TableStyle.WITHOUT_BORDER not in self.style else '') + (self.borderstyle[0] * longest_row_length + self.borderstyle[6]) * (self.columns-1-len(self.hidden_columns)) + self.borderstyle[0] * longest_row_length + (self.borderstyle[7] if TableStyle.WITHOUT_BORDER not in self.style else '') + '\n'
            
            else:                           # cell texts
                if TableStyle.WITHOUT_FIRST_COLUMN not in self.style and print_row//2 not in self.hidden_rows:
                    item = self.values.first_column[print_row//2]
                    text = TextAlign.set_text_align(item[0], longest_row_length, item[2])
                    if TableStyle.WITHOUT_BORDER not in self.style:
                        table += self.borderstyle[1] + FormatedText.BOLD + text + FormatedText.END
                    else:
                        table += FormatedText.BOLD + text + FormatedText.END
                    

                for x in self.sorted_column_indexes:
                    if print_row//2 not in self.hidden_rows and x not in self.hidden_columns:
                        text = self.values.get_text_from_cell(print_row//2, x)
                        text = TextAlign.set_text_align(text, longest_row_length, self.values.get_align_from_cell(print_row//2, x))
                        if TableStyle.WITHOUT_BORDER in self.style and not (x == 0 and TableStyle.WITHOUT_FIRST_COLUMN in self.style):
                            table += self.borderstyle[1] + text
                        elif TableStyle.WITHOUT_BORDER in self.style:
                            table += text
                        elif TableStyle.ONLY_BORDER in self.style:
                            table += ' ' + text
                        else:
                            table += self.borderstyle[1] + text

                if print_row//2 in self.hidden_rows:
                    pass
                elif TableStyle.WITHOUT_BORDER not in self.style:
                    table += self.borderstyle[1] + '\n'
                else:
                    table += '\n'

        return table + FormatedText.END
    

    def copy(self) -> any:
        '''
        Creates a copy of the table and returns it
        '''
        new_table = Table(title=self.title, columns=self.columns, rows=self.rows,
                          values=copy.deepcopy(self.values), style=self.style,
                          borderstyle=self.borderstyle, default_cell_length=self.default_cell_length,
                          hide_title=self.hide_title)
        new_table.hidden_rows = copy.deepcopy(self.hidden_rows)
        new_table.hidden_columns = copy.deepcopy(self.hidden_columns)
        new_table.sum_row = self.sum_row
        new_table.sum_row_columns = copy.deepcopy(self.sum_row_columns)

        return new_table


    def append_table(self, table_to_add: any) -> any:
        '''
        Appends the table to this table and returns the new table.
        '''
        if not isinstance(table_to_add, Table):
            raise TypeError('Excpected table_to_add to be an Table, got '+type(table_to_add).__name__)
        
        table: Table = self.copy()

        if table_to_add.get_values().first_column == self.get_values().first_column:
            for col in range(len(table_to_add.get_values().header_row)):
                head = table_to_add.get_values().header_row[col][0]
                rows = []
                for row in range(len(table_to_add.get_values().first_column)):
                    rows.append(table_to_add.get_values().get_text_from_cell(row, col))
                
                values = table.get_values()
                values.add_column(head, rows)
                table.set_values(values)
        else:
            raise ValueError('To append the table, the tables must have the same first column. Do you mean ".append_table_to_bottom()"?')

        return table


    def append_table_to_bottom(self, table_to_add: any) -> any:
        '''
        Appends the table to this table and returns the new table.
        '''
        if not isinstance(table_to_add, Table):
            raise TypeError('Excpected table_to_add to be an Table, got '+type(table_to_add).__name__)
        
        table: Table = self.copy()

        if table_to_add.get_values().header_row == self.get_values().header_row:
            for row in range(len(table_to_add.get_values().first_column)):
                first = table_to_add.get_values().first_column[row][0]
                rows = []
                for col in range(len(table_to_add.get_values().header_row)):
                    rows.append(table_to_add.get_values().get_text_from_cell(row, col))
                
                values = table.get_values()
                values.add_row(first, rows)
                table.set_values(values)
        else:
            raise ValueError('To append the table to the bottom, the tables must have the same header row. Do you mean ".append_table()"?')

        return table


    def __add__(self, other: any) -> any:
        '''
        Adds the second table to the first.
        '''
        if not isinstance(other, Table):
            raise TypeError('Excpected other to be an Table, got '+type(other).__name__)
        
        append = False
        append_to_bottom = False

        if other.get_values().first_column == self.get_values().first_column:
            append = True
        if other.get_values().header_row == self.get_values().header_row:
            append_to_bottom = True

        if append and append_to_bottom:
            raise ValueError('Both tables have the same header row and the same first column. Use ".append_table()" or ".append_table_to_bottom()" instead.')
        elif append == append_to_bottom:
            raise ValueError('The tables don\'t have the same header row or the same first column.')
        
        if append:
            return self.append_table(other)
        elif append_to_bottom:
            return self.append_table_to_bottom(other)
            
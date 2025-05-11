from widgets.text import *

class TableValues:
    def __init__(self, header_row: list = [], first_column: list = []):
        self.header_row: list[list[str, int]] = header_row
        self.first_column: list[list[str, int]] = first_column
        self.values: dict[tuple[int, int], list[str, int]] = {}


    def set_header_row(self, header_row: list) -> None:
        '''
        Sets the header row of your TableValues
        '''
        for i in range(len(header_row)):
            header_row[i] = [header_row[i], len(header_row[i])]
        self.header_row = header_row


    def set_first_column(self, first_column: list) -> None:
        '''
        Sets the first column of your TableValues
        '''
        for i in range(len(first_column)):
            first_column[i] = [first_column[i], len(first_column[i])]
        self.first_column = first_column

    
    def set_text_at_cell(self, row: int, column: int, text: str) -> None:
        '''
        Changes the text of the cell at the position
        '''
        self.values[(row, column)] = [text, len(text)]


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

class Table:
    '''
    Creates a new Table object.

    Parameters:
        - `title`  str, the title of your table
        - `columns`  int, the amount of columns of your table
        - `rows`  int, the amount of rows of your table
    '''


    def __init__(self, title: str = '', columns: int = 0, rows: int = 0, *, values: TableValues = TableValues()) -> None:
        self.title: str = title
        self.columns: int = columns
        self.rows: int = rows
        self.values: TableValues = values


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


    def get_longest_row_length(self) -> int:
        '''
        Returns the length of the longest text in any cell
        '''
        longest_row_length = 5
        for col_index in range(self.columns):
            for row_index in range(self.rows):
                row_length = self.values.get_textlength_from_cell(row_index, col_index)
                if row_length > longest_row_length:
                    longest_row_length = row_length
        for item in self.values.header_row + self.values.first_column:
            if item[1] > longest_row_length:
                longest_row_length = item[1]
        return longest_row_length


    def print_without_header_and_first_column(self) -> None:
        '''
        Prints your Table without a header row and a first column
        '''
        
        longest_row_length = self.get_longest_row_length()

        for print_row in range(self.rows*2+1):
            if print_row == 0:
                print('┌' + ('─' * longest_row_length + '┬') * (self.columns-1) + '─' * longest_row_length + '┐')
            elif print_row == self.rows*2:
                print('└' + ('─' * longest_row_length + '┴') * (self.columns-1) + '─' * longest_row_length + '┘')
            elif print_row % 2 == 0:
                print('├' + ('─' * longest_row_length + '┼') * (self.columns-1) + '─' * longest_row_length + '┤')
            else:
                for x in range(self.columns):
                    text = self.values.get_text_from_cell(print_row//2, x)
                    text_length = self.values.get_textlength_from_cell(print_row//2, x)
                    while text_length < longest_row_length:
                        text = ' ' + text
                        text_length += 1
                    print(f'│{text}', end='')
                print('│')
    

    def print(self) -> None:
        '''
        Prints your Table
        '''
        
        longest_row_length = self.get_longest_row_length()


        title_length = longest_row_length * (self.rows+1) + self.rows+2
        title = self.title
        while len(title) < title_length:
            title = ' ' + title + ' '
        
        print(FormatedText.BOLD + title.title() + FormatedText.BOLD, end='\n\n')

        print('┌' + ('─' * longest_row_length + '┬') * (self.columns) + '─' * longest_row_length + '┐')
        print(f'│' + ' ' * longest_row_length, end='')
        for item in self.values.header_row:
            text = item[0]
            text_length = item[1]
            while text_length < longest_row_length:
                text = ' ' + text
                text_length += 1
            print(f'│{FormatedText.BOLD + text + FormatedText.END}', end='')
        print('│')

        for print_row in range(self.rows*2+1):
            if print_row == self.rows*2:
                print('└' + ('─' * longest_row_length + '┴') * (self.columns) + '─' * longest_row_length + '┘')
            elif print_row % 2 == 0:
                print('├' + ('─' * longest_row_length + '┼') * (self.columns) + '─' * longest_row_length + '┤')
            else:
                item = self.values.first_column[print_row//2]
                text = item[0]
                text_length = item[1]
                while text_length < longest_row_length:
                    text = ' ' + text
                    text_length += 1
                print(f'│{FormatedText.BOLD + text + FormatedText.END}', end='')
                for x in range(self.columns):
                    text = self.values.get_text_from_cell(print_row//2, x)
                    text_length = self.values.get_textlength_from_cell(print_row//2, x)
                    while text_length < longest_row_length:
                        text = ' ' + text
                        text_length += 1
                    print(f'│{text}', end='')
                print('│')
# How to use PyGraph

## Table()-class
You can use the `Table()`-class to create tables in different designs and with a lot of features. They make it easier to add some cool stuff to your table.

The `Table()`-class has 8 optional arguments: 
`title: str = '', columns: int = 0, rows: int = 0, *, values: TableValues = TableValues(), style: TableStyle = TableStyle.DEFAULT, borderstyle: BorderStyle = BorderStyle.LIGHT, default_cell_length: int = 6, hide_title: bool = False`

`title: str` - The title of your table, it's printed in bold above your table.

`columns: int` - The number of columns your table has. Some other functions set `columns` by itself.

`rows: int` - The number of rows your table has. Some other functions set `rows` by itself.

`values: TableValues` - The values of the table as `TableValues()`-object.

`style: TableStyle` - The style of your table as `str` or easier `TableStyle.YOURSTYLE`, e.g. `TableStyle.DEFAULT`.

`borderstyle: BorderStyle` - The style of the border as `str` or easier `BorderStyle.YOURSTYLE`, e.g. `BorderStyle.ASCII` or `BorderStyle.LIGHT_ARC`.

`default_cell_length: int` - The length of the cell if no celltext is longer as `default_cell_length`.

`hide_title: bool` - Hides the title.


### .convert_to_html(filename: str = 'Table') -> None
Converts your table to html source code in saves it in `filename`.html. If the file already exists the programm adds a number to the end. By default the filename "Table" is chosen.

Only the text and text-align get converted. Styles and other things are ignored.


### .convert_to_markdown(filename: str = 'Table') -> None
Converts your table into an markdown table and saves it in `filename`.md. You can copy the table from this file to your markdown file if you want. By default the filename "Table" is chosen.

Only the text get converted. Styles and other things are ignored.

### .copy() -> Table
Creates a copy of the `Table()`-object and everything saved in the `Table()`-object.


### create_from_dict(dict_of_content: dict) -> None
Takes a python dictionary and turns it into a `TableValues()`-object and set the table values to this `TableValues()`-object.

The dictionary must have this format:

```python
{
    'header_row': [['5', len('5'), TextAlign.CENTER],['10', len('10'), TextAlign.CENTER]],
    'first_column': [['2', len('2'), TextAlign.CENTER], ['4', len('4'), TextAlign.CENTER]],
    'values': {
        (0,0): ['10', len('10'), TextAlign.RIGHT],
        (0,1): ['20', len('20'), TextAlign.RIGHT],
        (1,0): ['20', len('20'), TextAlign.RIGHT],
        (1,1): ['40', len('40'), TextAlign.RIGHT],
    },
}
```

You can get a dictionary like this with the function `.get_dict()`

`header_row` and `first_column` are lists of lists with the items: `text: str`, `textlength: int`, `align: TextAlign`

`values` is a dictionary with the position of the cell as tuple with `x: int` and `y: int` as key and a value like the lists in `header_row` and `first_column`.


### .create_from_list(list_of_content) -> None
Creates a new `TableValues()`-object and sets the table values to this object.

The list must have this format:
```python
[
    'title',
    [' ', '5', '10'],
    ['2', '10', '20'],
    ['4', '20', '40'],
]
```

You can get a list like this from `.get_list()`.

The item at index 0 of the list is the `title` of the table.

The first list (index 1) is the header row. The first value in this list is ignored.

All other lists (index 2 - index n) are structured like this: `['first_column_text', 'cell_1', ..., 'cell_n']`.

### .create_from_tuple(tuple_of_content) -> None
Creates a new `TableValues()`-object and sets the table values to this object.

The tuple must have this format:
```python
(
    'title',
    (' ', '5', '10'),
    ('2', '10', '20'),
    ('4', '20', '40'),
)
```

You can get a tuple like this from `.get_tuple()`.

The item at index 0 of the tuple is the `title` of the table.

The first tuple (index 1) is the header row. The first value in this tuple is ignored.

All other tuples (index 2 - index n) are structured like this: `('first_column_text', 'cell_1', ..., 'cell_n')`.

### .get_dict() -> dict
Returns the table values as dictionary, with the format like in `.create_from_dict()`:
```python
{
    'header_row': [['5', len('5'), TextAlign.CENTER],['10', len('10'), TextAlign.CENTER]],
    'first_column': [['2', len('2'), TextAlign.CENTER], ['4', len('4'), TextAlign.CENTER]],
    'values': {
        (0,0): ['10', len('10'), TextAlign.RIGHT],
        (0,1): ['20', len('20'), TextAlign.RIGHT],
        (1,0): ['20', len('20'), TextAlign.RIGHT],
        (1,1): ['40', len('40'), TextAlign.RIGHT],
    },
}
```

You can use this list to create new TableValues with `.create_from_dict()` or use it for yourself.

### .get_hidden_columns() -> list
Returns a list of all indexes of columns that are marked as hidden.
You can mark or unmark columns as hidden with the functions `.hide_column()` and `.show_column()` 

### .get_hidden_rows() -> list
Returns a list of all indexes of rows that are marked as hidden.
You can mark or unmark rows as hidden with the functions `.hide_row()` and `.show_row()` 

### .get_list() -> list
Returns the table values as list, with the format like in `.create_from_list()`:
```python
[
    'title',
    [' ', '5', '10'],
    ['2', '10', '20'],
    ['4', '20', '40'],
]
```

You can use this list to create new TableValues with `.create_from_list()` or use it for yourself.

### .get_longest_cell_length() -> int
Returns the length of the longest cell in the table as integer.

### .get_str() -> str
Returns the table as string. This string is the same as the `.print()`-function prints into the terminal.

The string could look like this:
```
   Your Cool Table    

┌──────┬──────┬──────┐
│      │     5│    10│
├──────┼──────┼──────┤
│     2│    10│    20│
├──────┼──────┼──────┤
│     4│    20│    40│
└──────┴──────┴──────┘

```

The title you can change with `.set_title()`.

You can change the text align with `.get_values().set_align()`, `.get_values().set_header_row_align()` and `.get_values().set_first_column_align()`.

The border style you can change with `.set_border_style()` and a border style from `BorderStyle()`.

The general style of the table you can change with `.set_style()` and a table style from `TableStyle()`.


### .get_tuple() -> tuple
Returns the table values as tuple, with the format like in `.create_from_tuple()`:
```python
(
    'title',
    (' ', '5', '10'),
    ('2', '10', '20'),
    ('4', '20', '40'),
)
```

You can use this tuple to create new TableValues with `.create_from_tuple()` or use it for yourself.

### .get_values() -> TableValues
Returns the values as `TableValues()`-object. You can set the values with `.set_values()`.

### .help() -> None
The `.help()`-function runs the python command `help(Table)` and shows the output in your terminal. In Linux you can leave this with ctrl-Z.

```
Help on class Table in module widgets.table:

class Table(builtins.object)
 |  Table(title: str = '', columns: int = 0, rows: int = 0, *, values: widgets.table.TableValues = <widgets.table.TableValues object at 0x798b32edc3e0>, style: widgets.table.TableStyle = 'default', borderstyle: widgets.table.BorderStyle = ('─', '│', '┌', '┬', '┐', '├', '┼', '┤', '└', '┴', '┘'), default_cell_length: int = 6, hide_title: bool = False) -> None
 |
 |  Creates a new Table object.
 |
 |  Methods defined here:
 |
 |  __init__(self, title: str = '', columns: int = 0, rows: int = 0, *, values: widgets.table.TableValues = <widgets.table.TableValues object at 0x798b32edc3e0>, style: widgets.table.TableStyle = 'default', borderstyle: widgets.table.BorderStyle = ('─', '│', '┌', '┬', '┐', '├', '┼', '┤', '└', '┴', '┘'), default_cell_length: int = 6, hide_title: bool = False) -> None
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __str__(self) -> str
 |      Return str(self).
 |
 |  convert_to_html(self, filename: str = 'Table') -> None
 |      Saves the table as markdown table in `filename`.html
 |
 |  convert_to_markdown(self, filename: str = 'Table') -> None
 |      Saves the table as markdown table in `filename`.md

...
```


### .hide_column(column_index: int) -> None
Marks the column at the index `column_index` as hidden. You can see which columns are marked as hidden with the function `.get_hidden_columns()`. Hidden columns aren't visible if you print the table with `.print()`, use `.get_str()` to get the table as string or if you write `str(my_table)`.

### .hide_columns(column_indexes: list) -> None
Marks the columns at the indexes in the list `column_indexes` as hidden. You can see which columns are marked as hidden with the function `.get_hidden_columns()`. Hidden columns aren't visible if you print the table with `.print()`, use `.get_str()` to get the table as string or if you write `str(my_table)`.

### .hide_row(row_index: int) -> None
Marks the row at the index `row_index` as hidden. You can see which rows are marked as hidden with the function `.get_hidden_rows()`. Hidden rows aren't visible if you print the table with `.print()`, use `.get_str()` to get the table as string or if you write `str(my_table)`.

### .hide_rows(row_indexes: list) -> None
Marks the rows at the indexes in the list `row_indexes` as hidden. You can see which rows are marked as hidden with the function `.get_hidden_rows()`. Hidden rows aren't visible if you print the table with `.print()`, use `.get_str()` to get the table as string or if you write `str(my_table)`.

### .hide_sum_row() -> None
Hides the sum row at the end of the table. The sum row is hidden by default. If you want to show this row, you can use `.show_sum_row()`.

### .is_column_hidden(column_index: int) -> bool
Returns `True` if the column with the index `column_index` is hidden. You can hide columns with `.hide_column()` and `.hide_columns()` and you can show hidden columns again with `.show_column()` and `.show_columns()`.


### .is_row_hidden(row_index: int) -> bool
Returns `True` if the row with the index `row_index` is hidden. You can hide rows with `.hide_row()` and `.hide_rows()` and you can show hidden rows again with `.show_row()` and `.show_rows()`.

### .is_sum_row_hidden() -> bool
Returns `True` if the sum row is hidden. You can hide the sum row with `.hide_sum_row()` and show it with `.show_sum_row()`. By default the sum row is hidden.

### .is_title_hidden() -> bool
Returns `True` if the title is hidden. By default the title isn't hidden. You can show the title again with `.show_title()`.

### .load_from_file(filename: str) -> None
Loads the table from the file ".`filename`.table". The title, the header row, first column and the values are loaded from this file. The text aligns are also loaded from the file. The program uses it's `.get_dict()`-functions to create a dictionary and saves the dictionary in this file.

### .print() -> None
Prints your table in the terminal, this could look like this:

```
   Your Cool Table    

┌──────┬──────┬──────┐
│      │     5│    10│
├──────┼──────┼──────┤
│     2│    10│    20│
├──────┼──────┼──────┤
│     4│    20│    40│
└──────┴──────┴──────┘

```

You can change a lot of things with the functions of the `Table()`- and the `TableValues()`-class. 

The style of the border you can change with the `BorderStyle()`-class and the `.set_border_style()`-function.

The general style of the table itself you can change with the `TableStyle()`-class and the `.set_style()`-function.

### .save_in_file(filename: str = 'Table') -> None
Saves the table in the file ".`filename`.table". `filename` is by default "Table". The title, the header row, first column and the values are saved in this file. The text aligns are also saved there. The program uses it's `.get_dict()`-functions to create and save the dictionary in this file.

### .set_border_style(borderstyle: BorderStyle) -> None
Sets the border style of the border of the table. The border styles are saved in the `BorderStyle()`-class. You can choose one of the existing styles like `BorderStyle.LIGHT_ARC`. But you can also create your own styles with `BorderStyle.create_style()` or `BorderStyle.create_style_from_tuple()`. If you want to see the border styles, go to the BorderStyle()-class explanation.

### .set_cell_color(row: int, column: int, color: ColoredText) -> None
Sets the color of the text at the cell to the color in `color`. `color` has as value a string saved in the `ColoredText()`-class, this means you can set color to e.g. `ColoredText.RED`.

### .set_columns(columns: int) -> None
Sets the number of columns your table has to the number in `columns`. In the most cases, you don't need to to set this value by hand.

### .set_default_cell_length(default_cell_length: int) -> None
Sets the default cell length to the value in `default_cell_length`. If one cell text length is higher than the value in `default_cell_length` the bigger one is taken. But if no cell text is longer then `default_cell_length` the value in `default_cell_length` is used. The default cell length is by default 6.

### .set_first_column_color(color: ColoredText) -> None
Sets the color of all texts in the first column to the color in `color`. `color` has as value a string saved in the `ColoredText()`-class, this means you can set color to e.g. `ColoredText.RED`.

### .set_header_row_color(color: ColoredText) -> None
Sets the color of all texts in the header row to the color in `color`. `color` has as value a string saved in the `ColoredText()`-class, this means you can set color to e.g. `ColoredText.RED`.

### .set_hide_title(hide_title: bool) -> None
Hides the title if `hide_title` is `True`, otherwise it shows the title.

### .set_rows(rows: int) -> None
Sets the number of rows your table has to the number in `rows`. In the most cases, you don't need to to set this value by hand.

### .set_style(style: TableStyle) -> None
Sets the general style of the table. You set the style with e.g `TableStyle.DEFAULT`. To see all table styles go to the TableStyle()-class explanation.

### .set_title(title: str) -> None
Sets the title of your table to the string in `title`. You can hide or show the title with `.set_hide_title(True)` and `.set_hide_title(False)`.

### .set_values(values: TableValues) -> None
Sets the values of the table to the `TableValues()`-object in `values`. This function sets the number of rows and the number of columns, so you don't have to do it by hand.

### .show_column(column_index: int) -> None
Unmarks the column at the index `column_index` as hidden. To hide a column use the function `.hide_column()` or to hide multiple columns `.hide_columns()`. To see which columns are hidden, use the `.get_hidden_columns()`-function.

### .show_columns(column_indexes: list) -> None
Unmarks the columns at the indexes in `column_indexes` as hidden. To hide a column use the function `.hide_column()` or to hide multiple columns `.hide_columns()`. To see which columns are hidden, use the `.get_hidden_columns()`-function.

### .show_row(row_index: int) -> None
Unmarks the row at the index `row_index` as hidden. To hide a row use the function `.hide_row()` or to hide multiple rows `.hide_rows()`. To see which rows are hidden, use the `.get_hidden_rows()`-function.

### .show_rows(row_indexes: list) -> None
Unmarks the rows at the indexes in `row_indexes` as hidden. To hide a row use the function `.hide_row()` or to hide multiple rows `.hide_rows()`. To see which rows are hidden, use the `.get_hidden_rows()`-function.

### .show_sum_row(row_indexes: list) -> None
Shows the sum row at the bottom of your table. In this row are the sums of all values of the rows in `row_indexes`. To hide the sum row use the `.hide_sum_row()`-function and to find out if the sum row is hidden use the `is_sum_row_hidden()`-function.

### .sort_by_column(column_index: int, reverse: bool = False) -> None
Sorts all columns by the values in the column at the index `column_index`. The column is sorted by ascii, this means that the letters from A-Z are smaller than the letters from a-z. You can reverse the sorting if you set `reverse` to `True`. `reverse` is by default `False`.

### .sort_by_row(row_index: int, reverse: bool = False) -> None
Sorts all rows by the values in the row at the index `row_index`. The row is sorted by ascii, this means that the letters from A-Z are smaller than the letters from a-z. You can reverse the sorting if you set `reverse` to `True`. `reverse` is by default `False`.

## TableValues()-class
The `TableValues()`-class contains the values of the table. You can set the values of the table to a `TableValues()`-object with `your_table.set_values(your_table_values)`.

The `TableValues()`-class takes two arguments. At first `header_row` as list of strings. In this list are all header row texts, but you can add more later. After that it takes `first_column` as list of strings. In this list are all first column texts, but you can add more later.


### .add_column(header_row_value: str = ' ', values: list = [' ']) -> None
Adds a column to the end of the table. The text in the cell of the header row is set to the value of `header_row_value`. The texts of the cells in this column are set to the values in `values` from top to bottom. By default `header_row_value` is set to " " and values is a list of " ", which is multiplied with the number of first column items.


### .add_row(first_column_value: str = ' ', values: list = [' ']) -> None
Adds a row to the end of the table. The text in the cell of the first column is set to the value of `first_column_value`. The texts of the cells in this row are set to the values in `values` from left to right. By default `first_column_value` is set to " " and values is a list of " ", which is multiplied with the number of header row items.


### .copy() -> TableValues
Creates a copy of the `TableValues()`-object and everything saved in the `TableValues()`-object.


### .count(text: str, *, search_in_first_column: str = False, search_in_header_row: str = False) -> int
Counts how often the text in `text` appears in the table. If `search_in_first_column` is `True` than it searches the text also in the first column. If `search_in_header_row` is `True` than it searches the text also in the header row. By default `search_in_first_column` and `search_in_header_row` are set to False.


### .delete_column(index: int) -> None
Deletes the column at the index `index`.


### .delete_row(index: int) -> None
Deletes the row at the index `index`.


### .get_align_from_cell(row: int, column: int) -> TextAlign
Returns the text align of the cell at the position (`row`, `column`).


### .get_cell_with_text(text: str) -> tuple
Returns a tuple with the position of the first cell with the text `text`. The tuple has the format (row, column).


### .get_text_from_cell(row: int, column: int) -> str
Returns the text from the cell at the position (`row`, `column`).


### .get_text_from_column(column: int) -> list


### .get_text_from_row(row: int) -> list


### .get_textlength_from_cell(row: int, column: int) -> int


### .help() -> None


### .insert_column(index: int = 0, header_row_value: str = ' ', values: list = [' ']) -> None


### .insert_row(index: int = 0, first_column_value: str = ' ', values: list = [' ']) -> None


### .is_numeric_column(column: int) -> bool


### .is_numeric_row(row: int) -> bool


### .set_align(align: TextAlign) -> None


### .set_align_at_cell(row: int, column: int, align: TextAlign) -> None


### .set_first_column(first_column: list) -> None


### .set_first_column_align(align: TextAlign) -> None


### .set_first_column_align_at_position(pos: int, align: TextAlign) -> None


### .set_header_row(header_row: list) -> None


### .set_header_row_align(align: TextAlign) -> None


### .set_header_row_align_at_position(pos: int, align: TextAlign) -> None


### .set_text_at_cell(row: int, column: int, text: str) -> None


### .sum_column(column: int) -> float


### .sum_row(row: int) -> float


### .swap_columns(index1: int, index2: int) -> None


### .swap_rows(index1: int, index2: int) -> None


## BorderStyle()-class

### .create_style(self, name: str, vertical_line: str, horizontal_line: str, upper_left_corner: str, upper_T_corner: str, upper_right_corner: str, left_T_corner: str, X_cross: str, right_T_corner: str, lower_left_corner: str, lower_T_corner: str, lower_right_corner: str) -> None


### .create_style_from_tuple(self, name: str, style: tuple) -> None


## TableStyle()-class


## BarChart()-class


## Axis()-class


## Position()-class


## Direction()-class


# Examples
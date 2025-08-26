# How to use PyGraph

# Create Tables with PyGraph

## Table()-class
You can use the `Table()`-class to create tables in different designs and with a lot of features. They make it easier to add some cool stuff to your table.

The `Table()`-class has 8 optional arguments: 
`title: str = '', columns: int = 0, rows: int = 0, *, values: TableValues = TableValues(), style: list[str] = [TableStyle.DEFAULT], borderstyle: str = BorderStyle.LIGHT, default_cell_length: int = 6, hide_title: bool = False`

`title: str` - The title of your table, it's printed in bold above your table.

`columns: int` - The number of columns your table has. Some other functions set `columns` by itself.

`rows: int` - The number of rows your table has. Some other functions set `rows` by itself.

`values: TableValues` - The values of the table as `TableValues()`-object.

`style: TableStyle` - The style of your table as `str` or easier `TableStyle.YOURSTYLE`, e.g. `TableStyle.DEFAULT`.

`borderstyle: str` - The style of the border as `str` or easier `BorderStyle.YOURSTYLE`, e.g. `BorderStyle.ASCII` or `BorderStyle.LIGHT_ARC`.

`default_cell_length: int` - The length of the cell if no celltext is longer as `default_cell_length`.

`hide_title: bool` - Hides the title.

### .append_table(table_to_add: Table) -> Table
Adds the table in `table_to_add` to the right of this table.

This function returns the fused table.


### .append_table_to_bottom(table_to_add: Table) -> Table
Adds the table in `table_to_add` to the bottom of this table.

This function returns the fused table.


### .convert_to_html(filename: str = 'Table') -> None
Converts your table to html source code in saves it in `filename`.html. If the file already exists the programm adds a number to the end. By default the filename "Table" is chosen.

Only the text and text-align get converted. Styles and other things are ignored.


### .convert_to_markdown(filename: str = 'Table') -> None
Converts your table into an markdown table and saves it in `filename`.md. You can copy the table from this file to your markdown file if you want. By default the filename "Table" is chosen.

Only the text get converted. Styles and other things are ignored.

### .copy() -> Table
Creates a copy of the `Table()`-object and everything saved in the `Table()`-object.


### .create_from_dict(dict_of_content: dict) -> Table
Takes a python dictionary and turns it into a `Table()`-object and returns it.

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


### .create_from_list(list_of_content) -> Table
Creates a new `Table()`-object and returns it.

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

### .create_from_tuple(tuple_of_content) -> Table
Creates a new `Table()`-object and returns it.

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


### .get_title() -> str
Returns the title of this table.


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

### .set_border_style(borderstyle: str) -> None
Sets the border style of the border of the table. The border styles are saved in the `BorderStyle()`-class. You can choose one of the existing styles like `BorderStyle.LIGHT_ARC`. But you can also create your own styles with `BorderStyle.create_style()` or `BorderStyle.create_style_from_tuple()`. If you want to see the border styles, go to the BorderStyle()-class explanation.

### .set_cell_color(row: int, column: int, color: str) -> None
Sets the color of the text at the cell to the color in `color`. `color` has as value a string saved in the `ColoredText()`-class, this means you can set color to e.g. `ColoredText.RED`.

### .set_columns(columns: int) -> None
Sets the number of columns your table has to the number in `columns`. In the most cases, you don't need to to set this value by hand.

### .set_default_cell_length(default_cell_length: int) -> None
Sets the default cell length to the value in `default_cell_length`. If one cell text length is higher than the value in `default_cell_length` the bigger one is taken. But if no cell text is longer then `default_cell_length` the value in `default_cell_length` is used. The default cell length is by default 6.

### .set_first_column_color(color: str) -> None
Sets the color of all texts in the first column to the color in `color`. `color` has as value a string saved in the `ColoredText()`-class, this means you can set color to e.g. `ColoredText.RED`.

### .set_header_row_color(color: str) -> None
Sets the color of all texts in the header row to the color in `color`. `color` has as value a string saved in the `ColoredText()`-class, this means you can set color to e.g. `ColoredText.RED`.

### .set_hide_title(hide_title: bool) -> None
Hides the title if `hide_title` is `True`, otherwise it shows the title.

### .set_rows(rows: int) -> None
Sets the number of rows your table has to the number in `rows`. In the most cases, you don't need to to set this value by hand.

### .set_style(style: str) -> None
Sets the general style of the table. You set the style with e.g `TableStyle.DEFAULT`. To see all table styles go to the TableStyle()-class explanation.

This function overwrites the styles set before.

### .set_styles(styles: list) -> None
Sets the general styles of the table to the styles in `styles`. You set the style with e.g `TableStyle.DEFAULT`. To see all table styles go to the TableStyle()-class explanation.

This function overwrites the styles set before.

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


### .\_\_add__(other: Table) -> Table
You can append a table to another table with the operator `+`.

If the first columns of the tables are the same, the table after the `+`-operator gets appended to the right side of the table before the `+`-operator.

If the header rows of the tables are the same, the table after the `+`-operator gets appended to the bottom of the table before the `+`-operator.

If the first columns are the same and the header rows are the same, an error gets raised. 
If the first columns aren't the same and the header rows aren't the same, an error gets raised. 


### .\_\_copy__() -> Table
You can create a copy of this table with `copy.copy(your_table)`


### .\_\_deepcopy__() -> Table
You can create a copy of this table with `copy.deepcopy(your_table)`


### .\_\_getitem__(key: int) -> list
You can use `your_table[0]` to get a list of the texts of the first row under the header row.

This means that you can use `your_table[3][5]` instead of `your_table.get_values().get_text_at_cell(3, 5)`


### .\_\_str__() -> str
You can use `str(your_table)` to convert your table to a str.

If you use `print(your_table)` the table gets printed to the terminal.


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


### .get_cell_with_text(text: str) -> tuple | None
Returns a tuple with the position of the first cell with the text `text`. The tuple has the format (row, column).


### .get_text_from_cell(row: int, column: int) -> str
Returns the text from the cell at the position (`row`, `column`).


### .get_text_from_column(column: int) -> list
Returns the text of the header row cell and the texts of the cells in this column. The list could look like this: `['header row text', ['cell 1', 'cell 2', 'cell 3']]`. 


### .get_text_from_row(row: int) -> list
Returns the text of the first column cell and the texts of the cells in this row. The list could look like this: `['first column text', ['cell 1', 'cell 2', 'cell 3']]`. 


### .get_textlength_from_cell(row: int, column: int) -> int
Returns the length of the text of the cell at the position (`row`, `column`).


### .help() -> None
The `.help()`-function runs the python command `help(TableValues)` and shows the output in your terminal. In Linux you can leave this with ctrl-Z.

```
Help on class TableValues in module widgets.table:

class TableValues(builtins.object)
 |  TableValues(header_row: list = [], first_column: list = [])
 |
 |  Methods defined here:
 |
 |  __init__(self, header_row: list = [], first_column: list = [])
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  add_column(self, header_row_value: str = ' ', values: list[str] = [' ']) -> None
 |      Adds a new column to the end of the table
 |
 |  add_row(self, first_column_value: str = ' ', values: list[str] = [' ']) -> None
 |      Adds a new row to the end of the table
 |
 |  copy(self) -> <built-in function any>
 |      Creates a copy of this object and returns it
 |
 |  count(self, text: str, *, search_in_first_column: bool = False, search_in_header_row: bool = False) -> int
 |      Counts how often the text appears in the table
 |

...
```


### .insert_column(index: int = 0, header_row_value: str = ' ', values: list = [' ']) -> None
Inserts a column at the position `index`. The header row cells text is set to the value in `header_row_value` and the texts of the cells from the top to the bottom are set to the values in `values`.


### .insert_row(index: int = 0, first_column_value: str = ' ', values: list = [' ']) -> None
Inserts a row at the position `index`. The first column cells text is set to the value in `first_column_value` and the texts of the cells from left to right are set to the values in `values`.

### .is_numeric_column(column: int) -> bool
Returns `True` if all texts in this column are strings of integers, strings of floats or strings of float like values (like `'.8'` or `'2.'`).


### .is_numeric_row(row: int) -> bool
Returns `True` if all texts in this row are strings of integers, strings of floats or strings of float like values (like `'.8'` or `'2.'`).


### .set_align(align: TextAlign) -> None
Sets the align of all values in the table. It overwrites the aligns of all cells in the table. This doesn't change the header rows and first columns align.


### .set_align_at_cell(row: int, column: int, align: TextAlign) -> None
Sets the align of the text of the cell at the position (`row`, `column`) to the text align in `align`. This function overwrites the current text align of the cell.

### .set_first_column(first_column: list) -> None
Sets the texts of the first column to the texts in `first_column` (`first_column` is a list of strings).


### .set_first_column_align(align: TextAlign) -> None
Sets the align of the first column to the align in `align`. This overwrites the current text aligns of all cell texts in the first column.


### .set_first_column_align_at_position(pos: int, align: TextAlign) -> None
Sets the align of the cells text of the first column at the position `pos`. This overwrites the current text align of this first column cell.


### .set_header_row(header_row: list) -> None
Sets the texts of the header row to the texts in `header_row` (`header_row` is a list of strings).


### .set_header_row_align(align: TextAlign) -> None
Sets the align of the header row to the align in `align`. This overwrites the current text aligns of all cell texts in the header row.


### .set_header_row_align_at_position(pos: int, align: TextAlign) -> None
Sets the align of the cells text of the header row at the position `pos`. This overwrites the current text align of this header row cell.


### .set_text_at_cell(row: int, column: int, text: str) -> None
Sets the text of the cell at the position (`row`, `column`) to the value of `text`.

### .sum_column(column: int) -> float
Sums up all values in the column at the index `column` and returns the sum as float. Raises a ValueError if the column isn't numeric (you can check this with `.is_numeric_column()`).


### .sum_row(row: int) -> float
Sums up all values in the row at the index `row` and returns the sum as float. Raises a ValueError if the row isn't numeric (you can check this with `.is_numeric_row()`).


### .swap_columns(index1: int, index2: int) -> None
Swaps the column at the position `index1` with the column at the position `index2`.


### .swap_rows(index1: int, index2: int) -> None
Swaps the row at the position `index1` with the row at the position `index2`.


### .\_\_getitem__(key: int) -> list
You can use `your_table_values[0]` to get a list of the texts of the first row under the header row.

This means that you can use `your_table_values[3][5]` instead of `your_table_values.get_text_at_cell(3, 5)`


### .\_\_copy__() -> TableValues
You can create a copy of those table values with `copy.copy(your_table_values)`


### .\_\_deepcopy__() -> TableValues
You can create a copy of those table values with `copy.deepcopy(your_table_values)`


## BorderStyle()-class
There are 13 standart border styles in the `BorderStyle()`-class:

**INFO:** In your terminal are no gaps between the parts of the table (the distance between two lines is 0)

`BorderStyle.ASCII`:
```
+------+------+
|      |      |
+------+------+
|      |      |
+------+------+
```

`BorderStyle.BASIC`:
```
+——————+——————+
|      |      |
+——————+——————+
|      |      |
+——————+——————+
```

`BorderStyle.DOUBLE`:
```
╔══════╦══════╗
║      ║      ║
╠══════╬══════╣
║      ║      ║
╚══════╩══════╝
```

`BorderStyle.HEAVY`:
```
┏━━━━━━┳━━━━━━┓
┃      ┃      ┃
┣━━━━━━╋━━━━━━┫
┃      ┃      ┃
┗━━━━━━┻━━━━━━┛
```

`BorderStyle.HEAVY_DASHED`:
```
┏╍╍╍╍╍╍┳╍╍╍╍╍╍┓
┋      ┋      ┋
┣╍╍╍╍╍╍╋╍╍╍╍╍╍┫
┋      ┋      ┋
┗╍╍╍╍╍╍┻╍╍╍╍╍╍┛
```

`BorderStyle.HORIZONTAL_HEAVY`:
```
━━━━━━━━━━━━━━━
               
━━━━━━━━━━━━━━━
               
━━━━━━━━━━━━━━━
```

`BorderStyle.HORIZONTAL_LIGHT`:
```
───────────────
               
───────────────
               
───────────────
```

`BorderStyle.LIGHT` (default):
```
┌──────┬──────┐
│      │      │
├──────┼──────┤
│      │      │
└──────┴──────┘
```

`BorderStyle.LIGHT_ARC`:
```
╭──────┬──────╮
│      │      │
├──────┼──────┤
│      │      │
╰──────┴──────╯
```

`BorderStyle.LIGHT_DASHED`:
```
┌╌╌╌╌╌╌┬╌╌╌╌╌╌┐
┊      ┊      ┊
├╌╌╌╌╌╌┼╌╌╌╌╌╌┤
┊      ┊      ┊
└╌╌╌╌╌╌┴╌╌╌╌╌╌┘
```

`BorderStyle.VERTICAL_HEAVY`:
```
┃      ┃      ┃
┃      ┃      ┃
┃      ┃      ┃
┃      ┃      ┃
┃      ┃      ┃
```

`BorderStyle.VERTICAL_LIGHT`:
```
│      │      │
│      │      │
│      │      │
│      │      │
│      │      │
```

`BorderStyle.NO_BORDER`:
```





```
;-)


But you can also create your own styles and use them with: `BorderStyle.MY_STYLES['your_style_name']`

### .create_style(self, name: str, vertical_line: str, horizontal_line: str, upper_left_corner: str, upper_T_corner: str, upper_right_corner: str, left_T_corner: str, X_cross: str, right_T_corner: str, lower_left_corner: str, lower_T_corner: str, lower_right_corner: str) -> None
Creates a new border style. You can use this new borderstyle with `BorderStyle.MY_STYLES['name']`.

The default (LIGHT) `vertical_line` is: "─"

The default (LIGHT) `horizontal_line` is: "│"

The default (LIGHT) `upper_left_corner` is: "┌"

The default (LIGHT) `upper_T_corner` is: "┬"

The default (LIGHT) `upper_right_corner` is: "┐"

The default (LIGHT) `left_T_corner` is: "├"

The default (LIGHT) `X_cross` is: "┼"

The default (LIGHT) `right_T_corner` is: "┤"

The default (LIGHT) `lower_left_corner` is: "└"

The default (LIGHT) `lower_T_corner` is: "┴"

The default (LIGHT) `lower_right_corner` is: "┘"


### .create_style_from_tuple(self, name: str, style: tuple) -> None
Creates a new style from a tuple. You can use this new borderstyle with `BorderStyle.MY_STYLES['name']`.

The tuple should look like this (default/LIGHT):
```python
("─", "│", "┌", "┬", "┐", "├", "┼", "┤", "└", "┴", "┘")
```

## TableStyle()-class
There are 6 table styles:

`TableStyle.DEFAULT`:
```
┌──────┬──────┬──────┐
│      │      │      │
├──────┼──────┼──────┤
│      │      │      │
├──────┼──────┼──────┤
│      │      │      │
└──────┴──────┴──────┘
```

`TableStyle.ONLY_BORDER`:
```
┌────────────────────┐
│                    │
│                    │ 
│                    │
│                    │ 
│                    │
└────────────────────┘
```

`TableStyle.WITHOUT_BORDER`:
```

      │      │      
──────┼──────┼──────
      │      │      
──────┼──────┼──────
      │      │      

```

`TableStyle.WITHOUT_FIRST_COLUMN`:
```
┌──────┬──────┐
│      │      │
├──────┼──────┤
│      │      │
├──────┼──────┤
│      │      │
└──────┴──────┘
```

`TableStyle.WITHOUT_HEADER_ROW`:
```
┌──────┬──────┬──────┐
│      │      │      │
├──────┼──────┼──────┤
│      │      │      │
└──────┴──────┴──────┘
```

`TableStyle.WITHOUT_HEADER_ROW_AND_FIRST_COLUMN`:
```
┌──────┬──────┐
│      │      │
├──────┼──────┤
│      │      │
└──────┴──────┘
```


# Create Charts with PyGraph


## BarChart()-class


# Create Geometric Elements with PyGraph

## Rectangle()-class
Takes two arguments and four optional arguments.

- `width: int` - sets the width of the rectangle
- `height: int` - sets the height of the rectangle
- `border_chars: tuple[str] = ('#', '#', '#', '#', '#', '#')`  - sets the border of the rectangle
- `fill_char: str = ' '` - sets the character to fill the rectangle
- `text: str = ''` - sets the text of the rectangle
- `align: str = TextAlign.LEFT` - sets the text align of the text in the rectangle

### .copy() -> Rectangle
Creates a copy of this object and returns it.


### .draw() -> None
Prints the rectangle to the terminal.


### .get_align() -> str
Returns the align of the text in the rectangle as string (`'right'`, `'left'` and `'center'`).


### .get_border_chars() -> tuple
Returns the characters or symbols of the border of the rectangle as string.

The tuple consists of:
- a horizontal line at index 0
- a vertical line at index 1
- a top-left corner at index 2
- a top-right corner line at index 3
- a bottom-left corner line at index 4
- a bottom-right corner line at index 5


### .get_fill_char() -> str
Returns the character or symbol which fills the rectangle.


### .get_height() -> int
Returns the height of the rectangle as int. 


### .get_str() -> str
Returns the rectangle as multiline string.


### .get_text() -> str
Returns the text of the Rectangle.


### .get_width() -> int
Returns the width of the rectangle as int. 


### .set_align(align: TextAlign) -> None
Sets the align of the text in the rectangle to the align in `align`.


### .set_border_chars(border_chars: tuple) -> None
Sets the border chars of the rectangle to the border chars in `border_chars`.

`border_charts` needs to consists of:
- a horizontal line at index 0
- a vertical line at index 1
- a top-left corner at index 2
- a top-right corner line at index 3
- a bottom-left corner line at index 4
- a bottom-right corner line at index 5


### .set_fill_char(fill_char: str) -> None
Sets the character or symbol with which the rectangle gets filled to `fill_char`.


### .set_height(height: int) -> None
Sets the height of the rectangle to the value in `height`.


### .set_text(text: str) -> None
Sets the text of the rectangle to the value in `text`.

Newlines in the string are ignored.


### .set_width(width: int) -> None
Sets the width of the rectangle to the value in `width`.


### .\_\_copy__() -> Rectangle
You can create a copy of this rectangle with `copy.copy(your_rectangle)`


### .\_\_deepcopy__() -> Rectangle
You can create a copy of this rectangle with `copy.deepcopy(your_rectangle)`


## RectangleBorder()-class
There are 13 default border styles:

**INFO:** In your terminal are no gaps between the parts of the table (the distance between two lines is 0)

`RectangleBorder.ASCII`:
```
+------+
|      |
+------+
```

`RectangleBorder.BASIC`:
```
+——————+
|      |
+——————+
```

`RectangleBorder.DOUBLE`:
```
╔══════╗
║      ║
╚══════╝
```

`RectangleBorder.HEAVY`:
```
┏━━━━━━┓
┃      ┃
┗━━━━━━┛
```

`RectangleBorder.HEAVY_DASHED`:
```
┏╍╍╍╍╍╍┓
┋      ┋
┗╍╍╍╍╍╍┛
```

`RectangleBorder.LIGHT` (default):
```
┌──────┐
│      │
└──────┘
```

`RectangleBorder.LIGHT_ARC`:
```
╭──────╮
│      │
╰──────╯
```

`RectangleBorder.LIGHT_DASHED`:
```
┌╌╌╌╌╌╌┐
┊      ┊
└╌╌╌╌╌╌┘
```

`RectangleBorder.NO_BORDER`:
```



```
;-)


### .create_style(name: str, horizontal_line: str, vertical_line: str, upper_left_corner: str, upper_right_corner: str, lower_left_corner: str, lower_right_corner: str) -> None
Creates a style with the characters in `horizontal_line`, `vertical_line`, `upper_left_corner`, `upper_right_corner`, `lower_left_corner` and `lower_right_corner` as horizontal line, vertical line, upper-left corner, upper-right corner, lower-left corner and lower-right corner.


### .create_style_from_tuple(name: str, style: tuple) -> None
Creates a style from a tuple. The items in the tuple from index 0 to index 5 are the horizontal line, the vertical line, the upper-left corner, the upper-right corner, the lower-left corner and the lower-right corner.


## Line()-class
Takes four arguments and one optional argument.

- `startx: int` - sets the starting x position of the line
- `starty: int` - sets the starting y position of the line
- `endx: int` - sets the ending x position of the line
- `endy: int` - sets the ending y position of the line
- `symbol: str = '#'` - sets the symbol of the line to a single character

### .copy() -> Line
Creates a copy of this object and returns it.


### .draw() -> None
Prints the line to the terminal.


### .get_end_pos() -> tuple
Returns the ending position of the line as tuple with the format (x, y).


### .get_gradient() -> float
Returns the gradient of the line as float.


### .get_start_pos() -> tuple
Returns the starting position of the line as tuple with the format (x, y).


### .get_str() -> str
Returns the line as string.


### .get_symbol() -> str
Returns the symbol the line is made of.


### .set_end_pos(endx: int, endy: int) -> None
Sets the ending position of the line to (`endx`, `endy`).


### .set_start_pos(startx: int, starty: int) -> None
Sets the starting position of the line to (`startx`, `starty`).


### .set_symbol(symbol: str) -> None
Sets the symbol of the line to the single character or symbol in `symbol`.


### .\_\_copy__() -> Line
You can create a copy of this line with `copy.copy(your_line)`


### .\_\_deepcopy__() -> Line
You can create a copy of this line with `copy.deepcopy(your_line)`


# Create Texts with PyGraph

## Text()-class
The Text()-class takes one argument and three optional arguments:

- `text: str` - The text of this object
- `width: int = -1` - The width of the formated text (-1 means "take the length of the text")
- `height: int = 1` - The height of the formated text
- `optimal_height: bool = True` - If set to True, `height` is ignored and the optimal height for the text is chosen


### .copy() -> Text
Creates a copy of this object and returns it.


### .get_formated_text() -> str
Returns the text of this Text()-object with the width and height set earlier.

If the text is: "Some cool text, but longer and longer", the width is 10 and the height is 10, the formated text would look like this:
```
Some cool
text, but
longer and
longer






```


### .get_height() -> int
Returns the height of the text as integer.


### .get_str() -> str
This function does the same as `get_formated_text()`.

This function exists, because the Overview()-class needs a `.get_str()`-function for it's widgets.


### .get_text() -> str
Returns the unformated text of this object.


### .get_width() -> int
Returns the width of the text as integer.


### .print() -> None
Prints the formated text to the terminal.


### .set_height(height: int) -> None
Sets the texts height to the value in `height`.


### .set_optimal_height(optimal_height: bool = True) -> None
Sets optimal height to True.

This means that you don't need to enter a height manually and there are no newlines at the end of the text.


### .set_text(text: str) -> None
Sets the text of this object to the value in `text`.


### .set_width(width: int) -> None
Sets the texts width to the value in `width`.


### .\_\_copy__() -> Text
You can create a copy of this text with `copy.copy(your_text)`


### .\_\_deepcopy__() -> Text
You can create a copy of this text with `copy.deepcopy(your_text)`


# Create an Widget Overview with PyGraph

## Overview()-class

### .add_widget(widget: Table | Rectangle | Line | Text, x: int, y: int) -> None
Adds the widget in `widget` to the overview at the position (`x`, `y`).


### .copy() -> Overview
Creates a copy of this object and returns it.

This functions doesn't copy the widgets in it.


### .deepcopy() -> Overview
Creates a copy of this object and of all widgets in it and returns it.


### .delete_widget(widget: Table | Rectangle | Line | Text) -> Table | Rectangle | Line | Text
Deletes the widget `widget` from the overview and returns it.

If the widget doesn't exist in this overview, then a ValueError is raised.


### .get_str() -> str
Returns the overview as string.


### .has_widget(widget: Table | Rectangle | Line | Text) -> bool
Returns `True` if the widget `widget` is a widget of this overview, else False.


### .print() -> None
Prints the overview to the terminal.


### .\_\_copy__() -> Overview
You can create a copy of this overview with `copy.copy(your_overview)`


### .\_\_deepcopy__() -> Overview
You can create a copy of this overview with `copy.deepcopy(your_overview)`


# Format Text with PyGraph

## ColoredText()-class
The `ColoredText()`-class contains items to print colored text to the terminal.

The colors are:
```python
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
```

`END` is the default terminal text color. You can use it to reset the color.

You can use the colors with `ColoredText.COLOR`, like `ColoredText.RED` and `ColoredText.BLUE`.

To print a red text, you can write:
```python
print(ColoredText.RED + 'This is my red text, it ends here ->' + ColoredText.END)
``` 


## ColoredBackground()-class
The `ColoredBackground()`-class contains items to print text with colored background to the terminal.

The background colors are:
```python
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
```

`END` is the default terminal text background color. You can use it to reset the background color.

You can use the background colors with `ColoredBackground.COLOR`, like `ColoredBackground.RED` and `ColoredBackground.BLUE`.

To print a text with a red background, you can write:
```python
print(ColoredBackground.RED + 'This is my text with red background, it ends here ->' + ColoredBackground.END)
``` 


## FormatedText()-class
The `FormatedText()`-class contains items to print text with colored background to the terminal.

The background colors are:
```python
END       = '\033[0m'

BOLD      = '\33[1m'
ITALIC    = '\33[3m'
URL       = '\33[4m'
BLINK     = '\33[5m'
BLINK2    = '\33[6m'
SELECTED  = '\33[7m'
```

`END` is the default terminal text style. You can use it to reset the text style.

You can use the styles with `FormatedText.STYLE`, like `FormatedText.BOLD` and `FormatedText.ITALIC`.

To print a bold text, you can write:
```python
print(FormatedText.BOLD + 'This is my bold text, it ends here ->' + FormatedText.END)
```


## TextAlign()-class
The `TextAlign()`-class contains three strings saved in the variables `RIGHT`, `LEFT` and `CENTER`.

The text in `RIGHT` is `'right'`.

The text in `LEFT` is `'left'`.

The text in `CENTER` is `'center'`.


You can use this class to set the text align of a string, like with the string methods `.rjust()`, `.ljust()` and `.center()`.

To set the text align of a string, use the `TextAlign.set_text_align()`-function.

### .set_text_align(text: str, space: int, align: str, fill_char: str = ' ') -> str
Sets the text align of the text in `text` to the align in `align`. The value of `align`
needs to be a string (`'right'`, `'left'` or `'center'`), here you can use the `TextAlign()`-constants `RIGHT`, `LEFT` and `CENTER`.
The value in `space` is the length of the final string, this means if the string is `'Hello'` and you set `align` to `'right'` and `space`
is set to `10` the final string looks like `'     Hello'`. You can change the characters that are filled in (by default `' '`), by setting
the value in `fill_char` to another value. If `fill_char` is set to `'-'` the final string would look like this: `'-----Hello'`.


## Other Functions

### make_text_horizontal(text: str) -> str
Returns the text as multiline string, in which the text is written horizontal:

```python
>>> make_text_horizontal('Some Cool Text')
S
o
m
e

C
o
o
l

T
e
x
t
```


### make_text_backwards(text: str) -> str
Returns the text, but written backwards:

```python
>>> make_text_backwards('Some Cool Text')
txeT looC emoS
```


# Examples

## Table()-class

### Table to show all products from 1\*1 to 10\*10

```python
from widgets.table import Table, TableValues

table = Table('1*1 - 10*10')        # Create a Table()-object

values = TableValues()              # Create a TableValues()-object
values.set_header_row(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])      # Set the header row of the TableValues()-object
values.set_first_column(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])    # Set the first column of the TableValues()-object
for col in range(10):
    for row in range(10):
        values.set_text_at_cell(row, col, str( (row+1) * (col+1) ))             # Set all cell texts from (0, 0) to (9, 9) to the products of 1*1 to 10*10

table.set_values(values)            # Set the table's values to the TableValues()-object

table.print()                       # Print the table to the terminal
```


If you run this code you will see this table in your terminal:

```
                                 1*1 - 10*10                                  

┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐
│      │     1│     2│     3│     4│     5│     6│     7│     8│     9│    10│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│     1│     1│     2│     3│     4│     5│     6│     7│     8│     9│    10│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│     2│     2│     4│     6│     8│    10│    12│    14│    16│    18│    20│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│     3│     3│     6│     9│    12│    15│    18│    21│    24│    27│    30│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│     4│     4│     8│    12│    16│    20│    24│    28│    32│    36│    40│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│     5│     5│    10│    15│    20│    25│    30│    35│    40│    45│    50│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│     6│     6│    12│    18│    24│    30│    36│    42│    48│    54│    60│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│     7│     7│    14│    21│    28│    35│    42│    49│    56│    63│    70│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│     8│     8│    16│    24│    32│    40│    48│    56│    64│    72│    80│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│     9│     9│    18│    27│    36│    45│    54│    63│    72│    81│    90│
├──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┼──────┤
│    10│    10│    20│    30│    40│    50│    60│    70│    80│    90│   100│
└──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘
```


### Table to show the money spend in this month

```python
from widgets.table import Table, TableValues, TableStyle
from widgets.text import TextAlign

table = Table('money spend in this month')          # Create a Table()-object

values = TableValues()                              # Create a TableValues()-object
values.set_header_row(['Date', 'Bought Object', 'Price in €'])  # Set header row of table values
values.add_row('', ['09.01.2025', 'Computer', '2035'])          # Add a row to the table values
values.add_row('', ['10.01.2025', 'Fridge', '799'])             # Add a row to the table values
values.add_row('', ['18.01.2025', 'Pencil', '1'])               # Add a row to the table values
values.add_row('', ['21.01.2025', 'Fridge', '899'])             # Add a row to the table values
values.add_row('', ['23.01.2025', 'Car', '100000'])             # Add a row to the table values

values.set_align(TextAlign.CENTER)                  # Set the text align to center
values.set_header_row_align(TextAlign.CENTER)       # Set the header row text align to center

table.set_values(values)                            # Set the tables values to the TableValues()-object
table.set_style(TableStyle.WITHOUT_FIRST_COLUMN)    # Hide first column (we don't want a first column in this table)
table.show_sum_row([2])                             # Show a sum row with the sum of all values in the third column (third column has index 2)

table.print()                                       # Print the table to the terminal
```


If you run this code you will see this table in your terminal:

```
        Money Spend In This Month                              

┌─────────────┬─────────────┬─────────────┐
│     Date    │Bought Object│  Price in € │
├─────────────┼─────────────┼─────────────┤
│  09.01.2025 │   Computer  │     2035    │
├─────────────┼─────────────┼─────────────┤
│  10.01.2025 │    Fridge   │     799     │
├─────────────┼─────────────┼─────────────┤
│  18.01.2025 │    Pencil   │      1      │
├─────────────┼─────────────┼─────────────┤
│  21.01.2025 │    Fridge   │     899     │
├─────────────┼─────────────┼─────────────┤
│  23.01.2025 │     Car     │    100000   │
├─────────────┼─────────────┼─────────────┤
│             │             │   103734.0  │
└─────────────┴─────────────┴─────────────┘
```


### A TicTacToe game

```python
from widgets.table import Table, TableValues, TableStyle
from widgets.text import TextAlign

tictactoe = Table()                     # Create a table

values = TableValues()                  # Create table values
values.set_header_row(['', '', ''])     # Create an empty header row
values.add_row('', [' ', ' ', ' '])     # Create an empty row
values.add_row('', [' ', ' ', ' '])     # Create an empty row
values.add_row('', [' ', ' ', ' '])     # Create an empty row

values.set_align(TextAlign.CENTER)      # Set the text align of all values to center

tictactoe.set_values(values)            # Set the tables values to the TableValues()-object
tictactoe.set_styles([TableStyle.WITHOUT_FIRST_COLUMN, TableStyle.WITHOUT_HEADER_ROW, TableStyle.WITHOUT_BORDER])   # Set the table styles

tictactoe.set_hide_title(True)          # Hide the tables title
tictactoe.set_default_cell_length(3)    # Make the fields smaller

turn = 'X'                              # Set the player symbol of the player which begins to "X"
for _ in range(9):                      # Play 9 rounds at most
    
    tictactoe.print()                   # Print the tic tac toe board

    field = int(input('Enter a field (1-9): '))     # Enter the field you want to play (1-9)

    tictactoe.get_values().set_text_at_cell((field-1)//3, (field-1)%3, turn)    # Set your symbol at the field you want to play

    # Check if someone won (horizontal)
    if tictactoe.get_values().get_text_from_cell(0,0) == tictactoe.get_values().get_text_from_cell(0,1) == tictactoe.get_values().get_text_from_cell(0,2) != ' ' or \
        tictactoe.get_values().get_text_from_cell(1,0) == tictactoe.get_values().get_text_from_cell(1,1) == tictactoe.get_values().get_text_from_cell(1,2) != ' ' or \
        tictactoe.get_values().get_text_from_cell(2,0) == tictactoe.get_values().get_text_from_cell(2,1) == tictactoe.get_values().get_text_from_cell(2,2) != ' ':
        break
    
    # Check if someone won (vertical)
    elif tictactoe.get_values().get_text_from_cell(0,0) == tictactoe.get_values().get_text_from_cell(1,0) == tictactoe.get_values().get_text_from_cell(2,0) != ' ' or \
        tictactoe.get_values().get_text_from_cell(0,1) == tictactoe.get_values().get_text_from_cell(1,1) == tictactoe.get_values().get_text_from_cell(2,1) != ' ' or \
        tictactoe.get_values().get_text_from_cell(0,2) == tictactoe.get_values().get_text_from_cell(1,2) == tictactoe.get_values().get_text_from_cell(2,2) != ' ':
        break
    
    # Check if someone won (diagonal)
    elif tictactoe.get_values().get_text_from_cell(0,0) == tictactoe.get_values().get_text_from_cell(1,1) == tictactoe.get_values().get_text_from_cell(2,2) != ' ' or \
        tictactoe.get_values().get_text_from_cell(0,2) == tictactoe.get_values().get_text_from_cell(1,1) == tictactoe.get_values().get_text_from_cell(2,0) != ' ':
        break


    # Change the turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


tictactoe.print()   # If the game is over, print the final board

```


If you run this code you will see a tic tac toe game in your terminal, that you can play with your friends:

```
   │   │   
───┼───┼───
   │   │   
───┼───┼───
   │   │   

Enter a field (1-9): 2
   │ X │   
───┼───┼───
   │   │   
───┼───┼───
   │   │   

Enter a field (1-9): 7
   │ X │   
───┼───┼───
   │   │   
───┼───┼───
 O │   │   

Enter a field (1-9): 6
   │ X │   
───┼───┼───
   │   │ X 
───┼───┼───
 O │   │   

Enter a field (1-9): 5
   │ X │   
───┼───┼───
   │ O │ X 
───┼───┼───
 O │   │   

Enter a field (1-9): 3
   │ X │ X 
───┼───┼───
   │ O │ X 
───┼───┼───
 O │   │   

Enter a field (1-9): 1
 O │ X │ X 
───┼───┼───
   │ O │ X 
───┼───┼───
 O │   │   

Enter a field (1-9): 9
 O │ X │ X 
───┼───┼───
   │ O │ X 
───┼───┼───
 O │   │ X 
```


## 










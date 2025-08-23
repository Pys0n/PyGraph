from widgets.charts import *
from widgets.geometry import *
from widgets.table import *
from widgets.text import *


class Overview:
    def __init__(self):
        '''
        Creates an overview over your widgets at a glance
        '''
        self.widgets: list = []


    def copy(self) -> any:
        '''
        Returns a copy of this object
        '''
        overview = Overview()
        
        for widget in self.widgets:
            overview.add_widget(widget)
        
        return overview


    def deepcopy(self) -> any:
        '''
        Returns a copy of this object and copies of its widgets
        '''
        overview = Overview()
        
        for widget in self.widgets:
            overview.add_widget(widget.copy())
        
        return overview

    
    def add_widget(self, widget: Table | Rectangle | Line | Text, x: int, y: int) -> None:
        '''
        Adds a widget to the overview
        '''
        if not isinstance(widget, Table) and not isinstance(widget, Rectangle) and not isinstance(widget, Line):
            raise TypeError('Excpected widget to be a Table, Rectangle or Line, got '+type(widget).__name__)
        if not isinstance(x, int):
            raise TypeError('Excpected x to be an int, got '+type(x).__name__)
        if not isinstance(y, int):
            raise TypeError('Excpected y to be an int, got '+type(y).__name__)

        self.widgets.append((widget, x, y))

    
    def delete_widget(self, widget: Table | Rectangle | Line | Text) -> Table | Rectangle | Line | Text:
        '''
        Deletes a widget from the overview
        '''
        if not isinstance(widget, Table) and not isinstance(widget, Rectangle) and not isinstance(widget, Line):
            raise TypeError('Excpected widget to be a Table, Rectangle or Line, got '+type(widget).__name__)
        
        for i, item in enumerate(self.widgets):
            if id(widget) == id(item[0]):
                self.widgets.pop(i)
                return widget
            
        raise ValueError('Overview don\'t has the widget '+str(widget))


    def has_widget(self, widget: Table | Rectangle | Line | Text) -> bool:
        '''
        Returns True if the widget is a widget of the overview
        '''
        if not isinstance(widget, Table) and not isinstance(widget, Rectangle) and not isinstance(widget, Line):
            raise TypeError('Excpected widget to be a Table, Rectangle or Line, got '+type(widget).__name__)
        
        for item in self.widgets:
            if id(widget) == id(item[0]):
                return True
        return False


    def print(self) -> None:
        '''
        Prints the overview to the terminal
        '''
        print(self.get_str())


    def get_str(self) -> str:
        '''
        Returns the overview as string
        '''
        return str(self)


    def __str__(self):
        widgets = []
        width = 0
        height = 0
        for item in self.widgets:
            widgets.append((item[0].get_str(), item[1], item[2]))
            if item[1] + len(item[0].get_str().split('\n')[0]) > width:
                width = item[1] + len(item[0].get_str().split('\n')[0])
            if item[2] + len(item[0].get_str().split('\n')) > height:
                height = item[2] + len(item[0].get_str().split('\n'))

        overview = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(' ')
            overview.append(row)

        for item in widgets:
            offsetx = item[1]
            offsety = item[2]
            for y, line in enumerate(item[0].split('\n')):
                for x, character in enumerate(line):
                    if isinstance(self.widgets[widgets.index(item)][0], Table):
                        overview[y+offsety][x+offsetx] = character
                        continue
                    elif character != ' ':
                        overview[y+offsety][x+offsetx] = character


        overview_str = ''
        for row in overview:
            overview_str += ''.join(row) + '\n'

        return overview_str
    

    def __copy__(self) -> any:
        return self.copy()
    

    def __deepcopy__(self) -> any:
        return self.deepcopy()
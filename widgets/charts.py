from widgets.text import ColoredBackground


BarColor = ColoredBackground


class Chart:
    def __init__(self, name: str, x_axis: list, y_axis: list, values: dict) -> None:
        if not isinstance(name, str):
            raise TypeError('Excpected name to be a str, got '+type(name).__name__)
        if not isinstance(x_axis, list):
            raise TypeError('Excpected x_axis to be a list, got '+type(x_axis).__name__)
        if not isinstance(y_axis, list):
            raise TypeError('Excpected y_axis to be a list, got '+type(y_axis).__name__)
        if not isinstance(values, dict):
            raise TypeError('Excpected values to be a dict, got '+type(values).__name__)
        
        self.name = name
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.values = values


    def set_name(self, name: str) -> None:
        '''
        Sets the name of the chart
        '''
        if not isinstance(name, str):
            raise TypeError('Excpected name to be a str, got '+type(name).__name__)
        
        self.name = name


    def set_x_axis(self, x_axis: list) -> None:
        '''
        Sets the x axis of the chart
        '''
        if not isinstance(x_axis, list):
            raise TypeError('Excpected x_axis to be a list, got '+type(x_axis).__name__)
        
        self.x_axis = x_axis


    def set_y_axis(self, y_axis: list) -> None:
        '''
        Sets the y axis of the chart
        '''
        if not isinstance(y_axis, list):
            raise TypeError('Excpected y_axis to be a list, got '+type(y_axis).__name__)
        
        self.y_axis = y_axis


    def set_values(self, values: dict) -> None:
        '''
        Sets the values of the chart
        '''
        if not isinstance(values, dict):
            raise TypeError('Excpected values to be a dict, got '+type(values).__name__)
        
        self.values = values


    def get_name(self) -> str:
        '''
        Returns the name of the chart
        '''
        return self.name


    def get_x_axis(self) -> list:
        '''
        Returns the x axis of the chart
        '''
        return self.x_axis


    def get_y_axis(self) -> list:
        '''
        Returns the y axis of the chart
        '''
        return self.y_axis
    

    def get_values(self) -> dict:
        '''
        Returns the values of the chart
        '''
        return self.values
    


class BarChart(Chart):
    def __init__(self, name: str, x_axis: list, y_axis: list, bar_width: int = 1, *, values: dict = {}) -> None:
        super().__init__(name, x_axis, y_axis, values)
        self.bar_width: int = bar_width
    

    def add_bar(self, x, y) -> None:
        '''
        Adds a bar that starts at x and goes up to y

        x and y must be items of x_axis and y_axis
        '''
        if x not in self.x_axis:
            raise ValueError('The charts x axis has no item named "'+str(x)+'"')
        if y not in self.y_axis:
            raise ValueError('The charts y axis has no item named "'+str(y)+'"')
        
        self.values[x] = [y, BarColor.WHITE]


    def delete_bar(self, x) -> None:
        '''
        Deletes the bar at the position x

        x must be a item of x_axis
        '''
        if x not in self.x_axis:
            raise ValueError('The charts x axis has no item named "'+str(x)+'"')
        if x not in self.values.keys():
            raise ValueError('There is no bar at "'+str(x)+'"')
        
        self.values[x][0] = None


    def set_all_bar_colors(self, bar_color: str) -> None:
        '''
        Sets the color of all bars
        '''
        if not isinstance(bar_color, str):
            raise TypeError('Excpected bar_color to be a str, got '+type(bar_color).__name__)

        for key in self.values:
            self.values[key][1] = bar_color

    
    def set_bar_color(self, x, bar_color: str) -> None:
        '''
        Sets the color of the bar at position x
        '''
        if x not in self.x_axis:
            raise ValueError('The charts x axis has no item named "'+str(x)+'"')
        if x not in self.values.keys():
            raise ValueError('There is no bar at "'+str(x)+'"')
        if not isinstance(bar_color, str):
            raise TypeError('Excpected bar_color to be a str, got '+type(bar_color).__name__)

        self.values[x][1] = bar_color


    def set_bar_width(self, width: int) -> None:
        '''
        Sets the width of all bars
        '''
        if not isinstance(width, int):
            raise TypeError('Excpected width to be an int, got '+type(width).__name__)
        
        self.bar_width = width


    def get_bar_width(self) -> int:
        '''
        Returns the width of all bars
        '''
        return self.bar_width
    

    def print(self) -> None:
        '''
        Prints the graph to the terminal
        '''
        print(str(self))
              

    def get_str(self) -> str:
        '''
        Returns the graph as string
        '''
        return str(self)


    def __str__(self) -> str:
        graph = []

        self.y_axis.reverse()
        y_axis = self.y_axis.copy()
        self.y_axis.reverse()

        space_before_graph = 0
        for item in y_axis:
            if len(str(item)) > space_before_graph:
                space_before_graph = len(str(item)) + 2

        graph.append(' ' * space_before_graph + '  │\n')
        print_bars = set()
        for item in y_axis:
            line = ' ' + str(item).rjust(space_before_graph) + ' ┼ '

            for key in self.values:
                if str(self.values[key][0]) == str(item) or key in print_bars:
                    print_bars.add(key)
                    line += str('#'*self.bar_width).center((len(str(key))//2 if len(str(key))//2 > self.bar_width*4-2 else 0)+(self.bar_width*4))
                else:
                    line += str(' '*self.bar_width).center((len(str(key))//2 if len(str(key))//2 > self.bar_width*4-2 else 0)+(self.bar_width*4))

            

            graph.append(line+'\n')
            for _ in range(self.bar_width):
                line = ' ' * space_before_graph + '  │ '
                for key in self.values:
                    if str(self.values[key][0]) == str(item) or key in print_bars:
                        print_bars.add(key)
                        line += str('#'*self.bar_width).center((len(str(key))//2 if len(str(key))//2 > self.bar_width*4-2 else 0)+(self.bar_width*4))
                    else:
                        line += str(' '*self.bar_width).center((len(str(key))//2 if len(str(key))//2 > self.bar_width*4-2 else 0)+(self.bar_width*4))
                graph.append(line + '\n')

        x = ' ' * (space_before_graph+2) + '└─'

        for item in self.x_axis:
            item_len = len(str(item))//2
            x += '┼'.center((item_len if item_len > self.bar_width*4-2 else 0)+(self.bar_width*4), '─')

        graph.append(x + '\n')

        x_text = ' ' * (space_before_graph+4)

        for item in self.x_axis:
            x_text += str(item).center((len(str(item))//2 if len(str(item))//2 > self.bar_width*4-2 else 0)+(self.bar_width*4), ' ')

        graph.append(x_text + '\n')

        return ''.join(graph)
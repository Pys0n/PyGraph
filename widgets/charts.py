class Direction:
    VERTICAL = 0
    HORIZONTAL = 1


class Position:
    X = 0
    Y = 1


class Axis:
    def __init__(self, name: str = '', pos: Position = Position.X, labels: list[str] = []):
        self.name = name
        self.pos = pos      # "x" or "y"
        self.labels = labels
        self.shown_labels = []


    def set_labels(self, labels: list[str]) -> None:
        '''
        Sets the labels
        '''
        self.labels = labels


    def set_position(self, pos: Position) -> None:
        '''
        Sets the axis position ("x" or "y")
        '''
        self.pos = pos


    def set_name(self, name: str) -> None:
        '''
        Sets the name of the axis
        '''
        self.name = name


    def config_labels(self, shown_labels: list[str]) -> None:
        self.shown_labels = shown_labels


class BarChart:
    def __init__(self, title: str = '', *, x: Axis = None, y: Axis = None, direction: Direction = Direction.VERTICAL, values: list[tuple[str, str]] = []) -> None:
        self.title = title
        self.xaxis = x
        self.yaxis = y
        self.direction = direction
        self.values = values


    def set_axis(self, xy: Position, axis: Axis) -> None:
        if xy == Position.X:
            self.xaxis = axis
        elif xy == Position.Y:
            self.yaxis = axis
    

    def set_title(self, title: str):
        '''
        Sets the title of the bar chart
        '''
        self.title = title


    def set_direction(self, direction: Direction) -> None:
        '''
        Sets the direction of the bar chart
        '''
        self.direction = direction
    

    def set_values(self, values: list[tuple[str, str]]) -> None:
        '''
        Sets the values of the bar chart
        '''
        self.values = values


    def print(self) -> None:
        '''
        Prints the bar chart
        '''
        print('X:', self.xaxis.labels)
        print('Y:', self.yaxis.labels)
        print('Values:\n', self.values)
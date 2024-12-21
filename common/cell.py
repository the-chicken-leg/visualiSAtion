from graphics import *

class Cell(Square):
    def __init__(self, parent: Window, center: Point, cell_size: int, i: int, j: int):
        super().__init__(parent, center, cell_size)
        self.searched = False
        self.i = i
        self.j = j

    def draw(self):
        fill_color = "white"
        if self.searched:
            fill_color = "gray"
        super().draw(fill_color)
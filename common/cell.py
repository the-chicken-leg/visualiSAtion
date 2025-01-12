from graphics import *

class Cell(Square):
    def __init__(self, i: int, j: int, center: Point):
        super().__init__()

        self.i = i
        self.j = j
        self.center = center
        self.searched = False

    def draw(self, window: Window, cell_size: int):
        fill_color = "white"
        if self.searched:
            fill_color = "gray"
        super().draw(window, self.center, cell_size, fill_color)
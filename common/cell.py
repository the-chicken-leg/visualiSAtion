from . import graphics as gr

class Cell(gr.Square):
    def __init__(self, i: int, j: int, center: gr.Point):
        super().__init__()

        self.i = i
        self.j = j
        self.center = center
        self.searched = False

    def draw(self, window: gr.Window, cell_size: int):
        fill_color = "white"
        if self.searched:
            fill_color = "gray"
        super().draw(window, self.center, cell_size, fill_color)

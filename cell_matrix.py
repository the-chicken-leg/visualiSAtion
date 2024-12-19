from graphics import *
from cell import *
import time

class CellMatrix:
    def __init__(self, parent: Window, cell_size: int, smooth_cell_creation: bool):
        self.parent = parent
        self.cell_size = cell_size
        self.smooth_cell_creation = smooth_cell_creation

        self.num_columns = (parent.width - 50) // self.cell_size
        self.x_border = (parent.width - (self.cell_size * self.num_columns)) // 2

        self.num_rows = (parent.height - 50) // self.cell_size
        self.y_border = (parent.height - (self.cell_size * self.num_rows)) // 2

        self.create_cell_matrix()

    def create_cell_matrix(self):
        self.cell_matrix = []
        for i in range(self.num_rows):
            row = []
            center_y = self.y_border + (0.5 * self.cell_size) + (i * self.cell_size)
            for j in range(self.num_columns):
                center_x = self.x_border + (0.5 * self.cell_size) + (j * self.cell_size)
                row.append(
                    Cell(
                        self.parent,
                        Point(center_x, center_y),
                        self.cell_size,
                        i,
                        j,
                    )
                )
            self.cell_matrix.append(row)

        self.draw_cell_matrix()

    def draw_cell_matrix(self):
        for cell_row in self.cell_matrix:
            for cell in cell_row:
                cell.draw()
                self.parent.redraw()
                if self.smooth_cell_creation:
                    time.sleep(0.01)
from cell import *
import time

class CellMatrix:
    def __init__(self, window: Window, cell_size: int, smooth_cell_creation: bool):
        self.window = window
        self.cell_size = cell_size

        self.num_columns = (window.width - 50) // cell_size
        x_border = (window.width - (cell_size * self.num_columns)) // 2

        self.num_rows = (window.height - 50) // cell_size
        y_border = (window.height - (cell_size * self.num_rows)) // 2

        self.cell_matrix = []
        for i in range(self.num_rows):
            row = []
            center_y = y_border + (0.5 * cell_size) + (i * cell_size)
            for j in range(self.num_columns):
                center_x = x_border + (0.5 * cell_size) + (j * cell_size)
                cell = Cell(i, j, Point(center_x, center_y))
                row.append(cell)
            self.cell_matrix.append(row)

        for cell_row in self.cell_matrix:
            for cell in cell_row:
                cell.draw(window, cell_size)
                window.redraw()
                if smooth_cell_creation:
                    time.sleep(0.01)
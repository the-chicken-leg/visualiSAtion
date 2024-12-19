import os, sys
sys.path.insert(0, os.path.join(os.getcwd()))

from graphics import *
from cell import Cell

class DirtyDishes:
    def __init__(self, parent: Window, single_dish_height: int, smooth_dishes: bool):
        self.parent = parent
        self.single_dish_height = single_dish_height
        self.smooth_dishes = smooth_dishes

        self.num_columns = 1
        self.x_border = (parent.width - (self.single_dish_height * self.num_columns)) // 2

        self.num_rows = (parent.height - 50) // self.single_dish_height
        self.y_border = (parent.height - (self.single_dish_height * self.num_rows)) // 2

        self.create_cell_matrix()

    def create_cell_matrix(self):
        self.cell_matrix = []
        for i in range(self.num_rows):
            row = []
            center_y = self.y_border + (0.5 * self.single_dish_height) + (i * self.single_dish_height)
            for j in range(self.num_columns):
                center_x = self.x_border + (0.5 * self.single_dish_height) + (j * self.single_dish_height)
                row.append(
                    Cell(
                        self.parent,
                        Point(center_x, center_y),
                        self.single_dish_height,
                        i,
                        1,
                    )
                )
            self.cell_matrix.append(row)

        self.draw_cell_matrix()

    def draw_cell_matrix(self):
        for cell_row in self.cell_matrix:
            for cell in cell_row:
                cell.draw()
                self.parent.redraw()
                if self.smooth_dishes:
                    time.sleep(0.01)
from graphics import *
from cell import *
import random
import time

class BFS:
    def __init__(self, parent: Window, cell_size: int):
        self.parent = parent
        self.cell_size = cell_size

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
                    )
                )
            self.cell_matrix.append(row)

        self.draw_cell_matrix()

    def draw_cell_matrix(self):
        for cell_row in self.cell_matrix:
            for cell in cell_row:
                cell.draw()
                self.parent.redraw()
                time.sleep(0.01)

    def search(self, start_i: int, start_j: int, sleep_time: int, seed=None):
        self.sleep_time = sleep_time
        if seed is not None:
            random.seed(seed)
        self.search_r(start_i, start_j, [("start", self.cell_matrix[start_i][start_j])])

    def search_r(self, i: int, j: int, to_search: list):
        while to_search:
            direction, current_cell = to_search.pop(0)
            if direction == "top":
                i -= 1
            if direction == "right":
                j += 1
            if direction == "bottom":
                i += 1
            if direction == "left":
                j -= 1
            print(i, j, direction, current_cell)
            current_cell.searched = True
            current_cell.draw()
            self.parent.redraw()
            time.sleep(self.sleep_time)

            neighbors = self.get_cell_neighbors(i, j)
            valid_neighbors = {k: v for k, v in neighbors.items() if v and v.searched == False} 
            for direction, neighbor in valid_neighbors.items():
                if neighbor not in to_search:
                    to_search.append((direction, neighbor))

            print(to_search)
            input("Press Enter to continue")
            self.search_r(i, j, to_search)
    
    def get_previous_cell(self, i: int, j: int, direction: str):
        if direction == "top":
            return self.cell_matrix[i + 1][j]
        if direction == "right":
            return self.cell_matrix[i][j - 1]
        if direction == "bottom":
            return self.cell_matrix[i - 1][j]
        if direction == "left":
            return self.cell_matrix[i][j + 1]

    def get_cell_neighbors(self, i: int, j: int):
        if i - 1 >= 0:
            neighbor_top = self.cell_matrix[i - 1][j]
        else:
            neighbor_top = None

        if j + 1 <= self.num_columns - 1:
            neighbor_right = self.cell_matrix[i][j + 1]
        else:
            neighbor_right = None

        if i + 1 <= self.num_rows - 1:
            neighbor_bottom = self.cell_matrix[i + 1][j]
        else:
            neighbor_bottom = None

        if j - 1 >= 0:
            neighbor_left = self.cell_matrix[i][j - 1]
        else:
            neighbor_left = None

        return {
            "top": neighbor_top,
            "right": neighbor_right,
            "bottom": neighbor_bottom,
            "left": neighbor_left,
        }
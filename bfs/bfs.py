from graphics import *
from cell import *
import time

class BFS:
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

    def search(self, start_i: int, start_j: int, sleep_time: int, show_numbers: bool):
        to_search = [self.cell_matrix[start_i][start_j]]
        search_num = 1

        while to_search:
            current_cell = to_search.pop(0)
            current_cell.searched = True
            current_cell.draw()
            self.parent.redraw()
            time.sleep(sleep_time)

            neighbors = self.get_cell_neighbors(current_cell.i, current_cell.j)
            neighbors_to_search = [v for v in neighbors.values() if (
                v 
                and v.searched == False 
                and v not in to_search
            )]
            
            if show_numbers:
                for neighbor in neighbors_to_search:
                    neighbor.search_num_text = Text(self.parent, neighbor.center, str(search_num))
                    neighbor.search_num_text.draw("black", 16)
                    self.parent.redraw()
                    time.sleep(sleep_time)
                    search_num += 1

            to_search.extend(neighbors_to_search)

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
from common.graphics import *
from common.cell_matrix import *
import random
import time

class DFSMatrix(CellMatrix):
    def search(self, start_i: int, start_j: int, sleep_time: float, is_random: bool, seed):
        self.start_i = start_i
        self.start_j = start_j
        self.sleep_time = sleep_time
        self.is_random = is_random
        if seed is not None:
            random.seed(seed)
        self.search_r(self.cell_matrix[start_i][start_j])

    def search_r(self, current_cell: Cell, direction: str = None):
        first_pass = True
        while True:
            current_cell.searched = True
            current_cell.draw(self.window, self.cell_size)
            if current_cell.i == self.start_i and current_cell.j == self.start_j:
                start_end_point = Circle()
                start_end_point.draw(self.window, current_cell.center, 10, "lime green")
            if direction and first_pass:
                previous_cell = self.get_previous_cell(current_cell.i, current_cell.j, direction)
                track_up_stack = SolidLine()
                track_up_stack.draw(self.window, current_cell.center, previous_cell.center)
            self.window.redraw()
            time.sleep(self.sleep_time)

            neighbors = self.get_cell_neighbors(current_cell.i, current_cell.j)
            to_search = [k for k, v in neighbors.items() if v and v.searched == False]
            if not to_search:
                if first_pass:
                    current_cell.draw(self.window, self.cell_size)
                    self.window.redraw()
                return
            
            if not first_pass:
                breadth_marker = Circle()
                breadth_marker.draw(self.window, current_cell.center, 10)
                self.window.redraw()

            if self.is_random:
                direction = random.choice(to_search)
            else:
                direction = to_search[0]

            if direction == "top":
                self.search_r(self.cell_matrix[current_cell.i - 1][current_cell.j], direction)
            if direction == "right":
                self.search_r(self.cell_matrix[current_cell.i][current_cell.j + 1], direction)
            if direction == "bottom":
                self.search_r(self.cell_matrix[current_cell.i + 1][current_cell.j], direction)
            if direction == "left":
                self.search_r(self.cell_matrix[current_cell.i][current_cell.j - 1], direction)
                
            first_pass = False

    def get_previous_cell(self, i: int, j: int, direction: str) -> Cell:
        if direction == "top":
            return self.cell_matrix[i + 1][j]
        if direction == "right":
            return self.cell_matrix[i][j - 1]
        if direction == "bottom":
            return self.cell_matrix[i - 1][j]
        if direction == "left":
            return self.cell_matrix[i][j + 1]

    def get_cell_neighbors(self, i: int, j: int) -> dict:
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
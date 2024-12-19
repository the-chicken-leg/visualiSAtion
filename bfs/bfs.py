import os, sys
sys.path.insert(0, os.path.join(os.getcwd()))

from graphics import *
from cell_matrix import *
import time

class BFS(CellMatrix):
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
                    neighbor.search_num_text.draw()
                    self.parent.redraw()
                    time.sleep(sleep_time)
                    search_num += 1

            to_search.extend(neighbors_to_search)

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
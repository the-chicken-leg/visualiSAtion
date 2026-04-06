from .breadth_first_search_matrix import BFSMatrix
from common.graphics import Window

def run_breadth_first_search():
    # tuneables
    window_width = 800
    window_height = 800
    cell_size = 50
    smooth_cell_creation = True
    start_i = 7
    start_j = 7
    sleep_time = 0.05
    show_numbers = True

    window = Window(window_width, window_height)
    bfs_matrix = BFSMatrix(window, cell_size, smooth_cell_creation)
    bfs_matrix.search(start_i, start_j, sleep_time, show_numbers)
    window.wait_for_close()

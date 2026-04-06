import sys

from .depth_first_search_matrix import DFSMatrix
from common import graphics as gr

def run_depth_first_search():
    # tuneables
    window_width = 800
    window_height = 800
    cell_size = 50
    smooth_cell_creation = True
    start_i = 7
    start_j = 7
    sleep_time = 0.05
    is_random = True
    seed = None         # ignored if is_random is False

    sys.setrecursionlimit(10000)
    window = gr.Window(window_width, window_height)
    dfs_matrix = DFSMatrix(window, cell_size, smooth_cell_creation)
    dfs_matrix.search(start_i, start_j, sleep_time, is_random, seed)
    window.wait_for_close()

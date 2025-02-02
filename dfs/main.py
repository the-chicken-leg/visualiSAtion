import os, sys
sys.path.insert(1, os.path.join(os.getcwd()))
sys.path.insert(1, os.path.join(os.getcwd(), "common"))

from common.graphics import Window
from dfs_matrix import DFSMatrix

def main():
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
    window = Window(window_width, window_height)
    dfs_matrix = DFSMatrix(window, cell_size, smooth_cell_creation)
    dfs_matrix.search(start_i, start_j, sleep_time, is_random, seed)
    window.wait_for_close()

if __name__ == "__main__":
    main()
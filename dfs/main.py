import os, sys
sys.path.insert(0, os.path.join(os.getcwd()))

from graphics import Window
from dfs import DFS

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
    seed = None

    sys.setrecursionlimit(10000)
    window = Window(window_width, window_height)
    dfs_matrix = DFS(window, cell_size, smooth_cell_creation)
    dfs_matrix.search(start_i, start_j, sleep_time, is_random, seed)
    window.wait_for_close()

main()
from graphics import Window
from dfs import DFS
import sys

def main():
    # tuneables
    window_width = 800
    window_height = 600
    cell_size = 50
    start_i = 0
    start_j = 0
    sleep_time = 0.1
    seed = None

    window = Window(window_width, window_height)
    cell_matrix = DFS(window, cell_size)
    cell_matrix.search(start_i, start_j, sleep_time, seed)
    window.wait_for_close()

main()
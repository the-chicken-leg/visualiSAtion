from graphics import Window
from bfs import BFS

def main():
    # tuneables
    window_width = 800
    window_height = 600
    cell_size = 100
    start_i = 0
    start_j = 0
    sleep_time = 0.1
    seed = None

    window = Window(window_width, window_height)
    cell_matrix = BFS(window, cell_size)
    cell_matrix.search(start_i, start_j, sleep_time, seed)
    window.wait_for_close()

main()




# if direction == "top":
#     i -= 1
# if direction == "right":
#     j += 1
# if direction == "bottom":
#     i += 1
# if direction == "left":
#     j -= 1
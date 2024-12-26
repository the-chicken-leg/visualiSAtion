import os, sys
sys.path.insert(1, os.path.join(os.getcwd()))

from common.graphics import Window
from rb_tree import RBTree

def main():
    # tuneables
    window_width = 1500
    window_height = 500
    insertion_type = "random"   # "ascending", "descending", "random", or "custom"
    num_nodes = 15              # ignored if "custom" insertion_type
    custom_insertion = [5, 1, 5, 8, 6, 4, 5, 10, 3, 9]      # ignored if not "custom" insertion_type
    step_manually = False        # can navigate with right and left arrow keys
    sleep_time = 1

    window = Window(window_width, window_height)
    RBTree(window, insertion_type, num_nodes, custom_insertion, step_manually, sleep_time)
    window.wait_for_close()

if __name__ == "__main__":
    main()
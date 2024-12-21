import os, sys
sys.path.insert(1, os.path.join(os.getcwd()))

from common.graphics import Window
from snackshack_queue import SnackshackQueue

def main():
    # tuneables
    window_width = 800
    window_height = 800
    starting_num_patrons = 15
    patron_fatbody_index = 25
    push_pop_ratio = 0.5
    sleep_time = 0.3
    stop_when_empty = True

    window = Window(window_width, window_height)
    snackshack_queue = SnackshackQueue(window, starting_num_patrons, patron_fatbody_index)
    input("Press Enter to continue")
    snackshack_queue.simulate(push_pop_ratio, sleep_time, stop_when_empty)
    window.wait_for_close()

if __name__ == "__main__":
    main()
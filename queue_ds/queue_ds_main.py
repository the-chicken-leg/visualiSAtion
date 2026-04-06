from .snackshack_queue import SnackshackQueue
from common.graphics import Window

def run_queue_ds():
    # tuneables
    window_width = 800
    window_height = 800
    starting_num_patrons = 15
    push_pop_ratio = 0.5
    stop_when_empty = True
    patron_fatbody_width = 25
    sleep_time = 0.3

    window = Window(window_width, window_height)
    snackshack_queue = SnackshackQueue(starting_num_patrons, push_pop_ratio, stop_when_empty)
    snackshack_queue.draw_in_window(window, patron_fatbody_width, sleep_time)
    window.wait_for_close()

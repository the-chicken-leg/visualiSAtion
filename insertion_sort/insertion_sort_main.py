from .insertion_sort_things import InsertionSortThings
from common.graphics import Window

def run_insertion_sort():
    # tuneables
    window_width = 800
    window_height = 800
    thing_width = 20
    value_order = "random"    # "ascending", "descending", "random", or "custom"
    custom_values = [100, 700, 200, 600, 300, 500, 400, 150, 50, 250, 650, 350, 550, 450]    # ignored if not "custom" value_order, values measured in pixels, min=50, max=window_height-100
    sleep_time = 0.06

    window = Window(window_width, window_height)
    insertionsort_things = InsertionSortThings(window, thing_width, value_order, custom_values)
    insertionsort_things.sort(sleep_time)
    window.wait_for_close()

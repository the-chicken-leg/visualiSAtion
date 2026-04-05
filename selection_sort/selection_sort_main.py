from .selection_sort_things import SelectionSortThings
from common.graphics import Window

def run_selection_sort():
    # tuneables
    window_width = 800
    window_height = 800
    thing_width = 20
    value_order = "random"    # "ascending", "descending", "random", or "custom"
    custom_values = [100, 700, 200, 600, 300, 500, 400, 150, 50, 250, 650, 350, 550, 450]    # ignored if not "custom" value_order, values measured in pixels, min=50, max=window_height-100
    sleep_time = 0.04

    window = Window(window_width, window_height)
    selectionsort_things = SelectionSortThings(window, thing_width, value_order, custom_values)
    selectionsort_things.sort(sleep_time)
    window.wait_for_close()

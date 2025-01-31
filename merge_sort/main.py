import os, sys
sys.path.insert(1, os.path.join(os.getcwd()))
sys.path.insert(1, os.path.join(os.getcwd(), "common"))

from common.graphics import Window
from mergesort_things import MergesortThings

def main():
    # tuneables
    window_width = 800
    window_height = 800
    thing_width = 20
    value_order = "random"    # "ascending", "descending", "random", or "custom"
    custom_values = [100, 700, 200, 600, 300, 500, 400, 150, 50, 250, 650, 350, 550, 450]    # ignored if not "custom" value_order, values measured in pixels, min=50, max=window_height-100
    sleep_time = 0.1

    window = Window(window_width, window_height)
    mergesort_things = MergesortThings(window, thing_width, value_order, custom_values)
    mergesort_things.sort(sleep_time)
    window.wait_for_close()

if __name__ == "__main__":
    main()
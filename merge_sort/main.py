import os, sys
sys.path.insert(1, os.path.join(os.getcwd()))
sys.path.insert(1, os.path.join(os.getcwd(), "common"))

from common.graphics import Window
from merge_sort_things import MergeSortThings

def main():
    # tuneables
    window_width = 800
    window_height = 800
    starting_num_things = 29
    thing_width = 25
    sleep_time = 0.05

    window = Window(window_width, window_height)
    merge_sort_things = MergeSortThings(window, starting_num_things, thing_width)
    merge_sort_things.sort(sleep_time)
    merge_sort_things.remove_highlighter()
    window.wait_for_close()

if __name__ == "__main__":
    main()
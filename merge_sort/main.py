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
    sleep_time = 0.1

    window = Window(window_width, window_height)
    mergesort_things = MergesortThings(window, thing_width)
    mergesort_things.sort(sleep_time)
    window.wait_for_close()

if __name__ == "__main__":
    main()
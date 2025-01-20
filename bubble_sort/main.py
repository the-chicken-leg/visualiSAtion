import os, sys
sys.path.insert(1, os.path.join(os.getcwd()))
sys.path.insert(1, os.path.join(os.getcwd(), "common"))

from common.graphics import Window
from bubbles import Bubbles

def main():
    # tuneables
    window_width = 800
    window_height = 800
    thing_width = 20
    sleep_time = 0.05

    window = Window(window_width, window_height)
    bubbles = Bubbles(window, thing_width)
    bubbles.sort(sleep_time)
    bubbles.remove_highlighter()
    window.wait_for_close()

if __name__ == "__main__":
    main()
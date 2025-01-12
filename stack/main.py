import os, sys
sys.path.insert(1, os.path.join(os.getcwd()))

from common.graphics import Window
from dirty_dishes import DirtyDishes

def main():
    # tuneables
    window_width = 800
    window_height = 800
    starting_num_dishes = 15
    push_pop_ratio = 0.75
    stop_when_empty = True
    single_dish_height = 25
    sleep_time = 0.2

    window = Window(window_width, window_height)
    dirty_dishes = DirtyDishes(starting_num_dishes, push_pop_ratio, stop_when_empty)
    dirty_dishes.draw_in_window(window, single_dish_height, sleep_time)
    window.wait_for_close()

if __name__ == "__main__":
    main()
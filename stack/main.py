import os, sys
sys.path.insert(1, os.path.join(os.getcwd()))

from common.graphics import Window
from dirty_dishes import DirtyDishes

def main():
    # tuneables
    window_width = 800
    window_height = 800
    starting_num_dishes = 15
    single_dish_height = 25
    push_pop_ratio = 0.75
    sleep_time = 0.2
    stop_when_empty = True

    window = Window(window_width, window_height)
    dirty_dishes = DirtyDishes(window, starting_num_dishes, single_dish_height)
    dirty_dishes.simulate(push_pop_ratio, sleep_time, stop_when_empty)
    window.wait_for_close()

if __name__ == "__main__":
    main()
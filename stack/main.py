import os, sys
sys.path.insert(0, os.path.join(os.getcwd()))

from graphics import Window
from dirty_dishes import DirtyDishes

def main():
    # tuneables
    window_width = 800
    window_height = 800
    starting_num_dishes = 15
    single_dish_height = 25
    push_pop_ratio = 0.75
    sleep_time = 0.2

    window = Window(window_width, window_height)
    dirty_dishes = DirtyDishes(window, starting_num_dishes, single_dish_height)
    dirty_dishes.simulate(push_pop_ratio, sleep_time)
    window.wait_for_close()

main()
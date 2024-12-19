import os, sys
sys.path.insert(0, os.path.join(os.getcwd()))

from graphics import Window
from dirty_dishes import DirtyDishes

def main():
    # tuneables
    window_width = 400
    window_height = 800
    single_dish_height = 25
    smooth_dishes = True
    push_pop_ratio = 1
    sleep_time = 0.1

    window = Window(window_width, window_height)
    dirty_dishes = DirtyDishes(window, single_dish_height, smooth_dishes)
    # dirty_dishes.simulate(push_pop_ratio, sleep_time)
    window.wait_for_close()

main()
from sort_thing import *
import time
import random

class ThingsToSort:
    def __init__(self, window: Window, starting_num_things: int, thing_width: int):
        self.window = window
        self.thing_width = thing_width

        self.things_to_sort = [
            SortThing(random.randint(50, window.height - 100)) for i in range(starting_num_things)
        ]

        # self.things_to_sort = [
        #     SortThing(674), SortThing(621), SortThing(395), SortThing(127), SortThing(329), SortThing(530)
        # ]

        for i, sort_thing in enumerate(self.things_to_sort):
            self.middle_index = starting_num_things // 2
            center_x = window.width / 2 + (i - self.middle_index) * thing_width
            sort_thing.draw(window, center_x, thing_width)
            window.redraw()
            time.sleep(0.05)
from sort_thing import *
import time
import random

class ThingsToSort:
    def __init__(self, window: Window, thing_width: int):
        self.window = window
        self.thing_width = thing_width

        num_things = (window.width - 100) // self.thing_width

        self.things_to_sort = [
            SortThing(random.randint(50, window.height - 100)) for i in range(num_things)
        ]

        for i, sort_thing in enumerate(self.things_to_sort):
            self.middle_index = num_things // 2
            center_x = window.width / 2 + (i - self.middle_index) * self.thing_width
            sort_thing.draw(window, center_x, self.thing_width)
            window.redraw()
            time.sleep(0.05)

    def delete_sort_markers(self):
        self.window.canvas.delete("sort_indicator", "sort_highlighter")

    def redraw_sort_markers(self, i: int, center_x_i: float):
        self.delete_sort_markers()
        sort_indicator = SortIndicator()
        sort_indicator.draw(self.window, center_x_i)
        sort_highlighter = SortHighlighter(self.things_to_sort[i])
        sort_highlighter.draw(self.window, center_x_i, self.thing_width)
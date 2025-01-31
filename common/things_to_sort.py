from sort_thing import *
import time
import random

class ThingsToSort:
    def __init__(self, window: Window, thing_width: int, data_order: str, custom_values = list):
        self.window = window
        self.thing_width = thing_width

        if data_order == "ascending":
            num_things = (window.width - 100) // self.thing_width
            self.things_to_sort = sorted(
                [SortThing(random.randint(50, window.height - 100)) for i in range(num_things)],
            )
        elif data_order == "descending":
            num_things = (window.width - 100) // self.thing_width
            self.things_to_sort = sorted(
                [SortThing(random.randint(50, window.height - 100)) for i in range(num_things)],
                reverse=True,
            )
        elif data_order == "random":
            num_things = (window.width - 100) // self.thing_width
            self.things_to_sort = [
                SortThing(random.randint(50, window.height - 100)) for i in range(num_things)
            ]
        elif data_order == "custom":
            num_things = len(custom_values)
            self.things_to_sort = [SortThing(custom_value) for custom_value in custom_values]
            
        for i, sort_thing in enumerate(self.things_to_sort):
            self.middle_index = num_things // 2
            center_x = window.width / 2 + (i - self.middle_index) * self.thing_width
            sort_thing.draw(window, center_x, self.thing_width)
            window.redraw()
            time.sleep(0.05)

    def delete_all_markers(self):
        self.window.canvas.delete(
            "sort_indicator",
            "sort_highlighter_red",
            "sort_highlighter_cyan",
            "sort_highlighter_yellow",
        )
        
    def redraw_primary_sort_markers(self, i: int, center_x_i: float):
        self.window.canvas.delete("sort_indicator", "sort_highlighter_red")
        sort_indicator = SortIndicator()
        sort_indicator.draw(self.window, center_x_i)
        sort_highlighter_red = SortHighlighterRed(self.things_to_sort[i])
        sort_highlighter_red.draw(self.window, center_x_i, self.thing_width)

    def redraw_highlighter_cyan(self, i: int, center_x_i: float):
        self.window.canvas.delete("sort_highlighter_cyan")
        sort_highlighter_cyan = SortHighlighterCyan(self.things_to_sort[i])
        sort_highlighter_cyan.draw(self.window, center_x_i, self.thing_width)

    def redraw_highlighter_yellow(self, i: int, center_x_i: float):
        self.window.canvas.delete("sort_highlighter_yellow")
        sort_highlighter_yellow = SortHighlighterYellow(self.things_to_sort[i])
        sort_highlighter_yellow.draw(self.window, center_x_i, self.thing_width)
from sort_thing import *
import time
import random

class ThingsToSort:
    def __init__(self, window: Window, starting_num_things: int, thing_width: int):
        self.window = window
        self.starting_num_things = starting_num_things
        self.thing_width = thing_width

        self.things_to_sort = [
            SortThing(random.randint(50, window.height - 100)) for i in range(starting_num_things)
        ]

        self.draw_initial()

    def draw_initial(self):
        self.window.redraw()
        for i, sort_thing in enumerate(self.things_to_sort):
            self.middle_index = self.starting_num_things // 2
            center_x = self.window.width / 2 + (i - self.middle_index) * self.thing_width
            sort_thing.draw(self.window, center_x, self.thing_width)
            self.window.redraw()
            time.sleep(0.05)

    def bubble_sort(self, sleep_time: int):
        self.sleep_time = sleep_time
        
        swapping = True
        end = len(self.things_to_sort)
        while swapping:
            swapping = False
            for i in range(1, end):
                self.draw_indicator(i)
                if self.things_to_sort[i - 1].value > self.things_to_sort[i].value:
                    temp = self.things_to_sort[i - 1]
                    self.things_to_sort[i - 1] = self.things_to_sort[i]
                    self.things_to_sort[i] = temp
                    swapping = True
                self.draw_after_sort(i)
            end -= 1
        return self.things_to_sort

    def draw_indicator(self, i):
        center_x_i = self.window.width / 2 + (i - self.middle_index) * self.thing_width

        self.window.canvas.delete("indicator")
        sort_indicator = SortIndicator()
        sort_indicator.draw(self.window, center_x_i)

    def draw_after_sort(self, i):
        center_x_i = self.window.width / 2 + (i - self.middle_index) * self.thing_width
        center_x_i_minus = self.window.width / 2 + (i - 1 - self.middle_index) * self.thing_width

        self.window.canvas.delete(self.things_to_sort[i].id)
        self.window.canvas.delete(self.things_to_sort[i - 1].id)
        self.things_to_sort[i].draw(self.window, center_x_i, self.thing_width)
        self.things_to_sort[i - 1].draw(self.window, center_x_i_minus, self.thing_width)
        
        self.window.redraw()
        time.sleep(self.sleep_time)
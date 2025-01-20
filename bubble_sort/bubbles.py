from common.things_to_sort import *

class Bubbles(ThingsToSort):
    def sort(self, sleep_time: float):
        swapping = True
        end = len(self.things_to_sort)
        while swapping:
            swapping = False
            for i in range(1, end):
                if self.things_to_sort[i - 1].value > self.things_to_sort[i].value:
                    temp = self.things_to_sort[i - 1]
                    self.things_to_sort[i - 1] = self.things_to_sort[i]
                    self.things_to_sort[i] = temp
                    swapping = True
                self.draw_after_swap(i)
                self.draw_highlighter(i)
                self.window.redraw()
                time.sleep(sleep_time)
            end -= 1

    def draw_after_swap(self, i: int):
        center_x_i = self.window.width / 2 + (i - self.middle_index) * self.thing_width
        center_x_i_minus = self.window.width / 2 + (i - 1 - self.middle_index) * self.thing_width

        self.window.canvas.delete(self.things_to_sort[i].id)
        self.window.canvas.delete(self.things_to_sort[i - 1].id)
        self.things_to_sort[i].draw(self.window, center_x_i, self.thing_width)
        self.things_to_sort[i - 1].draw(self.window, center_x_i_minus, self.thing_width)

    def draw_highlighter(self, i: int):
        center_x_i = self.window.width / 2 + (i - self.middle_index) * self.thing_width

        self.window.canvas.delete("sort_indicator")
        sort_indicator = SortIndicator()
        sort_indicator.draw(self.window, center_x_i)

        self.window.canvas.delete("sort_highlighter")
        sort_highlighter = SortHighlighter(self.things_to_sort[i])
        sort_highlighter.draw(self.window, center_x_i, self.thing_width)

    def remove_highlighter(self):
        self.window.canvas.delete("sort_indicator")
        self.window.canvas.delete("sort_highlighter")        
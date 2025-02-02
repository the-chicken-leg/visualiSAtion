from common.things_to_sort import *

class Bubbles(ThingsToSort):
    def sort(self, sleep_time: float):
        self.sleep_time = sleep_time

        swapping = True
        end = len(self.things_to_sort)
        while swapping:
            swapping = False
            for i in range(1, end):
                if self.things_to_sort[i - 1] > self.things_to_sort[i]:
                    temp = self.things_to_sort[i - 1]
                    self.things_to_sort[i - 1] = self.things_to_sort[i]
                    self.things_to_sort[i] = temp
                    swapping = True
                self.draw_i(i)
            end -= 1
            self.draw_end(end)
        self.delete_all_markers()

    def draw_i(self, i: int):
        self.window.canvas.delete(self.things_to_sort[i].id)
        self.window.canvas.delete(self.things_to_sort[i - 1].id)

        center_x_i = self.calculate_center(i)
        center_x_i_minus = self.calculate_center(i - 1)

        self.things_to_sort[i].draw(self.window, center_x_i, self.thing_width)
        self.things_to_sort[i - 1].draw(self.window, center_x_i_minus, self.thing_width)

        self.draw_primary_sort_markers(i, center_x_i)

        self.window.redraw()
        time.sleep(self.sleep_time)

    def draw_end(self, end: int):
        center_x_end = self.calculate_center(end)
        self.draw_highlighter_yellow(end, center_x_end)
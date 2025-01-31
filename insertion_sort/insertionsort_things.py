from common.things_to_sort import *

class InsertionsortThings(ThingsToSort):
    def sort(self, sleep_time: float):
        self.sleep_time = sleep_time
 
        for i in range(len(self.things_to_sort)):
            j = i
            if not (j > 0 and self.things_to_sort[j - 1] > self.things_to_sort[j]):
                self.draw_i(i)
            while j > 0 and self.things_to_sort[j - 1] > self.things_to_sort[j]:
                self.things_to_sort[j], self.things_to_sort[j - 1] = self.things_to_sort[j - 1], self.things_to_sort[j]
                self.draw(i, j)
                j -= 1
        self.delete_all_markers()

    def draw_i(self, i: int):
        center_x_i = self.window.width / 2 + (i - self.middle_index) * self.thing_width
        self.redraw_highlighter_yellow(i, center_x_i)

        self.window.redraw()
        time.sleep(self.sleep_time)

    def draw(self, i: int, j: int):
        self.window.canvas.delete(self.things_to_sort[j].id)
        self.window.canvas.delete(self.things_to_sort[j - 1].id)
        
        center_x_j = self.window.width / 2 + (j - self.middle_index) * self.thing_width
        center_x_j_minus = self.window.width / 2 + (j - 1 - self.middle_index) * self.thing_width
        center_x_i = self.window.width / 2 + (i - self.middle_index) * self.thing_width

        self.things_to_sort[j].draw(self.window, center_x_j, self.thing_width)
        self.things_to_sort[j - 1].draw(self.window, center_x_j_minus, self.thing_width)

        self.redraw_primary_sort_markers(j - 1, center_x_j_minus)
        self.redraw_highlighter_yellow(i, center_x_i)

        self.window.redraw()
        time.sleep(self.sleep_time)
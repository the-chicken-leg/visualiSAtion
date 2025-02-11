from common.things_to_sort import *

class SelectionsortThings(ThingsToSort):
    def sort(self, sleep_time: float):
        self.sleep_time = sleep_time

        for i in range(len(self.things_to_sort)):
            self.draw_i(i)
            smallest_index = i
            for j in range(i + 1, len(self.things_to_sort)):
                self.draw_j(j)
                if self.things_to_sort[j] < self.things_to_sort[smallest_index]:
                    smallest_index = j
                    self.draw_smallest_index(smallest_index)
            self.things_to_sort[i], self.things_to_sort[smallest_index] = self.things_to_sort[smallest_index], self.things_to_sort[i]
            self.draw_swap(i, smallest_index)
        self.delete_all_markers()

    def draw_i(self, i: int):
        center_x_i = self.calculate_center(i)
        self.draw_highlighter_yellow(i, center_x_i)

    def draw_j(self, j: int):
        center_x_j = self.calculate_center(j)
        self.draw_primary_sort_markers(j, center_x_j)
        self.window.redraw()
        time.sleep(self.sleep_time)

    def draw_smallest_index(self, smallest_index: int):
        center_x_smallest_index = self.calculate_center(smallest_index)
        self.draw_highlighter_cyan(smallest_index, center_x_smallest_index)

    def draw_swap(self, i: int, smallest_index: int):
        self.window.canvas.delete(self.things_to_sort[i].id)
        self.window.canvas.delete(self.things_to_sort[smallest_index].id)

        center_x_i = self.calculate_center(i)
        center_x_smallest_index = self.calculate_center(smallest_index)
        
        self.things_to_sort[i].draw(self.window, center_x_i, self.thing_width)
        self.things_to_sort[smallest_index].draw(self.window, center_x_smallest_index, self.thing_width)
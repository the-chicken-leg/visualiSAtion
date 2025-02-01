from common.things_to_sort import *

class QuicksortThings(ThingsToSort):
    def sort(self, sleep_time: float):
        self.sleep_time = sleep_time
        self.quick_sort_r(self.things_to_sort, 0, len(self.things_to_sort) - 1)
        self.delete_all_markers()
        
    def quick_sort_r(self, list_to_sort: list, low: int, high: int):
        if low < high:
            sorted_index = self.quick_sort(list_to_sort, low, high)
            self.quick_sort_r(list_to_sort, low, sorted_index - 1)
            self.quick_sort_r(list_to_sort, sorted_index + 1, high)

    def quick_sort(self, list_to_sort: list, low: int, high: int):
        pivot = list_to_sort[high]
        i = low
        for j in range(low, high):
            self.draw_markers(i, j, high)
            if list_to_sort[j] < pivot:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
                if i != j:
                    self.draw_j_swap(list_to_sort, i, j, high)
                i += 1
        list_to_sort[i], list_to_sort[high] = list_to_sort[high], list_to_sort[i]
        if i != high:
            self.draw_pivot_swap(list_to_sort, i, j, high)
        return i
    
    def draw_markers(self, i: int, j: int, high: int):
        center_x_high = self.window.width / 2 + (high - self.middle_index) * self.thing_width
        center_x_i = self.window.width / 2 + (i - self.middle_index) * self.thing_width
        center_x_j = self.window.width / 2 + (j - self.middle_index) * self.thing_width

        self.draw_highlighter_yellow(high, center_x_high)
        self.draw_highlighter_cyan(i, center_x_i)
        self.draw_primary_sort_markers(j, center_x_j)

        self.window.redraw()
        time.sleep(self.sleep_time)

    def draw_j_swap(self, list_to_sort: list, i: int, j: int, high: int):
        self.window.canvas.delete(list_to_sort[i].id)
        self.window.canvas.delete(list_to_sort[j].id)

        center_x_i = self.window.width / 2 + (i - self.middle_index) * self.thing_width
        center_x_j = self.window.width / 2 + (j - self.middle_index) * self.thing_width

        list_to_sort[i].draw(self.window, center_x_i, self.thing_width)
        list_to_sort[j].draw(self.window, center_x_j, self.thing_width)

        self.draw_markers(i, j, high)

    def draw_pivot_swap(self, list_to_sort: list, i: int, j: int, high: int):
        self.window.canvas.delete(list_to_sort[i].id)
        self.window.canvas.delete(list_to_sort[high].id)

        center_x_i = self.window.width / 2 + (i - self.middle_index) * self.thing_width
        center_x_pivot = self.window.width / 2 + (high - self.middle_index) * self.thing_width

        list_to_sort[i].draw(self.window, center_x_i, self.thing_width)
        list_to_sort[high].draw(self.window, center_x_pivot, self.thing_width)

        self.draw_markers(i, j, high)
from common.things_to_sort import *

class MergeSortThings(ThingsToSort):
    def sort(self, sleep_time: float):
        self.sleep_time = sleep_time
        self.k = 0
        self.merge_sort_r(self.things_to_sort)

    def merge_sort_r(self, list_to_sort: list):
        if len(list_to_sort) < 2:
            return list_to_sort
        if len(list_to_sort) % 2 == 0:
            sorted_left_side = self.merge_sort_r(list_to_sort[:len(list_to_sort) // 2])
            sorted_right_side = self.merge_sort_r(list_to_sort[len(list_to_sort) // 2:])
        else:
            sorted_left_side = self.merge_sort_r(list_to_sort[:len(list_to_sort) // 2 + 1])
            sorted_right_side = self.merge_sort_r(list_to_sort[len(list_to_sort) // 2 + 1:])
        return self.merge_sort(sorted_left_side, sorted_right_side)
    
    def merge_sort(self, sorted_left_side: list, sorted_right_side: list):
        sorted_combined = []
        i = 0
        j = 0
        while i < len(sorted_left_side) and j < len(sorted_right_side):
            if sorted_left_side[i].value <= sorted_right_side[j].value:
                sorted_combined.append(sorted_left_side[i])
                i += 1
            else:
                sorted_combined.append(sorted_right_side[j])
                j += 1
        while i < len(sorted_left_side):
            sorted_combined.append(sorted_left_side[i])
            i += 1
        while j < len(sorted_right_side):
            sorted_combined.append(sorted_right_side[j])
            j += 1
        self.draw(sorted_combined)
        return sorted_combined

    def draw(self, sorted_combined: list):
        if len(sorted_combined) == 2:
            self.k += 2
        if len(sorted_combined) == 3:
            self.k += 1
        old_canvas_ids = self.get_ids(self.things_to_sort)

        for index in range(self.k - len(sorted_combined), self.k):
            self.window.canvas.delete(old_canvas_ids[index])
            
            center_x_i = self.window.width / 2 + (index - self.middle_index) * self.thing_width
            self.things_to_sort[index] = sorted_combined[index - self.k]
            self.things_to_sort[index].draw(self.window, center_x_i, self.thing_width)

            self.window.canvas.delete("sort_indicator")
            sort_indicator = SortIndicator()
            sort_indicator.draw(self.window, center_x_i)

            self.window.canvas.delete("sort_highlighter")
            sort_highlighter = SortHighlighter(self.things_to_sort[index])
            sort_highlighter.draw(self.window, center_x_i, self.thing_width)                    

            self.window.redraw()
            time.sleep(self.sleep_time)

    def get_ids(self, list_of_sort_things: list):
        ids = []
        for sort_thing in list_of_sort_things:
            ids.append(sort_thing.id)
        return ids
    
    def get_values(self, list_of_sort_things: list):
        values = []
        for sort_thing in list_of_sort_things:
            values.append(sort_thing.value)
        return values
    
    def remove_highlighter(self):
        self.window.canvas.delete("sort_indicator")
        self.window.canvas.delete("sort_highlighter")
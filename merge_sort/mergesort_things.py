from common.things_to_sort import *

class MergesortThings(ThingsToSort):
    def sort(self, sleep_time: float):
        self.sleep_time = sleep_time
        self.k = 0
        self.merge_sort_r(self.things_to_sort)
        self.delete_all_markers()
        
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
            if sorted_left_side[i] <= sorted_right_side[j]:
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
        elif len(sorted_combined) == 3:
            self.k += 1
        old_canvas_ids = [sort_thing.id for sort_thing in self.things_to_sort]

        for index in range(self.k - len(sorted_combined), self.k):
            self.window.canvas.delete(old_canvas_ids[index])
            
            center_x_index = self.calculate_center(index)
            self.things_to_sort[index] = sorted_combined[index - self.k]
            self.things_to_sort[index].draw(self.window, center_x_index, self.thing_width)

            self.draw_primary_sort_markers(index, center_x_index)
            
            self.window.redraw()
            time.sleep(self.sleep_time)
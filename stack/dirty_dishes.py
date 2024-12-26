from dish import *
import random

class DirtyDishes:
    def __init__(self, starting_num_dishes: int, push_pop_ratio: float, stop_when_empty: bool):
        self.push_pop_ratio = push_pop_ratio
        self.stop_when_empty = stop_when_empty

        self.dirty_dishes = [Dish() for i in range(starting_num_dishes)]

    def draw_in_window(self, window: Window, single_dish_height: int, sleep_time: float):
        self.window = window
        self.single_dish_height = single_dish_height
        self.sleep_time = sleep_time

        self.center_x = window.width / 2
        for i, dirty_dish in enumerate(self.dirty_dishes):
            center_y = window.height - 25 - (0.5 * single_dish_height) - (i * single_dish_height)
            dirty_dish.draw(window, Point(self.center_x, center_y), single_dish_height)
        window.redraw()
        time.sleep(sleep_time)

        self.simulate()

    def simulate(self):
        while True:
            push_or_pop = self.get_push_or_pop(self.push_pop_ratio)
            if push_or_pop == "push":
                self.push()
            elif push_or_pop == "pop":
                self.pop()
            if self.stop_when_empty and not self.dirty_dishes:
                break
            time.sleep(self.sleep_time)

    def get_push_or_pop(self, push_pop_ratio: float) -> str:
        prob_push = push_pop_ratio / (push_pop_ratio + 1)
        rando = random.random()
        if rando <= prob_push:
            return "push"
        return "pop"
        
    def push(self):
        new_dish = Dish()
        self.dirty_dishes.append(new_dish)

        num_dishes = len(self.dirty_dishes) - 1
        center_y = self.window.height - 25 - (0.5 * self.single_dish_height) - (num_dishes * self.single_dish_height)
        new_dish.draw(self.window, Point(self.center_x, center_y), self.single_dish_height)
        self.window.redraw()

    def pop(self):
        if not self.dirty_dishes:
            return
        clean_this_dish = self.dirty_dishes.pop()
        self.window.canvas.delete(clean_this_dish.id)
        self.window.redraw()
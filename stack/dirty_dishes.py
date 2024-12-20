import os, sys
sys.path.insert(0, os.path.join(os.getcwd()))

from graphics import *
from dish import *
import random

class DirtyDishes:
    def __init__(self, parent: Window, starting_num_dishes: int, single_dish_height: int):
        self.parent = parent
        self.starting_num_dishes = starting_num_dishes
        self.single_dish_height = single_dish_height

        self.create_dirty_dishes()

    def create_dirty_dishes(self):
        self.dirty_dishes = []
        self.center_x = self.parent.width / 2
        for i in range(self.starting_num_dishes):
            center_y = self.parent.height - 25 - (0.5 * self.single_dish_height) - (i * self.single_dish_height)
            self.dirty_dishes.append(
                Dish(
                    self.parent,
                    Point(self.center_x, center_y),
                    self.single_dish_height,
                )
            )

        self.draw_dirty_dishes()

    def draw_dirty_dishes(self):
        for dirty_dish in self.dirty_dishes:
            dirty_dish.draw()
            self.parent.redraw()

    def simulate(self, push_pop_ratio: float, sleep_time: float, stop_when_empty: bool):
        while True:
            push_or_pop = self.get_push_or_pop(push_pop_ratio)
            if push_or_pop == "push":
                self.push()
            elif push_or_pop == "pop":
                self.pop()
            if stop_when_empty and not self.dirty_dishes:
                break
            time.sleep(sleep_time)

    def get_push_or_pop(self, push_pop_ratio: float) -> str:
        prob_push = push_pop_ratio / (push_pop_ratio + 1)
        rando = random.random()
        if rando <= prob_push:
            return "push"
        return "pop"
        
    def push(self):
        num_dishes = len(self.dirty_dishes)
        center_y = self.parent.height - 25 - (0.5 * self.single_dish_height) - (num_dishes * self.single_dish_height)
        new_dish = Dish(
            self.parent,
            Point(self.center_x, center_y),
            self.single_dish_height,
        )
        self.dirty_dishes.append(new_dish)
        new_dish.draw()
        self.parent.redraw()

    def pop(self):
        if not self.dirty_dishes:
            return
        clean_this_dish = self.dirty_dishes.pop()
        self.parent.canvas.delete(clean_this_dish.id)
        self.parent.redraw()
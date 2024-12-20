import os, sys
sys.path.insert(0, os.path.join(os.getcwd()))

from graphics import *
from dish import Dish

class DirtyDishes:
    def __init__(self, parent: Window, starting_num_dishes: int, single_dish_height: int, smooth_dishes: bool):
        self.parent = parent
        self.starting_num_dishes = starting_num_dishes
        self.single_dish_height = single_dish_height
        self.smooth_dishes = smooth_dishes

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
                    i,
                )
            )

        self.draw_dirty_dishes()

    def draw_dirty_dishes(self):
        for dirty_dish in self.dirty_dishes:
            dirty_dish.draw()
            self.parent.redraw()
            if self.smooth_dishes:
                time.sleep(0.1)

    def push(self):
        i = len(self.dirty_dishes)
        center_y = self.parent.height - 25 - (0.5 * self.single_dish_height) - (i * self.single_dish_height)
        new_dish = Dish(
            self.parent,
            Point(self.center_x, center_y),
            self.single_dish_height,
            i,
        )
        self.dirty_dishes.append(new_dish)
        new_dish.draw()
        self.parent.redraw()
        if self.smooth_dishes:
            time.sleep(0.1)

    def pop(self):
        if not self.dirty_dishes:
            return
        dish_to_clean = self.dirty_dishes.pop()
        self.parent.canvas.delete(dish_to_clean)
        # delete from canvas
        # redraw canvas



    def simulate():
        pass
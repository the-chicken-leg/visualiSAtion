import os, sys
sys.path.insert(0, os.path.join(os.getcwd()))

from graphics import *
from dish import Dish

class DirtyDishes:
    def __init__(self, parent: Window, single_dish_height: int, smooth_dishes: bool):
        self.parent = parent
        self.single_dish_height = single_dish_height
        self.smooth_dishes = smooth_dishes

        self.create_dirty_dishes()

    def create_dirty_dishes(self):
        self.dirty_dishes = []
        center_x = self.parent.width / 2
        for i in range(20):     # make starting_dishes parameter
            center_y = self.parent.height - 25 - (0.5 * self.single_dish_height) - (i * self.single_dish_height)
            self.dirty_dishes.append(
                Dish(
                    self.parent,
                    Point(center_x, center_y),
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
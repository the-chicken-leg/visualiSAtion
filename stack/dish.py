import os, sys
sys.path.insert(0, os.path.join(os.getcwd()))

from graphics import *
import random

class Dish(Rectangle):
    def __init__(self, parent: Window, center: Point, y_length: int, i: int):
        x_length = parent.width - (parent.width * 0.5)
        super().__init__(parent, center, x_length, y_length)
        self.i = i

    def draw(self):
        red = "%02x" % random.randint(0, 255)
        green = "%02x" % random.randint(0, 255)
        blue = "%02x" % random.randint(0, 255)
        color = "#" + red + green + blue
        super().draw(color)
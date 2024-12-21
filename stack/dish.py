from common.graphics import *
import random

class Dish(Rectangle):
    def __init__(self, parent: Window, center: Point, single_dish_height: int):
        x_length = parent.width - (parent.width * 0.5)
        super().__init__(parent, center, x_length, single_dish_height)

    def draw(self):
        red = "%02x" % random.randint(0, 255)
        green = "%02x" % random.randint(0, 255)
        blue = "%02x" % random.randint(0, 255)
        fill_color = "#" + red + green + blue
        super().draw(fill_color)
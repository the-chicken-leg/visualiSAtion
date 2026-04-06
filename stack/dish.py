import random

from common import graphics as gr

class Dish(gr.Rectangle):
    def draw(self, window: gr.Window, center: gr.Point, single_dish_height: int):
        x_length = window.width - (window.width * 0.5)

        red = "%02x" % random.randint(0, 255)
        green = "%02x" % random.randint(0, 255)
        blue = "%02x" % random.randint(0, 255)
        fill_color = "#" + red + green + blue
        
        super().draw(window, center, x_length, single_dish_height, fill_color)

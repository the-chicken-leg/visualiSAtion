from common.graphics import *
import random

class HungryPatron(Rectangle):
    def __init__(self, parent: Window, center: Point, patron_fatbody_index: int):
        y_length = parent.height - (parent.height * 0.5)
        self.patron_fatbody_index = patron_fatbody_index
        super().__init__(parent, center, patron_fatbody_index, y_length)

    def draw(self):
        red = "%02x" % random.randint(0, 255)
        green = "%02x" % random.randint(0, 255)
        blue = "%02x" % random.randint(0, 255)
        self.fill_color = "#" + red + green + blue
        super().draw(self.fill_color)

    def move_up_in_line(self):
        self.center = Point(self.center.x + self.patron_fatbody_index, self.center.y)
        self.top_left = Point(self.center.x - (self.x_length / 2), self.center.y - (self.y_length / 2))
        self.bottom_right = Point(self.center.x + (self.x_length / 2), self.center.y + (self.y_length / 2))
        super().draw(self.fill_color)
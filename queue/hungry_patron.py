from common.graphics import *
import random

class HungryPatron(Rectangle):
    def draw(self, window: Window, center: Point, patron_fatbody_width: int):
        self.window = window
        self.center = center
        self.patron_fatbody_width = patron_fatbody_width

        self.y_length = window.height - (window.height * 0.5)

        red = "%02x" % random.randint(0, 255)
        green = "%02x" % random.randint(0, 255)
        blue = "%02x" % random.randint(0, 255)
        self.fill_color = "#" + red + green + blue

        super().draw(window, center, patron_fatbody_width, self.y_length, self.fill_color)

    def move_up_in_line(self):
        self.center = Point(self.center.x + self.patron_fatbody_width, self.center.y)
        super().draw(self.window, self.center, self.patron_fatbody_width, self.y_length, self.fill_color)
from graphics import *

class SortThing(Rectangle):
    def __init__(self, value: int):
        self.value = value
        self.center_y = None
        self.fill_color = None
        super().__init__(tags=["bar"])

    def draw(self, window: Window, center_x: int, thing_width: int):
        if self.center_y is None:
            center_y = window.height - 50 - self.value / 2
        
        if self.fill_color is None:
            red = "%02x" % 50
            green = "%02x" % 50
            blue_int = 100 + int((self.value - 50) * ((255 - 100) / ((window.height - 100) - 50)))
            blue = "%02x" % blue_int
            self.fill_color = "#" + red + green + blue

        super().draw(window, Point(center_x, center_y), thing_width, self.value, self.fill_color)

class SortIndicator(Circle):
    def __init__(self):
        super().__init__(tags=["indicator"])

    def draw(self, window: Window, center_x: Point):
        super().draw(window, Point(center_x, 25), 10)
from tkinter import *
import time

class Window:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title("visualiSAtion!")
        # self.root.eval('tk::PlaceWindow . center')
        self.root.resizable(0, 0)

        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        self.is_window_running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.is_window_running = True
        while self.is_window_running:
            self.redraw()
            time.sleep(0.01)

    def close(self):
        self.is_window_running = False

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class SolidLine:
    def __init__(self, parent: Window, point1: Point, point2: Point):
        self.parent = parent
        self.point1 = point1
        self.point2 = point2

    def draw(self, fill_color: str = "black", width : int = 2):
        self.id = self.parent.canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=width,
        )

class DashedLine:
    def __init__(self, parent: Window, point1: Point, point2: Point):
        self.parent = parent
        self.point1 = point1
        self.point2 = point2

    def draw(self, fill_color: str = "black", width : int = 2):
        self.id = self.parent.canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=width,
            dash=10
        )

class Rectangle:
    def __init__(self, parent: Window, center: Point, x_length: int, y_length: int):
        self.parent = parent
        self.center = center
        self.x_length = x_length
        self.y_length = y_length
        self.top_left = Point(center.x - (x_length / 2), center.y - (y_length / 2))
        self.bottom_right = Point(center.x + (x_length / 2), center.y + (y_length / 2))

    def draw(self, fill_color: str = "black"):
        self.id = self.parent.canvas.create_rectangle(
            self.top_left.x,
            self.top_left.y,
            self.bottom_right.x,
            self.bottom_right.y,
            fill=fill_color,
        )

class Square:
    def __init__(self, parent: Window, center: Point, side_length: int):
        self.parent = parent
        self.center = center
        self.top_left = Point(center.x - (side_length / 2), center.y - (side_length / 2))
        self.bottom_right = Point(center.x + (side_length / 2), center.y + (side_length / 2))

    def draw(self, fill_color: str = "black"):
        self.id = self.parent.canvas.create_rectangle(
            self.top_left.x,
            self.top_left.y,
            self.bottom_right.x,
            self.bottom_right.y,
            fill=fill_color,
        )

class Circle:
    def __init__(self, parent: Window, center: Point, radius: int):
        self.parent = parent
        self.top_left = Point(center.x - radius, center.y - radius)
        self.bottom_right = Point(center.x + radius, center.y + radius)

    def draw(self, fill_color: str = "black"):
        self.id = self.parent.canvas.create_oval(
            self.top_left.x,
            self.top_left.y,
            self.bottom_right.x,
            self.bottom_right.y,
            fill=fill_color,
        )

class BigX:
    def __init__(self, parent: Window, center: Point, radius: int):
        self.parent = parent
        self.top_left = Point(center.x - radius, center.y - radius)
        self.top_right = Point(center.x + radius, center.y - radius)
        self.bottom_right = Point(center.x + radius, center.y + radius)
        self.bottom_left = Point(center.x - radius, center.y + radius)

    def draw(self, fill_color: str = "black", width: int = 7):
        forward_slash = SolidLine(self.parent, self.bottom_left, self.top_right)
        back_slash = SolidLine(self.parent, self.bottom_right, self.top_left)
        forward_slash.draw(fill_color, width)
        back_slash.draw(fill_color, width)

class Triangle:
    def __init__(self, parent: Window, center: Point, radius: int):
        self.parent = parent
        self.top = Point(center.x, center.y - radius)
        self.bottom_right = Point(center.x + radius, center.y + radius)
        self.bottom_left = Point(center.x - radius, center.y + radius)

    def draw(self, fill_color: str = "black"):
        self.id = self.parent.canvas.create_polygon(
            self.top.x,
            self.top.y,
            self.bottom_right.x,
            self.bottom_right.y,
            self.bottom_left.x,
            self.bottom_left.y,
            fill=fill_color,
        )

class Text:
    def __init__(self, parent: Window, center: Point, text: str):
        self.parent = parent
        self.center = center
        self.text = text

    def draw(self, fill_color: str = "black", font_size: int = 16):
        self.id = self.parent.canvas.create_text(
            self.center.x,
            self.center.y,
            font=("Tahoma", font_size),
            fill=fill_color,
            justify="center",
            text=self.text,
        )
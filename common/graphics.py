from tkinter import *
from tkinter import ttk
import time

class Window:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.root = Tk()
        self.root.title("visualiSAtion!")
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

class MyButton:
    def __init__(
        self,
        parent: Window,
        text: str,
        command,
        tags: list = None,
    ):
        self.parent = parent
        self.tags = tags
        self.button = ttk.Button(parent.root, text=text, command=command)

    def draw(self, center: Point):
        self.id = self.parent.canvas.create_window(
            center.x,
            center.y,
            window=self.button,
            tags=self.tags
        )

class SolidLine:
    def __init__(
        self,
        parent: Window,
        point1: Point = None,
        point2: Point = None,
        tags: list = None,
    ):
        self.parent = parent
        self.tags = tags
        if (point1 and point2) is not None:
            self.point1 = point1
            self.point2 = point2

    def draw(self, fill_color: str = "black", width: int = 2):
        self.id = self.parent.canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=width,
            tags=self.tags,
        )

class DashedLine:
    def __init__(
        self,
        parent: Window,
        point1: Point = None,
        point2: Point = None,
        tags: list = None,
    ):
        self.parent = parent
        self.tags = tags
        if (point1 and point2) is not None:
            self.point1 = point1
            self.point2 = point2

    def draw(self, fill_color: str = "black", width: int = 2):
        self.id = self.parent.canvas.create_line(
            self.point1.x,
            self.point1.y,
            self.point2.x,
            self.point2.y,
            fill=fill_color,
            width=width,
            dash=10,
            tags=self.tags,
        )

class Rectangle:
    def __init__(
        self,
        parent: Window,
        center: Point = None,
        x_length: int = None,
        y_length: int = None,
        tags: list = None,
    ):
        self.parent = parent
        self.tags = tags
        if (center and x_length and y_length) is not None:
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
            tags=self.tags,
        )

class Square:
    def __init__(
        self,
        parent: Window,
        center: Point = None,
        side_length: int = None,
        tags: list = None,
    ):
        self.parent = parent
        self.tags = tags
        if (center and side_length) is not None:
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
            tags=self.tags,
        )

class Circle:
    def __init__(
        self,
        parent: Window,
        center: Point = None,
        radius: int = None,
        tags: list = None,
    ):
        self.parent = parent
        self.tags = tags
        if (center and radius) is not None:
            self.center = center
            self.top_left = Point(center.x - radius, center.y - radius)
            self.bottom_right = Point(center.x + radius, center.y + radius)

    def draw(self, fill_color: str = "black"):
        self.id = self.parent.canvas.create_oval(
            self.top_left.x,
            self.top_left.y,
            self.bottom_right.x,
            self.bottom_right.y,
            fill=fill_color,
            tags=self.tags,
        )

class BigX:
    def __init__(
        self,
        parent: Window,
        center: Point = None,
        radius: int = None,
        tags: list = None,
    ):
        self.parent = parent
        self.tags = tags
        if (center and radius) is not None:
            self.top_left = Point(center.x - radius, center.y - radius)
            self.top_right = Point(center.x + radius, center.y - radius)
            self.bottom_right = Point(center.x + radius, center.y + radius)
            self.bottom_left = Point(center.x - radius, center.y + radius)

    def draw(self, fill_color: str = "black", width: int = 7):
        forward_slash = SolidLine(
            self.parent,
            self.bottom_left,
            self.top_right,
            tags=self.tags,
        )
        back_slash = SolidLine(
            self.parent,
            self.bottom_right,
            self.top_left,
            tags=self.tags,
        )
        self.id1 = forward_slash.draw(fill_color, width)
        self.id2 = back_slash.draw(fill_color, width)

class Triangle:
    def __init__(
        self,
        parent: Window,
        center: Point = None,
        radius: int = None,
        tags: list = None,
    ):
        self.parent = parent
        self.tags = tags
        if (center and radius) is not None:
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
            tags=self.tags,
        )

class Text:
    def __init__(
        self,
        parent: Window,
        text: str,
        center: Point = None,
        tags: list = None,
    ):
        self.parent = parent
        self.text = text
        self.tags = tags
        if center is not None:
            self.center = center

    def draw(self, fill_color: str = "black", font_size: int = 16):
        self.id = self.parent.canvas.create_text(
            self.center.x,
            self.center.y,
            font=("Tahoma", font_size),
            fill=fill_color,
            justify="center",
            text=self.text,
            tags=self.tags,
        )
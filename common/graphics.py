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

class CanvasButton:
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
    def __init__(self, tags: list = None):
        self.tags = tags

    def draw(
        self,
        parent: Window,
        point1: Point,
        point2: Point,
        fill_color: str = "black",
        width: int = 2,
    ):
        self.id = parent.canvas.create_line(
            point1.x,
            point1.y,
            point2.x,
            point2.y,
            fill=fill_color,
            width=width,
            tags=self.tags,
        )

class DashedLine:
    def __init__(self, tags: list = None):
        self.tags = tags

    def draw(
        self,
        parent: Window,
        point1: Point,
        point2: Point,        
        fill_color: str = "black",
        width: int = 2,
    ):
        self.id = parent.canvas.create_line(
            point1.x,
            point1.y,
            point2.x,
            point2.y,
            fill=fill_color,
            width=width,
            dash=10,
            tags=self.tags,
        )

class Rectangle:
    def __init__(self, tags: list = None):
        self.tags = tags

    def draw(
        self,
        parent: Window,
        center: Point,
        x_length: int,
        y_length: int,        
        fill_color: str = "black",
    ):
        top_left = Point(center.x - (x_length / 2), center.y - (y_length / 2))
        bottom_right = Point(center.x + (x_length / 2), center.y + (y_length / 2))        
        self.id = parent.canvas.create_rectangle(
            top_left.x,
            top_left.y,
            bottom_right.x,
            bottom_right.y,
            fill=fill_color,
            tags=self.tags,
        )

class Square:
    def __init__(self, tags: list = None):
        self.tags = tags

    def draw(
        self,
        parent: Window,
        center: Point,
        side_length: int,        
        fill_color: str = "black",
    ):
        top_left = Point(center.x - (side_length / 2), center.y - (side_length / 2))
        bottom_right = Point(center.x + (side_length / 2), center.y + (side_length / 2))        
        self.id = parent.canvas.create_rectangle(
            top_left.x,
            top_left.y,
            bottom_right.x,
            bottom_right.y,
            fill=fill_color,
            tags=self.tags,
        )

class Circle:
    def __init__(self, tags: list = None):
        self.tags = tags

    def draw(
        self,
        parent: Window,
        center: Point,
        radius: int,
        fill_color: str = "black",
    ):
        top_left = Point(center.x - radius, center.y - radius)
        bottom_right = Point(center.x + radius, center.y + radius)        
        self.id = parent.canvas.create_oval(
            top_left.x,
            top_left.y,
            bottom_right.x,
            bottom_right.y,
            fill=fill_color,
            tags=self.tags,
        )

class BigX:
    def __init__(self, tags: list = None):
        self.tags = tags

    def draw(
        self,
        parent: Window,
        center: Point,
        radius: int,        
        fill_color: str = "black",
        width: int = 7,
    ):
        forward_slash = SolidLine(tags=self.tags)
        back_slash = SolidLine(tags=self.tags)

        top_left = Point(center.x - radius, center.y - radius)
        top_right = Point(center.x + radius, center.y - radius)
        bottom_right = Point(center.x + radius, center.y + radius)
        bottom_left = Point(center.x - radius, center.y + radius)

        self.id_forward_slash = forward_slash.draw(parent, top_right, bottom_left, fill_color, width)
        self.id_back_slash = back_slash.draw(parent, top_left, bottom_right, fill_color, width)

class Triangle:
    def __init__(self, tags: list = None):
        self.tags = tags

    def draw(
        self,
        parent: Window,
        center: Point,
        radius: int,
        fill_color: str = "black",
    ):
        top = Point(center.x, center.y - radius)
        bottom_right = Point(center.x + radius, center.y + radius)
        bottom_left = Point(center.x - radius, center.y + radius)        
        self.id = parent.canvas.create_polygon(
            top.x,
            top.y,
            bottom_right.x,
            bottom_right.y,
            bottom_left.x,
            bottom_left.y,
            fill=fill_color,
            tags=self.tags,
        )

class Text:
    def __init__(self, text: str, tags: list = None):
        self.text = text
        self.tags = tags

    def draw(
        self,
        parent: Window,
        center: Point,        
        fill_color: str = "black",
        font_size: int = 16,
    ):
        self.id = parent.canvas.create_text(
            center.x,
            center.y,
            font=("Tahoma", font_size),
            fill=fill_color,
            justify="center",
            text=self.text,
            tags=self.tags,
        )
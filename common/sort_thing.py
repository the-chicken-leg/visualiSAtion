import functools

from . import graphics as gr

@functools.total_ordering
class SortThing(gr.Rectangle):
    def __init__(self, value: int):
        self.value = value
        self.center_y = None
        self.fill_color = None
        super().__init__(tags=["sort_thing"]) 

    def draw(self, window: gr.Window, center_x: float, thing_width: int):
        if self.center_y is None:
            self.center_y = window.height - 50 - self.value / 2
        
        if self.fill_color is None:
            red = "%02x" % 50
            green = "%02x" % 50
            blue = "%02x" % int(100 + (self.value - 50) * ((255 - 100) / ((window.height - 100) - 50)))
            self.fill_color = "#" + red + green + blue

        super().draw(
            window,
            gr.Point(center_x, self.center_y),
            thing_width,
            self.value,
            self.fill_color,
        )

    def __eq__(self, other):
        return self.value == other.value
    
    def __lt__(self, other):
        return self.value < other.value
    
class SortIndicator(gr.Circle):
    def __init__(self):
        super().__init__(tags=["sort_indicator"])

    def draw(self, window: gr.Window, center_x: float):
        super().draw(window, gr.Point(center_x, 25), 8)

class SortHighlighterRed(gr.Rectangle):
    def __init__(self, sort_thing: SortThing):
        self.value = sort_thing.value
        self.center_y = sort_thing.center_y
        self.fill_color = "red2"
        super().__init__(tags=["sort_highlighter_red"])

    def draw(self, window: gr.Window, center_x: float, thing_width: int):
        super().draw(
            window,
            gr.Point(center_x, self.center_y),
            thing_width,
            self.value,
            self.fill_color,
        )

class SortHighlighterCyan(gr.Rectangle):
    def __init__(self, sort_thing: SortThing):
        self.value = sort_thing.value
        self.center_y = sort_thing.center_y
        self.fill_color = "cyan2"
        super().__init__(tags=["sort_highlighter_cyan"])

    def draw(self, window: gr.Window, center_x: float, thing_width: int):
        super().draw(
            window,
            gr.Point(center_x, self.center_y),
            thing_width,
            self.value,
            self.fill_color,
        )

class SortHighlighterYellow(gr.Rectangle):
    def __init__(self, sort_thing: SortThing):
        self.value = sort_thing.value
        self.center_y = sort_thing.center_y
        self.fill_color = "yellow2"
        super().__init__(tags=["sort_highlighter_yellow"])

    def draw(self, window: gr.Window, center_x: float, thing_width: int):
        super().draw(
            window,
            gr.Point(center_x, self.center_y),
            thing_width,
            self.value,
            self.fill_color,
        )

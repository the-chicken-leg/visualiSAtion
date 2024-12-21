from common.graphics import *
from hungry_patron import *
import random

class SnackshackQueue:
    def __init__(self, parent: Window, starting_num_patrons: int, patron_fatbody_index: int):
        self.parent = parent
        self.starting_num_patrons = starting_num_patrons
        self.patron_fatbody_index = patron_fatbody_index

        self.create_snackshack_queue()

    def create_snackshack_queue(self):
        self.snackshack_queue = []
        self.center_y = self.parent.height / 2
        for i in range(self.starting_num_patrons):
            center_x = self.parent.width - 25 - (0.5 * self.patron_fatbody_index) - (i * self.patron_fatbody_index)
            self.snackshack_queue.append(
                HungryPatron(
                    self.parent,
                    Point(center_x, self.center_y),
                    self.patron_fatbody_index,
                )
            )

        self.draw_snackshack_queue()

    def draw_snackshack_queue(self):
        for hungry_patron in self.snackshack_queue:
            hungry_patron.draw()
            self.parent.redraw()

    def simulate(self, push_pop_ratio: float, sleep_time: float, stop_when_empty: bool):
        while True:
            push_or_pop = self.get_push_or_pop(push_pop_ratio)
            if push_or_pop == "push":
                self.push()
            elif push_or_pop == "pop":
                self.pop()
            if stop_when_empty and not self.snackshack_queue:
                break
            time.sleep(sleep_time)

    def get_push_or_pop(self, push_pop_ratio: float) -> str:
        prob_push = push_pop_ratio / (push_pop_ratio + 1)
        rando = random.random()
        if rando <= prob_push:
            return "push"
        return "pop"
    
    def push(self):
        num_patrons = len(self.snackshack_queue)
        center_x = self.parent.width - 25 - (0.5 * self.patron_fatbody_index) - (num_patrons * self.patron_fatbody_index)
        new_patron = HungryPatron(
            self.parent,
            Point(center_x, self.center_y),
            self.patron_fatbody_index,
        )
        self.snackshack_queue.append(new_patron)
        new_patron.draw()
        self.parent.redraw()

    def pop(self):
        if not self.snackshack_queue:
            return
        feed_this_patron = self.snackshack_queue.pop()
        self.parent.canvas.delete(feed_this_patron.id)
        self.parent.redraw()
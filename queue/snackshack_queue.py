from hungry_patron import *
import random

class SnackshackQueue:
    def __init__(self, starting_num_patrons: int, push_pop_ratio: float, stop_when_empty: bool):
        self.push_pop_ratio = push_pop_ratio
        self.stop_when_empty = stop_when_empty
        
        self.snackshack_queue = [HungryPatron() for i in range(starting_num_patrons)]

    def draw_in_window(self, window: Window, patron_fatbody_width: int, sleep_time: float):
        self.window = window
        self.patron_fatbody_width = patron_fatbody_width
        self.sleep_time = sleep_time

        self.center_y = window.height / 2
        for i, hungry_patron in enumerate(self.snackshack_queue):
            center_x = window.width - 25 - (0.5 * patron_fatbody_width) - (i * patron_fatbody_width)
            hungry_patron.draw(window, Point(center_x, self.center_y), patron_fatbody_width)
        window.redraw()
        time.sleep(sleep_time)

        self.simulate()

    def simulate(self):
        while True:
            push_or_pop = self.get_push_or_pop(self.push_pop_ratio)
            if push_or_pop == "push":
                self.push()
            elif push_or_pop == "pop":
                self.pop()
            if self.stop_when_empty and not self.snackshack_queue:
                break
            time.sleep(self.sleep_time)

    def get_push_or_pop(self, push_pop_ratio: float) -> str:
        prob_push = push_pop_ratio / (push_pop_ratio + 1)
        rando = random.random()
        if rando <= prob_push:
            return "push"
        return "pop"
    
    def push(self):
        new_patron = HungryPatron()
        self.snackshack_queue.append(new_patron)

        num_patrons = len(self.snackshack_queue) - 1
        center_x = self.window.width - 25 - (0.5 * self.patron_fatbody_width) - (num_patrons * self.patron_fatbody_width)
        new_patron.draw(self.window, Point(center_x, self.center_y), self.patron_fatbody_width)
        self.window.redraw()

    def pop(self):
        if not self.snackshack_queue:
            return
        feed_this_patron = self.snackshack_queue.pop(0)
        self.window.canvas.delete(feed_this_patron.id)
        self.window.redraw()
        time.sleep(self.sleep_time)

        for hungry_patron in self.snackshack_queue:
            self.window.canvas.delete(hungry_patron.id)
            hungry_patron.move_up_in_line()
        self.window.redraw()
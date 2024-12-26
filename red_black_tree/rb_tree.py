from rb_node import *
import random
import time

class RBTree:
    def __init__(
        self,
        window: Window,
        insertion_type: str,
        num_nodes: int,
        custom_insertion: list,
        step_manually: bool,
        sleep_time: int,
    ):
        self.window = window

        self.step_manually = step_manually
        if step_manually:
            self.forward_button = MyButton(
                window,
                "Forward",
                self.step_forward,
                ["buttons"],
            )
            self.window.root.bind(
                "<Right>",
                lambda x: self.forward_button.button.invoke(),
            )
            self.forward_button.draw(Point(window.width / 2 + 50, window.height - 25))
            
            self.back_button = MyButton(
                window,
                "Back",
                self.step_back,
                ["buttons"],
            )
            self.window.root.bind(
                "<Left>",
                lambda x: self.back_button.button.invoke(),
            )
            self.back_button.draw(Point(window.width / 2 - 50, window.height - 25))

        self.insertion_type = insertion_type
        self.num_nodes = num_nodes
        self.custom_insertion = custom_insertion
        self.sleep_time = sleep_time

        self.nil = RBNode(window, None)

        self.create_node_values()

    def create_node_values(self):
        if self.insertion_type == "ascending":
            self.node_values = list(range(1, self.num_nodes + 1))
        elif self.insertion_type == "descending":
            self.node_values = list(reversed(range(1, self.num_nodes + 1)))
        elif self.insertion_type == "random":
            self.node_values = list(range(1, self.num_nodes + 1))
            random.shuffle(self.node_values)
        elif self.insertion_type == "custom":
            self.node_values = self.custom_insertion

        insertion_order = Text(
            self.window,
            f"Insertion order: {str(self.node_values).strip("[]")}",
            Point(self.window.width / 2, 25),
        )
        insertion_order.draw()
        
        if self.step_manually:
            self.node_index = 1
            self.should_fix = False
            self.replay(self.should_fix)
        else:
            self.window.redraw()
            time.sleep(self.sleep_time)
            self.insert_and_fix()

    def step_forward(self):
        if self.node_index < len(self.node_values):
            if not self.should_fix:
                self.should_fix = not self.should_fix
                self.replay(self.should_fix)
            else:
                self.node_index += 1
                self.should_fix = not self.should_fix
                self.replay(self.should_fix)
        elif self.node_index == len(self.node_values):
            self.should_fix = True
            self.replay(self.should_fix)

    def step_back(self):
        if self.node_index > 1:
            if not self.should_fix:
                self.node_index -= 1
                self.should_fix = not self.should_fix
                self.replay(self.should_fix)
            else:
                self.should_fix = not self.should_fix
                self.replay(self.should_fix)
        elif self.node_index == 1:
            self.should_fix = False
            self.replay(self.should_fix)

    def replay(self, should_fix: bool):
        self.root_node = self.nil
        for node_value in self.node_values[:self.node_index]:
            self.insert(node_value)
            if not should_fix:
                self.draw(node_value, "insert")
            try:
                self.fix(self.new_node)
            except AttributeError:
                # duplicate, just ignore
                pass
        if should_fix:
            self.draw(node_value, "fix")

    def insert_and_fix(self):
        self.root_node = self.nil
        for node_value in self.node_values:
            self.insert(node_value)
            self.draw(node_value, "insert")
            try:
                self.fix(self.new_node)
            except AttributeError:
                # duplicate, just ignore
                pass
            self.draw(node_value, "fix")

    def insert(self, node_value: int):
        self.new_node = RBNode(self.window, node_value)
        self.new_node.red = True
        self.new_node.left_child = self.nil
        self.new_node.right_child = self.nil

        parent = None
        current = self.root_node
        while current != self.nil:
            parent = current
            if self.new_node.value < current.value:
                current = current.left_child
            elif self.new_node.value > current.value:
                current = current.right_child
            else:
                # duplicate, just ignore
                return

        self.new_node.parent_node = parent
        if parent is None:
            self.root_node = self.new_node
        elif self.new_node.value < parent.value:
            parent.left_child = self.new_node
        elif self.new_node.value > parent.value:
            parent.right_child = self.new_node

    def draw(self, node_value: int, insert_or_fix: str):
        self.window.canvas.delete("action", "tree")
        action = Text(
            self.window,
            f"{insert_or_fix} {node_value}",
            Point(self.window.width / 2, 75),
            tags=["action"],
        )
        action.draw()
        self.root_node.draw_tree()
        if not self.step_manually:
            self.window.redraw()
            time.sleep(self.sleep_time)

    def fix(self, new_node: RBNode):
        while new_node != self.root_node and new_node.parent_node.red:
            parent = new_node.parent_node
            grandparent = parent.parent_node

            if parent == grandparent.right_child:
                uncle = grandparent.left_child
                if uncle.red:
                    parent.red = False                  # case 1
                    grandparent.red = True              # case 1
                    uncle.red = False                   # case 1
                    new_node = grandparent
                elif not uncle.red:
                    if new_node == parent.left_child:
                        self.rotate_right(parent)       # case 2
                        new_node = parent
                        parent = new_node.parent_node
                    parent.red = False                  # case 3
                    grandparent.red = True              # case 3
                    self.rotate_left(grandparent)       # case 3

            elif parent == grandparent.left_child:
                uncle = grandparent.right_child
                if uncle.red:
                    parent.red = False                  # case 1
                    grandparent.red = True              # case 1
                    uncle.red = False                   # case 1
                    new_node = grandparent
                elif not uncle.red:
                    if new_node == parent.right_child:
                        self.rotate_left(parent)        # case 2
                        new_node = parent
                        parent = new_node.parent_node
                    parent.red = False                  # case 3
                    grandparent.red = True              # case 3
                    self.rotate_right(grandparent)      # case 3
        self.root_node.red = False      # case 0

    def rotate_left(self, pivot_parent: RBNode):
        if pivot_parent == self.nil or pivot_parent.right_child == self.nil:
            return
        pivot = pivot_parent.right_child
        pivot_parent.right_child = pivot.left_child
        if pivot.left_child != self.nil:
            pivot.left_child.parent_node = pivot_parent

        pivot.parent_node = pivot_parent.parent_node
        if pivot_parent.parent_node is None:
            self.root_node = pivot
        elif pivot_parent == pivot_parent.parent_node.left_child:
            pivot_parent.parent_node.left_child = pivot
        else:
            pivot_parent.parent_node.right_child = pivot
        pivot.left_child = pivot_parent
        pivot_parent.parent_node = pivot

    def rotate_right(self, pivot_parent: RBNode):
        if pivot_parent == self.nil or pivot_parent.left_child == self.nil:
            return
        pivot = pivot_parent.left_child
        pivot_parent.left_child = pivot.right_child
        if pivot.right_child != self.nil:
            pivot.right_child.parent_node = pivot_parent

        pivot.parent_node = pivot_parent.parent_node
        if pivot_parent.parent_node is None:
            self.root_node = pivot
        elif pivot_parent == pivot_parent.parent_node.right_child:
            pivot_parent.parent_node.right_child = pivot
        else:
            pivot_parent.parent_node.left_child = pivot
        pivot.right_child = pivot_parent
        pivot_parent.parent_node = pivot
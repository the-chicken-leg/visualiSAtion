from common.graphics import *

class RBNode(Circle):
    def __init__(self, value: int):
        super().__init__(tags=["nodes", "tree"])

        self.value = value

        self.red = False
        self.parent_node = None
        self.left_child = None
        self.right_child = None

    def draw_tree(self, window: Window):
        self.window = window
        cell_size = 50
        root_center = Point(window.width / 2, cell_size / 2 + 100)

        self.draw_nodes(window, cell_size, root_center, self.value)
        self.draw_lines()

    def draw_nodes(
        self,
        window: Window,
        cell_size: int,
        root_center: Point,
        root_value: int,
        level: int = 0,
    ):
        if self.value is not None:
            self.right_child.draw_nodes(window, cell_size, root_center, root_value, level + 1)

            self.node_center_x = root_center.x + cell_size * (self.value - root_value)
            self.node_center_y = root_center.y + (cell_size * level)
            self.draw(window, Point(self.node_center_x, self.node_center_y))
            node_text = Text(str(self.value), tags=["text", "tree"])
            node_text.draw(window, Point(self.node_center_x, self.node_center_y), fill_color="white")

            self.left_child.draw_nodes(window, cell_size, root_center, root_value, level + 1)

    def draw(self, window: Window, center: Point):
        fill_color = "black"
        if self.red:
            fill_color = "red"
        super().draw(window, center, 20, fill_color)

    def draw_lines(self):
        for rb_node in self.traverse_preorder([], False):
            if rb_node.left_child.value:
                line_to_left_child = SolidLine(tags=["lines", "tree"])
                line_to_left_child.draw(
                    self.window,
                    Point(rb_node.node_center_x, rb_node.node_center_y),
                    Point(rb_node.left_child.node_center_x, rb_node.left_child.node_center_y),
                )

            if rb_node.right_child.value:
                line_to_right_child = SolidLine(tags=["lines", "tree"])
                line_to_right_child.draw(
                    self.window,
                    Point(rb_node.node_center_x, rb_node.node_center_y),
                    Point(rb_node.right_child.node_center_x, rb_node.right_child.node_center_y),
                )

        self.window.canvas.tag_lower("lines", "text")
        self.window.canvas.tag_lower("lines", "nodes")

    def traverse_preorder(self, traversed: list, return_values: bool = True) -> list:
        if self.value is not None:
            if return_values:
                traversed.append(self.value)
            else:
                traversed.append(self)
        if self.left_child is not None:
            self.left_child.traverse_preorder(traversed, return_values)
        if self.right_child is not None:
            self.right_child.traverse_preorder(traversed, return_values)
        return traversed

    def traverse_postorder(self, traversed: list, return_values: bool = True) -> list:
        if self.left_child is not None:
            self.left_child.traverse_postorder(traversed, return_values)
        if self.right_child is not None:
            self.right_child.traverse_postorder(traversed, return_values)
        if self.value is not None:
            if return_values:
                traversed.append(self.value)
            else:
                traversed.append(self)
        return traversed

    def traverse_inorder(self, traversed: list, return_values: bool = True) -> list:
        if self.left_child is not None:
            self.left_child.traverse_inorder(traversed, return_values)
        if self.value is not None:
            if return_values:
                traversed.append(self.value)
            else:
                traversed.append(self)
        if self.right_child is not None:
            self.right_child.traverse_inorder(traversed, return_values)
        return traversed
    
    def print_tree(self, level: int = 0):
        if self.value is not None:
            self.right_child.print_tree(level + 1)
            print(
                " " * 4 * level
                + "> "
                + str(self.value)
                + " "
                + ("[red]" if self.red else "[black]")
            )
            self.left_child.print_tree(level + 1)
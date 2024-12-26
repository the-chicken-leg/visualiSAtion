from common.graphics import *

class RBNode(Circle):
    def __init__(self, window: Window, value: int):
        self.window = window
        super().__init__(window, tags=["nodes", "tree"])

        self.value = value

        self.red = False
        self.parent_node = None
        self.left_child = None
        self.right_child = None

        self.cell_size = 50
        self.node_radius = 20
        self.root_center = Point(self.window.width / 2, self.cell_size / 2 + 100)

    def draw(self, center: Point):
        self.center = center
        self.top_left = Point(center.x - self.node_radius, center.y - self.node_radius)
        self.bottom_right = Point(center.x + self.node_radius, center.y + self.node_radius)

        fill_color = "black"
        if self.red:
            fill_color = "red"
        super().draw(fill_color)

    def draw_tree(self):
        self.draw_nodes(self.value)
        self.draw_lines()

    def draw_nodes(self, root_value: int, level: int = 0):
        if self.value is not None:
            self.right_child.draw_nodes(root_value, level + 1)

            self.node_center_x = self.root_center.x + self.cell_size * (self.value - root_value)
            self.node_center_y = self.root_center.y + (self.cell_size * level)
            self.draw(Point(self.node_center_x, self.node_center_y))
            node_text = Text(
                self.window,
                str(self.value),
                Point(self.node_center_x, self.node_center_y),
                tags=["text", "tree"],
            )
            node_text.draw(fill_color="white")

            self.left_child.draw_nodes(root_value, level + 1)

    def draw_lines(self):
        for rb_node in self.traverse_preorder([], False):
            if rb_node.left_child.value:
                line_to_left_child = SolidLine(
                    rb_node.window,
                    Point(rb_node.node_center_x, rb_node.node_center_y),
                    Point(rb_node.left_child.node_center_x, rb_node.left_child.node_center_y),
                    tags=["lines", "tree"],
                )
                line_to_left_child.draw()

            if rb_node.right_child.value:
                line_to_right_child = SolidLine(
                    rb_node.window,
                    Point(rb_node.node_center_x, rb_node.node_center_y),
                    Point(rb_node.right_child.node_center_x, rb_node.right_child.node_center_y),
                    tags=["lines", "tree"],
                )
                line_to_right_child.draw()

        self.window.canvas.tag_lower("lines", "text")
        self.window.canvas.tag_lower("lines", "nodes")

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
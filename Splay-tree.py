class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.parent = None  # Add parent attribute

class SplayTree:
    def __init__(self):
        self.root = None

    def splay(self, node):
        while node != self.root:
            if node == node.parent.left:
                self._rotate_right(node.parent)
            else:
                self._rotate_left(node.parent)

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        right_child.parent = node.parent
        if not node.parent:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        left_child.parent = node.parent
        if not node.parent:
            self.root = left_child
        elif node == node.parent.left:
            node.parent.left = left_child
        else:
            node.parent.right = left_child
        left_child.right = node
        node.parent = left_child

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return
        current = self.root
        while current:
            parent = current
            current = new_node.value < current.value and current.left or current.right
        new_node.parent = parent
        if new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        self.splay(new_node)

    def height(self):
        def height_helper(node):
            return 0 if not node else 1 + max(height_helper(node.left), height_helper(node.right))
        return height_helper(self.root)

    def display(self):
        def display_helper(node, prefix="", is_left=True):
            if node:
                print(prefix + ("|-- " if is_left else "`-- ") + str(node.value))
                display_helper(node.left, prefix + ("|   " if is_left else "    "), True)
                display_helper(node.right, prefix + ("|   " if is_left else "    "), False)
        display_helper(self.root)

def main():
    splay_tree = SplayTree()
    values = input("Enter values separated by commas: ").split(',')
    for value in map(int, values):
        splay_tree.insert(value)
    print("\nSplay Tree structure:")
    splay_tree.display()
    print(f"\nHeight of the tree: {splay_tree.height()}")

if __name__ == "__main__":
    main()

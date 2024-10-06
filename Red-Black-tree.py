class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None
        self.color = "red"  # New nodes are red by default

class RedBlackTree:
    def __init__(self):
        self.NIL_LEAF = Node(0)
        self.NIL_LEAF.color = "black"
        self.root = self.NIL_LEAF

    def insert(self, value):
        new_node = Node(value)
        new_node.left = new_node.right = self.NIL_LEAF
        self._insert_into_tree(new_node)
        self._fix_insert(new_node)

    def _insert_into_tree(self, new_node):
        parent = None
        current = self.root
        while current != self.NIL_LEAF:
            parent = current
            current = new_node.value < current.value and current.left or current.right
        if parent is None:
            self.root = new_node
        else:
            if new_node.value < parent.value:
                parent.left = new_node
            else:
                parent.right = new_node
        new_node.parent = parent

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_right(node.parent.parent)
            else:
                # Symmetric case
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._rotate_left(node.parent.parent)
        self.root.color = "black"

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left != self.NIL_LEAF:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
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
        if left_child.right != self.NIL_LEAF:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def height(self):
        def height_helper(node):
            if node == self.NIL_LEAF:
                return 0
            return 1 + max(height_helper(node.left), height_helper(node.right))

        return height_helper(self.root)

    def display(self):
        def display_helper(node, prefix="", is_left=True):
            if node != self.NIL_LEAF:
                print(prefix + ("|-- " if is_left else "`-- ") + str(node.value) + f"({node.color})")
                display_helper(node.left, prefix + ("|   " if is_left else "    "), True)
                display_helper(node.right, prefix + ("|   " if is_left else "    "), False)

        display_helper(self.root)

def main():
    rbt = RedBlackTree()
    values = input("Enter values separated by commas: ").split(',')
    for value in map(int, values):
        rbt.insert(value)
    print("\nRed-Black Tree structure:")
    rbt.display()
    print(f"\nHeight of the tree: {rbt.height()}")

if __name__ == "__main__":
    main()

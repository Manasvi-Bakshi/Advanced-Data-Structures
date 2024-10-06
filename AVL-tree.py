class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance(root)

    def balance(self, node):
        balance_factor = self.get_balance(node)

        # Left heavy
        if balance_factor > 1:
            if self.get_balance(node.left) < 0:  # Left-Right case
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right heavy
        if balance_factor < -1:
            if self.get_balance(node.right) > 0:  # Right-Left case
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def display(self, node, prefix="", is_left=True):
        if node:
            print(prefix + ("|-- " if is_left else "`-- ") + str(node.value))
            self.display(node.left, prefix + ("|   " if is_left else "    "), True)
            self.display(node.right, prefix + ("|   " if is_left else "    "), False)

def main():
    avl_tree = AVLTree()
    root = None
    values = input("Enter values separated by commas: ").split(',')
    for value in map(int, values):
        root = avl_tree.insert(root, value)
    
    print("\nAVL Tree structure:")
    avl_tree.display(root)
    print(f"\nHeight of the tree: {avl_tree.get_height(root)}")

if __name__ == "__main__":
    main()

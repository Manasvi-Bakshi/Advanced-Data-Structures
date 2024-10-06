from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)  # Left
        print(root.data, end=" ")      # Current
        inorder_traversal(root.right) # Right

def postorder_traversal(node):
    if node:
        postorder_traversal(node.left)   # Left
        postorder_traversal(node.right)  # Right
        print(node.data, end=' ')         # Current

def preorder_traversal(root):
    if root:
        print(root.data, end=' ')         # Current
        preorder_traversal(root.left)     # Left
        preorder_traversal(root.right)    # Right

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def insert_node(root, data):
    """Insert a new node into the binary tree."""
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert_node(root.left, data)
    else:
        root.right = insert_node(root.right, data)
    return root

def display_tree(node, level=0):
    """Display the tree structure using / and \\."""
    if node is not None:
        if node.right:
            display_tree(node.right, level + 1)
            print(" " * (level * 4) + " /")
        print(" " * (level * 4) + str(node.data))
        if node.left:
            print(" " * (level * 4) + " \\")
            display_tree(node.left, level + 1)

def get_valid_integer_list(prompt):
    """Get a valid list of integers from the user."""
    while True:
        try:
            # Split input by comma and convert to integers
            return [int(x.strip()) for x in input(prompt).split(',')]
        except ValueError:
            print("Invalid input. Please enter valid integers separated by commas.")

# Main execution
if __name__ == "__main__":
    root = None
    node_values = get_valid_integer_list("Enter values for nodes (separated by commas): ")

    for value in node_values:
        root = insert_node(root, value)

    print("\nTree structure:")
    display_tree(root)

    print("\nInorder traversal: ", end="")
    inorder_traversal(root)
    
    print("\nPostorder traversal: ", end="")
    postorder_traversal(root)
    
    print("\nPreorder traversal: ", end="")
    preorder_traversal(root)
    
    print("\nLevel Order Traversal: ", end="")
    level_order_traversal(root)

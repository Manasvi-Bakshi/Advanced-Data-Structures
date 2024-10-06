class BTreeNode:
    def __init__(self, t):
        self.t = t  # Minimum degree
        self.keys = []  # List of keys
        self.children = []  # List of children
        self.is_leaf = True  # True if leaf node

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(t)

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * root.t) - 1:  # Node is full
            new_node = BTreeNode(root.t)
            new_node.children.append(self.root)
            self.split_child(new_node, 0)
            self.insert_non_full(new_node, key)
            self.root = new_node
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.is_leaf:  # If leaf node
            node.keys.append(0)  # Add a dummy key
            while i >= 0 and key < node.keys[i]:  # Find the position to insert
                node.keys[i + 1] = node.keys[i]  # Shift key to right
                i -= 1
            node.keys[i + 1] = key  # Insert the key
        else:  # If not leaf
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * node.t) - 1:  # Child is full
                self.split_child(node, i)
                if key > node.keys[i]:  # Decide which child to insert into
                    i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        t = parent.t
        new_node = BTreeNode(t)
        child = parent.children[index]
        new_node.is_leaf = child.is_leaf
        parent.keys.insert(index, child.keys[t - 1])  # Move median key up
        parent.children.insert(index + 1, new_node)  # Link new child
        new_node.keys = child.keys[t:(2 * t) - 1]  # Give new node keys
        child.keys = child.keys[0:t - 1]  # Retain the first half in the old node
        if not child.is_leaf:
            new_node.children = child.children[t:2 * t]  # Move children to new node
            child.children = child.children[0:t]

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node.is_leaf:
            return 0
        return 1 + self._height(node.children[0])  # Height is the same for all children

    def display(self, node, level=0):
        print("  " * level + " ".join(map(str, node.keys)))
        if not node.is_leaf:
            for child in node.children:
                self.display(child, level + 1)

def main():
    t = int(input("Enter the minimum degree of the B-Tree: "))
    btree = BTree(t)
    
    values = input("Enter values separated by commas: ")
    for value in map(int, values.split(',')):
        btree.insert(value)

    print("\nB-Tree Structure:")
    btree.display(btree.root)
    print(f"\nHeight of the B-Tree: {btree.height()}")

if __name__ == "__main__":
    main()

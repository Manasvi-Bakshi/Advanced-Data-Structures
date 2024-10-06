class BPlusTreeNode:
    def __init__(self, t, leaf=False):
        self.t = t  # Minimum degree
        self.keys = []  # List of keys
        self.children = []  # List of child nodes
        self.leaf = leaf  # True if leaf node

class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(t, True)

    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * root.t) - 1:  # Node is full
            new_root = BPlusTreeNode(root.t)
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, key)
            self.root = new_root
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:  # If leaf node
            node.keys.append(0)  # Add a dummy key
            while i >= 0 and key < node.keys[i]:  # Find position to insert
                node.keys[i + 1] = node.keys[i]  # Shift keys to the right
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
        child = parent.children[index]
        new_node = BPlusTreeNode(t, child.leaf)
        parent.keys.insert(index, child.keys[t - 1])  # Move median key up
        parent.children.insert(index + 1, new_node)  # Link new child
        new_node.keys = child.keys[t:(2 * t) - 1]  # Give new node keys
        child.keys = child.keys[0:t - 1]  # Retain first half in the old node
        if not child.leaf:
            new_node.children = child.children[t:2 * t]  # Move children to new node
            child.children = child.children[0:t]

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node.leaf:
            return 0
        return 1 + self._height(node.children[0])  # Height is the same for all children

    def display(self, node, level=0):
        print("  " * level + " | ".join(map(str, node.keys)))
        if not node.leaf:
            for child in node.children:
                self.display(child, level + 1)

def main():
    t = int(input("Enter the minimum degree of the B+ Tree: "))
    bplustree = BPlusTree(t)

    values = input("Enter values separated by commas: ")
    for value in map(int, values.split(',')):
        bplustree.insert(value)

    print("\nB+ Tree Structure:")
    bplustree.display(bplustree.root)
    print(f"\nHeight of the B+ Tree: {bplustree.height()}")

if __name__ == "__main__":
    main()

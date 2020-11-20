
class Tree():

    def __init__(self):
        self.size = 0
        self.root = None
        self.items = []

    def get_size(self):
        return self.size

    def make(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        return node

    def insert(self, data, tree):
        if tree is None:
            tree = self.make(data)
        elif data < tree.data:
            self.insert(data, tree.left)
        else:
            self.insert(data, tree.right)
        self.size = self.size + 1

    def inorder(self, tree):
        if tree is None:
            return self.items
        self.inorder(tree.left)
        print(tree.data)
        self.inorder(tree.right)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

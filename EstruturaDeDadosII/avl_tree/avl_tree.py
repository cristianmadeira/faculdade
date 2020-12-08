from queue import Queue


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


class AVLTree(object):
    def do_rotation(self, fator_balanceamento, key, root):

        if fator_balanceamento > 1 and key < root.left.val:
            return self.right_rotate(root)

        if fator_balanceamento < -1 and key > root.right.val:
            return self.left_rotate(root)

        if fator_balanceamento > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if fator_balanceamento < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

    def maior_altura(self, root):
        return max(self.get_altura(root.left),
                   self.get_altura(root.right))

    def insert(self, root, key):

        if not root:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + self.maior_altura(root)

        balanco = self.get_balanceamento(root)
        if balanco >= -1 and balanco <= 1:
            return root
        else:
            return self.do_rotation(balanco, key, root)

    def delete(self, root, key):

        if not root:
            return root

        elif key < root.val:
            root.left = self.delete(root.left, key)

        elif key > root.val:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.get_first_value(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)

        if root is None:
            return root

        root.height = 1 + self.maior_altura(root)
        balanco = self.get_balanceamento(root)

        if balanco >= -1 and balanco <= 1:
            return root
        else:
            return self.do_rotation(balanco, key, root)

    def left_rotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + self.maior_altura(z)

        y.height = 1 + self.maior_altura(y)

        # Return the new root
        return y

    def right_rotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + self.maior_altura(z)

        y.height = 1 + self.maior_altura(y)

        # Return the new root
        return y

    def get_altura(self, root):
        if not root:
            return 0

        return root.height

    def get_balanceamento(self, root):
        if not root:
            return 0

        return self.get_altura(root.left) - self.get_altura(root.right)

    def get_first_value(self, root):
        if root is None or root.left is None:
            return root

        return self.get_first_value(root.left)

    def pre_order(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

    def percurso_nivel(self, root):
        if root is None:
            return

        queue = Queue()
        queue.push(root)

        while len(queue) > 0:
            node = queue.pop()

            if node.left is not None:
                queue.push(node.left)

            if node.right is not None:
                queue.push(node.right)

            print(node.val, end=" ")

import unittest


import unittest
from .tree import Tree


class TreeTest(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()

    def test_size(self):
        expected = 0
        result = self.tree.get_size()
        self.assertEqual(expected, result)

    def test_insert(self):
        data = 10
        result = self.tree.insert(data, tree=None)
        data = 5
        result = self.tree.insert(data, tree=result)
        expected = 2
        result = self.tree.get_size()
        self.assertEqual(expected, result)

    def test_inorder(self):
        tree = Tree()
        element1 = tree.insert(10, None)
        element2 = tree.insert(4, element1)
        element3 = tree.insert(11, element2)
        element4 = tree.insert(1, element3)
        print(tree.inorder(element1))


if __name__ == '__main__':
    unittest.main()

import unittest
from classes.stack import Stack
class StackTest(unittest.TestCase):
    
    def setUp(self):
        self.stack = Stack()

    def test_size(self):
        self.assertEquals(self.stack.size(),0)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
    
    def test_insert(self):
        element = 'Cristian'
        self.stack.insert(element)
        self.assertFalse(self.stack.is_empty())
        self.assertEquals(self.stack.size(),1)

    def test_remove(self):
        self.test_insert()
        expected = self.stack.remove()
        self.assertIsNotNone(expected)
        
if __name__ == '__main__':
    unittest.main()
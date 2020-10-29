import unittest
from .stack import Stack
class StackTest(unittest.TestCase):
    
    def setUp(self):
        self.stack = Stack()

    def test_size(self):
        self.assertEqual(self.stack.size,0)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
    
    def test_insert(self):
        element = 'Cristian'
        self.stack.insert(element)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(self.stack.size,1)

    def test_remove(self):
        self.stack.insert('Cristian')
        
        expected = 'Cristian'
        result = self.stack.remove()
        
        self.assertEqual(expected,result)
    def test_swap(self):
        var1,var2 = 'a','b'

        expected = ('b','a')
        result =self.stack.swap(var1,var2)

        self.assertEqual(expected,result)

    def test_sort(self):
        stack = Stack()

        stack.insert('d')
        stack.insert('c')
        stack.insert('a')
        stack.insert('b')
         
        expected = ['a','b','c','d']
        result = stack.sort()

        self.assertEqual(expected,result)

    def test_remove_stakc_is_empty(self):
        self.assertRaises(Exception,Stack().remove)
    
    def test_to_list_when_stack_is_empty(self):
        self.assertRaises(Exception,Stack().all)
    
    def test_all(self):
        stack = Stack()

        stack.insert('Cristian')
        stack.insert('Madeira')
        stack.insert('De')
        stack.insert('Souza')
        stack.insert('Pereira')
        
        
        expected = ['Pereira', 'Souza', 'De', 'Madeira', 'Cristian']
        result = stack.all()

        self.assertEqual(expected,result)
        self.assertEqual(stack.size,5)
        
if __name__ == '__main__':
    unittest.main()
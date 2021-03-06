import unittest
from .queue import Queue
class QueeuTest(unittest.TestCase):
    
    def setUp(self):
        self.queue = Queue()
    
    def test_size(self):
        result = self.queue.size
        expected = 0
        self.assertEqual(expected, result)

    def test_is_empty(self):
        result = self.queue.is_empty()
        self.assertTrue(result)
    
    def test_insert(self):
        element = 'Cristian Madeira de Souza Pereira'
        self.queue.insert(element)
        
        resulted_size = self.queue.size
        expected_size = 1
        resulted_is_empty = self.queue.is_empty()
        
        self.assertFalse(resulted_is_empty)
        self.assertEqual(expected_size,resulted_size)

    def test_remove(self):
        queue = Queue()
        queue.insert('Cristian')

        expected = 'Cristian'
        result = queue.remove()
        
        self.assertEqual(expected,result)
    def test_swap(self):
        var1,var2 = 'a','b'

        expected = ('b','a')
        result =self.queue.swap(var1,var2)

        self.assertEqual(expected,result)

    def test_sort(self):
        queue = Queue()

        queue.insert('d')
        queue.insert('c')
        queue.insert('a')
        queue.insert('b')
         
        expected = ['a','b','c','d']
        result = queue.sort()

        self.assertEqual(expected,result)

    def test_remove_queue_is_empty(self):
        self.assertRaises(Exception,Queue().remove)
    
    def test_to_list_when_queue_is_empty(self):
        self.assertRaises(Exception,Queue().all)
        
    def test_all(self):
        queue = Queue()
        
        queue.insert('Cristian')
        queue.insert('Madeira')
        queue.insert('De')
        queue.insert('Souza')
        queue.insert('Pereira')

        expected = ['Cristian','Madeira','De','Souza','Pereira']
        result = queue.all()

        self.assertEqual(expected,result)

    def test_find(self):
        queue = Queue()
        
        queue.insert('Cristian')
        queue.insert('Madeira')
        queue.insert('De')
        queue.insert('Souza')
        queue.insert('Pereira')
        queue.sort()

        expected = 'Cristian'
        result = queue.find('Cristian')

        self.assertEqual(expected,result)
    
    def test_find_when_element_greater_than_mid(self):
        queue = Queue()
        
        queue.insert('Cristian')
        queue.insert('Madeira')
        queue.insert('De')
        queue.insert('Souza')
        queue.insert('Pereira')
        queue.sort()

        expected = 'Souza'
        result = queue.find('Souza')

        self.assertEqual(expected,result)

    def test_find_when_list_is_empty(self):   
        self.assertRaises(Exception,Queue().find,'Cristian')
    
    def test_find_element_not_found(self):
        element = 'x'
        queue = Queue()
        
        queue.insert('b')
        queue.insert('a')
        queue.insert('c')
        
        queue.sort()
        self.assertRaises(Exception,queue.find,element)


    def test_get_items_size(self):
        self.assertEqual(0,Queue().get_items_size())
    
    def test_items_is_empty(self):
        self.assertTrue(Queue().items_is_empty())

        
if __name__ == '__main__':
    unittest.main()
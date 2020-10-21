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
        
        
if __name__ == '__main__':
    unittest.main()
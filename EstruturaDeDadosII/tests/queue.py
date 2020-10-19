import unittest
from classes.queue import Queue
class QueeuTest(unittest.TestCase):
    
    def setUp(self):
        self.queue = Queue()
    
    def test_size(self):
        result = self.queue.size()
        expected = 0
        self.assertEquals(expected, result)

    def test_is_empty(self):
        result = self.queue.is_empty()
        self.assertTrue(result)
    
    def test_insert(self):
        element = 'Cristian Madeira de Souza Pereira'
        self.queue.insert(element)
        
        resulted_size = self.queue.size()
        expected_size = 1
        resulted_is_empty = self.queue.is_empty()
        
        self.assertFalse(resulted_is_empty)
        self.assertEquals(expected_size,resulted_size)

    def test_remove(self):
        self.test_insert()
        
        expected = self.queue.items[0]
        result = self.queue.remove()
        
        self.assertEquals(expected,result)

if __name__ == '__main__':
    unittest.main()
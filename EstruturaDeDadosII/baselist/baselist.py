from abc import ABCMeta, abstractmethod
class BaseList(object):
    
    __metaclass__ = ABCMeta

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.size() == 0
    
    @abstractmethod
    def insert(self,element = None):
        pass
    
    def remove(self):
        element = self.items[0]
        self.items.remove(element)
        return element

    def all(self):
        return self.items
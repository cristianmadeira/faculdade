from abc import ABCMeta, abstractmethod

class BaseList(object):
    
    __metaclass__ = ABCMeta
    
    size = 0
    first_element = None

    def is_empty(self):
        return self.size == 0
    
    @abstractmethod
    def insert(self,element = None):
        pass
    
    def remove(self) :
        if self.is_empty():
            raise Exception('Está vazia!')
        else:
            element = self.first_element
            self.first_element = element.next
            self.size = self.size - 1
            return element.data

    def all(self):
        items = []
        if self.is_empty():
            raise Exception('Está vazia!')
        else:
            pointer = self.first_element
            while pointer != None:
                data = pointer.data
                pointer = pointer.next
                items.append(data)
            return items
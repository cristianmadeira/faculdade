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
    
    @abstractmethod
    def remove(self):
        pass

    def all(self):
        items = []
        pointer = self.first_element
        if pointer  == None:
            raise Exception('Está vazia!')
        else:
            while pointer != None:
                data = pointer.data
                pointer = pointer.next
                items.append(data)
            return items
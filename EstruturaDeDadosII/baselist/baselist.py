from abc import ABCMeta, abstractmethod

class BaseList(object):
    
    __metaclass__ = ABCMeta
    
    size = 0
    first_element = None
    last_element = None
    items = []

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
            data = element.data
            self.first_element = element.next
            self.size = self.size - 1
            del element
            return data

    def sort(self):
        if len(self.items) == 0:
            self.items = self.all()
        for i in range(self.size-1):
            j = i + 1
            while( j < self.size):
                if self.items[i] > self.items[j]:
                    self.items[i],self.items[j] = self.swap(self.items[i],self.items[j])
                j = j + 1
            i = i + 1
        return self.items

    def swap(self, var1, var2):
        aux = var1
        var1 = var2
        var2 = aux
        return var1,var2

    def all(self):
        self.items = []
        if self.is_empty():
            raise Exception('Está vazia!')
        else:
            element = self.first_element
            while element != None:
                data = element.data
                element = element.next
                self.items.append(data)
            return self.items
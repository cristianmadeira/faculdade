from .base_list import BaseList
class Stack(BaseList):
    def __init__(self):
        BaseList.__init__(self)

    def insert(self,element):
        self.items.append(element)
        
    def remove(self):
        return self.items.pop()


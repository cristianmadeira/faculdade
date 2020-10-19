from baselist.baselist import BaseList
class Stack(BaseList):
    def __init__(self):
        BaseList.__init__(self)

    def insert(self,element):
        aux = [element]
        self.items = aux + self.items
        

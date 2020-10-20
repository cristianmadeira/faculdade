from baselist.baselist import BaseList
class Stack(BaseList):
    
    def insert(self,element):
        aux = [element]
        self.items = aux + self.items
        

from baselist.baselist import BaseList
class Queue(BaseList):
    
    def insert(self,element):
        self.items.append(element)
    
    
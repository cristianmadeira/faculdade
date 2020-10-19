from base_list import BaseList
class Queue(BaseList):
    
    def insert(self,element):
        self.items.append(element)
    
    def remove(self):
        element = self.items[0]
        self.items.remove(element)
        return element
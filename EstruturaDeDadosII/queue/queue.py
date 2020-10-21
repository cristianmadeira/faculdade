from baselist.baselist import BaseList
from baselist.node import Node
class Queue(BaseList):
    
    def __init__(self):
        self.first_element = None
        self.last_element = None

    def insert(self,element):
        node = Node(element)

        if self.first_element == None:
            self.first_element = node
            self.last_element = node
        else:
            self.last_element.next = node
            node.prev = self.last_element
            self.last_element = node

        self.size = self.size + 1

    
    




    
    
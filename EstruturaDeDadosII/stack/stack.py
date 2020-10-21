from baselist.baselist import BaseList
from baselist.node import Node

class Stack(BaseList):
    
    def insert(self,element):
        node = Node(element)
        node.next = self.first_element
        self.first_element = node
        self.size = self.size + 1

    

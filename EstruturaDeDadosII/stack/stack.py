from baselist.baselist import BaseList
from baselist.node import Node

class Stack(BaseList):
    
    def __init__(self):
      self.first_element = None
        

    def insert(self,element):
        node = Node(element)
        node.next = self.first_element
        self.first_element = node
        self.size = self.size + 1

    def remove(self) :
        if self.is_empty():
            raise Exception('Pilha está vazia!')
        else:
            element = self.first_element
            self.first_element = element.next
            self.size = self.size - 1
            return element.data

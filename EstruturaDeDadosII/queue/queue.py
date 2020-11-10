from baselist.baselist import BaseList
from baselist.node import Node


class Queue(BaseList):
    def insert(self, element):
        node = Node(element)

        if self.first_element == None:
            self.first_element = node
            self.last_element = node
        else:
            self.last_element.next = node
            node.prev = self.last_element
            self.last_element = node

        self.size = self.size + 1

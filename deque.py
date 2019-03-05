"""
双端队列double-ended queue
"""

from .double_link_list import CircualDoubleLinkedList


class Deque(CircualDoubleLinkedList):

    def pop(self):
        if len(self) == 0:
            raise Exception('empty')

        tailnode = self.tailnode()
        value = tailnode.value
        self.remove(tailnode)
        return value

    def popleft(self):
        if len(self) == 0:
            raise Exception('empty')

        headnode = self.headnode()
        value = headnode.value
        self.remove(headnode)
        return value

"""
双端队列double-ended queue
"""

from .double_link_list import CircualDoubleLinkedList


class Deque(CircualDoubleLinkedList):
    def __init__(self, maxsize=None):
        super(Deque, self).__init__(maxsize)

    def pop(self):
        if self.root.next is self.root:
            raise Exception('empty')

        tailnode = self.tailnode()
        prevnode = tailnode.prev

        prevnode.next = self.root
        self.root.prev = prevnode

        del tailnode
        self.length -= 1

    def popleft(self):
        if self.root.next is self.root:
            raise Exception('empty')

        headnode = self.headnode()
        if headnode.next is self.root:
            # 只有一个head节点
            self.root.next = self.root
            self.root.prev = self.root
        else:
            self.root.next = headnode.next
            headnode.next.prev = self.root

        del headnode
        self.length -= 1

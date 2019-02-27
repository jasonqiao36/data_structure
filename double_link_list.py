class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next

    def __repr__(self):
        return f'Node(value={self.value})'


class CircualDoubleLinkedList:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        if self.maxsize is not None and self.length > self.maxsize:
            raise Exception('full')
        node = Node(value)
        tailnode = self.tailnode()

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node

        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and self.length > self.maxsize:
            raise Exception('full')

        headnode = self.headnode()
        node = Node(value)
        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            self.root.next = node
            node.prev = self.root
            node.next = headnode
            headnode.prev = node

        self.length += 1

    def remove(self, node):  # O(1), node is not value
        if node is self.root:
            return
        else:
            prevnode = node.prev
            nextnode = node.next
            prevnode.next = nextnode
            nextnode.prev = prevnode

        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return

        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    # def iter_node(self):
    #     if self.root.next is self.root:
    #         return
    #     curnode = self.root.next
    #     while curnode is not self.tailnode():
    #         yield curnode
    #         curnode = curnode.next
    #     yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        if self.root.next is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

    # def iter_node_reverse(self):
    #     if self.root.next is self.root:
    #         return
    #
    #     curnode = self.root.prev
    #     while curnode is not self.root:
    #         yield curnode
    #         curnode = curnode.prev


def test_double_linked_list():
    dll = CircualDoubleLinkedList()
    assert len(dll) == 0

    dll.append(0)
    dll.append(1)
    dll.append(2)

    assert len(dll) == 3

    assert list(dll) == [0, 1, 2]

    assert [node.value for node in dll.iter_node()] == [0, 1, 2]
    assert [node.value for node in dll.iter_node_reverse()] == [2, 1, 0]

    headnode = dll.headnode()
    assert headnode.value == 0
    dll.remove(headnode)  # O(1)
    assert len(dll) == 2
    assert [node.value for node in dll.iter_node()] == [1, 2]

    dll.appendleft(0)
    assert [node.value for node in dll.iter_node()] == [0, 1, 2]

# if __name__ == '__main__':
#     dll = CircualDoubleLinkedList()
#     dll.append(0)
#     dll.append(1)
#     dll.append(2)
#
#     for node in dll.iter_node_reverse():
#         print(node.value)

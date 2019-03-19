def print_n(n):
    for i in range(1, n + 1):
        print(i)


# print_n(100)


def print_num_recursive(n):
    if n > 0:
        print_num_recursive(n - 1)
        print(n)


# print_num_recursive(100)


from collections import deque


class Stack:
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.pop()

    def is_empty(self):
        return len(self._deque) == 0


def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1

    while not s.is_empty():
        s.pop()


print_num_recursive(10)

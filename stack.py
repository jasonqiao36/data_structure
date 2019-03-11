from .deque import Deque


class Stack:
    def __init__(self):
        self.deque = Deque()

    def push(self, value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def __len__(self):
        return len(self.deque)

    def is_empty(self):
        return len(self) == 0


def test_stack():
    s = Stack()

    s.push(0)
    s.push(1)
    s.push(2)

    assert len(s) == 3
    assert s.is_empty() is False

    assert s.pop() == 2
    assert s.pop() == 1
    assert s.pop() == 0

    assert len(s) == 0
    assert s.is_empty() is True

    import pytest
    with pytest.raises(Exception) as excinfo:
        s.pop()

    assert 'empty' in str(excinfo.value)

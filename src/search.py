l = ['a', 'b', 'c', 'd', 'e', 'f']


def liner_search(value, iterable):
    for index, item in enumerate(iterable):
        if item == value:
            return index
    return -1


def liner_search_v2(predicate, iterable):
    for index, item in enumerate(iterable):
        if predicate(item):
            return index
    return -1


def liner_search_recursive(iterable, value):
    if len(iterable) == 0:
        return -1
    index = len(iterable) - 1
    if iterable[index] == value:
        return index
    return liner_search_recursive(iterable[:index], value)


def binary_search(sorted_array, val):
    if not sorted_array:
        return -1
    beg = 0
    end = len(sorted_array) - 1
    mid = int((beg + end) / 2)
    while beg <= end:
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            beg = mid + 1
    return -1


def binary_search_recursive(sorted_array, val):
    if not sorted_array:
        return -1

    beg = 0
    end = len(sorted_array) - 1
    if beg >= end:
        return -1
    mid = int((beg + end) / 2)

    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        return binary_search_recursive(sorted_array[:mid - 1], val)
    else:
        return binary_search_recursive(sorted_array[mid + 1:], val)


def binary_search_insert(sorted_array, val):
    if not sorted_array:
        return -1

    beg = 0
    end = len(sorted_array) - 1
    mid = int((beg + end) / 2)

    while beg <= end:
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] >= val:
            end = mid - 1
        else:
            beg = mid + 1


def test_binary_search():
    l = list(range(10))

    assert binary_search(l, 3) == 3
    assert binary_search(l, 0) == 0
    assert binary_search(l, -3) == -1
    assert binary_search(None, 3) == -1


def test_binary_search_recursive():
    l = list(range(10))

    assert binary_search_recursive(l, 3) == 3
    assert binary_search_recursive(l, 0) == 0
    assert binary_search_recursive(l, -3) == -1
    assert binary_search_recursive(None, 3) == -1


def test_liner_search():
    assert liner_search('e', l) == 4


def test_liner_search_v2():
    assert liner_search_v2(lambda x: x == 'e', l) == 4


def test_liner_search_recursive():
    l = list(range(8))

    assert liner_search_recursive(l, 5) == 5
    assert liner_search_recursive(l, 9) == -1
    assert liner_search_recursive(l, 7) == 7
    assert liner_search_recursive(l, 0) == 0

import bisect
import random


def bubble_sort(seq):  # O(n2)
    n = len(seq)
    # 外层循环控制从头走到尾的次数
    for i in range(n - 1):
        print(seq)
        # 内层循环控制走一次的过程
        for j in range(n - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq


def test_bubble_sort():
    seq = list(range(10))
    random.shuffle(seq)
    bubble_sort(seq)
    assert seq == sorted(seq)


def select_sort(seq):  # O(n2)
    n = len(seq)
    for i in range(n - 1):
        print(seq)
        min_idx = i
        for j in range(i + 1, n):
            if seq[j] < seq[min_idx]:
                min_idx = j
        if min_idx != i:  # 如果已经排好序，min_idx==i，这时候不用换位置
            seq[i], seq[min_idx] = seq[min_idx], seq[i]


def test_select_sort():
    seq = list(range(10))
    random.shuffle(seq)
    select_sort(seq)
    assert seq == sorted(seq)


def insertion_sort(seq):  # O(n2)
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        poi = i
        while poi > 0 and value < seq[poi - 1]:
            seq[poi] = seq[poi - 1]
            poi -= 1
        seq[poi] = value
        print(seq)


def test_insertion_sort():
    seq = list(range(10))
    random.shuffle(seq)
    insertion_sort(seq)
    assert seq == sorted(seq)


def insertion_sort_reverse(seq):
    """从大到小"""
    n = len(seq)
    for i in range(1, n):
        value = seq[i]
        poi = i
        while poi > 0 and value > seq[poi - 1]:
            seq[poi] = seq[poi - 1]
            poi -= 1
        seq[poi] = value


def test_insertion_sort_reverse():
    seq = list(range(10))
    random.shuffle(seq)
    insertion_sort_reverse(seq)
    assert seq == sorted(seq, reverse=True)

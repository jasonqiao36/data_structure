from .hashtable import HashTable


class SetADT(HashTable):

    def add(self, key):
        # 集合其实就是一个 dict，只不过我们把它的 value 设置成 1
        return super(SetADT, self).add(key, True)

    def __and__(self, other_set):
        """交集 A&B"""
        new_set = SetADT()
        for element_a in self:
            if element_a in other_set:
                new_set.add(element_a)
        return new_set

    def __sub__(self, other_set):
        """差集 A-B"""
        new_set = SetADT()
        for element_a in self:
            if element_a not in other_set:
                new_set.add(element_a)
        return new_set

    def __or__(self, other_set):
        """并集 A|B"""
        new_set = SetADT()
        for element_a in self:
            new_set.add(element_a)
        for element_b in other_set:
            new_set.add(element_b)
        return new_set


def test_set_adt():
    sa = SetADT()
    sa.add(1)
    sa.add(2)
    sa.add(3)

    assert 1 in sa

    sb = SetADT()
    sb.add(3)
    sb.add(4)
    sb.add(5)

    assert sorted(list(sa & sb)) == [3]
    assert sorted(list(sa | sb)) == [1, 2, 3, 4, 5]
    assert sorted(list(sa - sb)) == [1, 2]

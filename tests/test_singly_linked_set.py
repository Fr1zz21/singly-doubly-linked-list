from src.singly_linked_set import MySet, Node


def test_repr():
    a = MySet(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    assert str(a) == "{1, 2, 3, 4, 5}"


def test_add():
    a = MySet(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    b = MySet()

    a.add(6)
    b.add(9)

    assert 6 in a
    assert str(a) == "{1, 2, 3, 4, 5, 6}"

    assert 9 in b
    assert str(b) == "{9}"


def test_len():
    a = MySet(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    assert len(a) == 5


def test_contains():
    a = MySet(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    assert 4 in a
    assert 7 not in a


def test_intersect():
    a = MySet(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    b = MySet(Node(3, Node(9, Node(8, Node(1, Node(7))))))

    result = a.intersect(b)

    assert len(result) == 2
    assert 1 in result
    assert 3 in result
    assert 5 not in result
    assert 8 not in result


def test_union():
    a = MySet(Node(1, Node(2, Node(3, Node(4, Node(5))))))
    b = MySet(Node(3, Node(9, Node(8, Node(1, Node(7))))))

    result = a.union(b)

    assert 1 in result
    assert 2 in result
    assert 3 in result
    assert 4 in result
    assert 5 in result
    assert 7 in result
    assert 8 in result
    assert 9 in result
    assert len(result) == 8
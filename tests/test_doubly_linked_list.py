from src.doubly_linked_list import DoublyLinkedList


def test_doubly_add():
    d = DoublyLinkedList()
    d.add(1)
    d.add(2)
    d.add(3)

    assert 1 in d
    assert 2 in d
    assert 3 in d
    assert len(d) == 3


def test_doubly_len():
    d = DoublyLinkedList()
    d.add(1)
    d.add(2)
    d.add(3)
    d.add(4)
    d.add(5)

    assert len(d) == 5


def test_doubly_contains():
    d = DoublyLinkedList()
    d.add(1)
    d.add(2)
    d.add(3)

    assert 2 in d
    assert 99 not in d


def test_doubly_contains_method():
    d = DoublyLinkedList()
    d.add(1)
    d.add(2)
    d.add(3)

    assert d.contains(3) is True
    assert d.contains(99) is False


def test_doubly_repr():
    d = DoublyLinkedList()
    d.add(1)
    d.add(2)
    d.add(3)

    assert str(d) == "{1, 2, 3}"


def test_doubly_empty():
    d = DoublyLinkedList()

    assert len(d) == 0
    assert str(d) == "{}"
    assert 5 not in d
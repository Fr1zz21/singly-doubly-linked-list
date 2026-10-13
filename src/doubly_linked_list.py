from typing import Optional


class Node2:
    def __init__(self, value: int, next: Optional['Node2'] = None,
                 prev: Optional['Node2'] = None) -> None:
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node2] = None
        self.tail: Optional[Node2] = None

    def add(self, value: int) -> None:
        """Добавляем элемент в конец."""
        new_node = Node2(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def __len__(self) -> int:
        """Вывод длины."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __contains__(self, item: int) -> bool:
        """Проверка вхождения через магический метод."""
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            current = current.next
        return False

    def contains(self, item: int) -> bool:
        """Проверка вхождения обычным методом."""
        return item in self

    def __repr__(self) -> str:
        """Вывод элементов списка."""
        spis = []
        current = self.head
        while current is not None:
            spis.append(str(current.value))
            current = current.next
        return '{' + ', '.join(spis) + '}'
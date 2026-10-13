from typing import Optional


class Node:
    def __init__(self, value: int, next: Optional['Node'] = None) -> None:
        self.value = value
        self.next = next


class MySet:
    def __init__(self, head: Optional['Node'] = None) -> None:
        self.head = head

    def add(self, value: int) -> None:
        """Добавляем элемент, если его ещё нет."""
        if self.head is None:
            self.head = Node(value)
            return

        current = self.head
        while current is not None:
            if current.value == value:
                return
            if current.next is None:
                current.next = Node(value)
                return
            current = current.next

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
        """Вывод элементов множества."""
        spis = []
        current = self.head
        while current is not None:
            spis.append(str(current.value))
            current = current.next
        return '{' + ', '.join(spis) + '}'

    def intersect(self, second_set: 'MySet') -> 'MySet':
        """Пересечение двух множеств."""
        current = self.head
        result = MySet()
        while current is not None:
            if current.value in second_set:
                result.add(current.value)
            current = current.next
        return result

    def union(self, second_set: 'MySet') -> 'MySet':
        """Объединение двух множеств."""
        result = MySet()

        current = self.head
        while current is not None:
            result.add(current.value)
            current = current.next

        current = second_set.head
        while current is not None:
            result.add(current.value)
            current = current.next

        return result
import time

from src.singly_linked_set import MySet
from src.doubly_linked_list import DoublyLinkedList


def benchmark_my_set_add(n: int = 10000) -> None:
    """Замер добавления n элементов в MySet."""
    start = time.time()

    a = MySet()
    for i in range(n):
        a.add(i)

    end = time.time()
    print(f"MySet.add({n} элементов): {end - start:.4f} секунд")


def benchmark_my_set_contains(n: int = 10000) -> None:
    """Замер поиска последнего элемента в MySet."""
    a = MySet()
    for i in range(n):
        a.add(i)

    start = time.time()
    result = (n - 1) in a
    end = time.time()

    print(f"MySet.__contains__ (последний из {n}): {end - start:.6f} секунд")
    print(f"  Найдено: {result}")


def benchmark_doubly_add(n: int = 10000) -> None:
    """Замер добавления n элементов в DoublyLinkedList."""
    start = time.time()

    d = DoublyLinkedList()
    for i in range(n):
        d.add(i)

    end = time.time()
    print(f"DoublyLinkedList.add({n} элементов): {end - start:.4f} секунд")


def benchmark_doubly_contains(n: int = 10000) -> None:
    """Замер поиска последнего элемента в DoublyLinkedList."""
    d = DoublyLinkedList()
    for i in range(n):
        d.add(i)

    start = time.time()
    result = (n - 1) in d
    end = time.time()

    print(f"DoublyLinkedList.__contains__ (последний из {n}): {end - start:.6f} секунд")
    print(f"  Найдено: {result}")


if __name__ == "__main__":
    print("=" * 60)
    print("  Бенчмарки для односвязного множества (MySet)")
    print("=" * 60)
    benchmark_my_set_add()
    benchmark_my_set_contains()

    print()
    print("=" * 60)
    print("  Бенчмарки для двусвязного списка (DoublyLinkedList)")
    print("=" * 60)
    benchmark_doubly_add()
    benchmark_doubly_contains()
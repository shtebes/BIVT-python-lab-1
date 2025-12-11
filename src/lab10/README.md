# Лабораторная работа 10
> **Цель:** Реализовать базовые структуры данных (стек, очередь, связный список), сравнить их производительность и научиться думать в терминах асимптотики (O(1), O(n)).

## Теория
### Стек (Stack)
Стек - это структура данных, работающая по принципу LIFO (Last In First Out - последним пришел, первым ушел). Основные операции:
- `push(item)` - добавить элемент на вершину стека
- `pop()` - снять элемент с вершины стека
- `peek()` - посмотреть элемент на вершине без удаления
- `is_empty()` - проверить, пуст ли стек

**Сложность операций**: O(1) для всех основных операций

### Очередь (Queue)
Очередь - это структура данных, работающая по принципу FIFO (First In First Out - первым пришел, первым ушел). Основные операции:
- `enqueue(item)` - добавить элемент в конец очереди
- `dequeue()` - взять элемент из начала очереди
- `peek()` - посмотреть элемент в начале без удаления
- `is_empty()` - проверить, пуста ли очередь

**Сложность операций**: O(1) для всех основных операций

### Односвязный список (Singly Linked List)
Связный список - это линейная структура данных, состоящая из узлов, где каждый узел содержит значение и ссылку на следующий узел. Основные операции:
- `append(value)` - добавить в конец
- `prepend(value)` - добавить в начало
- `insert(idx, value)` - вставить по индексу
- `remove(value)` - удалить первое вхождение
- `remove_at(idx)` - удалить по индексу

**Сложность операций**:
- Добавление в начало/конец (с tail): O(1)
- Добавление в конец (без tail): O(n)
- Вставка/удаление по индексу: O(n) в худшем случае
- Поиск элемента: O(n)

## Задание A. Реализация Stack и Queue
```python
from collections import deque

class Stack:
    def __init__(self):
        # внутреннее хранилище стека
        self._data = []

    def push(self, item):
        # корректно: добавление в конец списка O(1) амортизированно
        self._data.append(item)

    def pop(self):
        if len(self._data) == 0:
            raise IndexError("Ошибка: Нельзя удалить элемент из пустого stack")
        return self._data.pop()

    def peek(self):
        # возвращает верхний элемент без удаления
        if len(self._data) == 0:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self) -> int:
        return len(self._data)


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        # добавление элемента в конец очереди
        self._data.append(item)

    def dequeue(self):
        # взять элемент из начала очереди и вернуть его
        if self.is_empty():
            raise IndexError("Ошибка: Нельзя удалить элемент из пустой очереди")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self) -> int:
        return len(self._data)
```

## Задание B. Реализация SinglyLinkedList 
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        """Добавить элемент в конец списка"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка"""
        new_node = Node(value, next=self.head)e
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1

    def insert(self, idx, value):
        """Вставка по индексу"""
        if idx < 0 or idx > self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size}]")
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        # Вставка в середину
        new_node = Node(value)
        current = self.head
        for i in range(idx - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def remove(self, idx):
        """Удалить элемент по индексу"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Индекс {idx} вне диапазона [0, {self._size - 1}]")
        
        # Удаление из головы
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return value
        # Удаление из середины или конца
        current = self.head
        for i in range(idx - 1):
            current = current.next
        value = current.next.value
        if current.next == self.tail:
            self.tail = current
        current.next = current.next.next
        self._size -= 1
        return value

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

```

**пример использования:**
![скриншот 1](./images/lab10/test.png)

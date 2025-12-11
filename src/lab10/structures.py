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
            return ("Ошибка: Нельзя удалить элемент из пустого stack")
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
    
    def __str__(self):
        return f"Stack({self._data})"

class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        # добавление элемента в конец очереди
        self._data.append(item)

    def dequeue(self):
        # взять элемент из начала очереди и вернуть его
        if self.is_empty():
            return ("Ошибка: Нельзя удалить элемент из пустой очереди")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0
    
    def __len__(self) -> int:
        return len(self._data)
    
    def __str__(self):
        return f"Queue({list(self._data)})"
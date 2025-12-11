from structures import Stack, Queue
from linked_list import SinglyLinkedList

def test_stack():
    print("=== Тестирование Stack ===")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Стек: {s}")
    print(f"Вершина: {s.peek()}")
    print(f"Pop: {s.pop()}")
    print(f"Размер: {len(s)}")
    print(f"Пуст? {s.is_empty()}")
    print(f"Pop: {s.pop()}")
    print(f"Pop: {s.pop()}")
    print(f"Pop: {s.pop()}")

def test_queue():
    print("\n=== Тестирование Queue ===")
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    print(f"Очередь: {q}")
    print(f"Первый: {q.peek()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Размер: {len(q)}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Dequeue: {q.dequeue()}")

def test_linked_list():
    print("\n=== Тестирование SinglyLinkedList ===")
    lst = SinglyLinkedList()
    lst.append(10)
    lst.append(20)
    lst.prepend(5)
    lst.insert(2, 15)
    
    print(f"Список: {lst}")
    print(f"Элементы: {list(lst)}")
    print(f"Размер: {len(lst)}")
    
    lst.remove(2)
    
    print(f"Удален элемент по индексу 2: {lst.remove(2)}")
    print(f"Итоговый список: {list(lst)}")

if __name__ == "__main__":
    test_stack()
    test_queue()
    test_linked_list()
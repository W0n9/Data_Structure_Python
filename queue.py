from typing import Union


class Node(object):
    def __init__(self, elem, next=None) -> None:
        self.elem = elem
        self.next = next


class Queue(object):
    def __init__(self) -> None:
        self.head = None
        self.rear = None

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, elem):
        '''
        入队
        '''
        p = Node(elem)
        if self.is_empty():
            self.head = p  # 新增一个节点
            self.rear = p
        else:
            self.rear.next = p
            self.rear = p

    def dequeue(self) -> int:
        if self.is_empty():
            return
        else:
            p = self.head.elem
            self.head = self.head.next
            return p

    def peek(self) -> Union[bool or int]:
        if self.is_empty():
            return
        else:
            return self.head.elem

    def print_quene(self):
        result = []
        p = self.head
        while p is not None:
            result.append(p.elem)
            p = p.next
        print(result)


class Queue_array():
    def __init__(self):
        self.entries = []  # 表示队列内的参数
        self.length = 0  # 表示队列的长度
        self.front = 0  # 表示队列头部位置

    def enqueue(self, item):
        self.entries.append(item)  # 添加元素到队列里面
        self.length = self.length + 1  # 队列长度增加 1

    def dequeue(self):
        self.length = self.length - 1  # 队列的长度减少 1
        dequeued = self.entries[self.front]  # 队首元素为dequeued
        self.front -= 1  # 队首的位置减少1
        self.entries = self.entries[self.front:]  # 队列的元素更新为退队之后的队列
        return dequeued

    def peek(self):
        return self.entries[0]  # 直接返回队列的队首元素


if __name__ == "__main__":
    data = [21, 35, 58, 13]
    queue = Queue()
    for i in data:
        queue.enqueue(i)
    queue.print_quene()
    print(queue.peek())
    queue.dequeue()
    print(queue.peek())
    queue.print_quene()
import sys

class LinkedListQueue:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, capacity=sys.maxsize):
        self.head = self.Node(None)  # 哨兵
        self.tail = self.head
        self.tail.next = self.head
        
        self.size = 0
        self.capacity = capacity  # 一般都要指定队列容量, 这里默认是int max
        
    # 在队列尾部插入
    def offer(self, value):
        if self.isFull():
            return False
        added = self.Node(value, self.head)
        self.tail.next = added
        self.tail = added  # 新节点是tail
        self.size += 1
        return True

    # 获取队头的值(同时移除)
    def poll(self):
        if self.isEmpty():
            return None
        first = self.head.next
        self.head.next = first.next
        if first == self.tail:
            self.tail = self.head
        self.size -= 1
        return first.value

    # 获取队头的值(但不移除)
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value

    # 检查队列是否为空
    def isEmpty(self):
        return self.head == self.tail

    # 检查队列是否已满
    def isFull(self):
        return self.size == self.capacity

    # 遍历
    def __iter__(self):
        p = self.head.next
        while p != self.head:
            print(p.value, end=' ')
            p = p.next
        print()



queue = LinkedListQueue(4)
queue.offer(1)
queue.offer(2)
queue.offer(3)
queue.offer(4)
print(queue.offer(5))
queue.__iter__()
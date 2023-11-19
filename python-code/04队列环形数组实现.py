import sys

# 环形链表有一个空位
'''
class ArrayQueue1:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, capacity=sys.maxsize):
        self.head = 0
        self.tail = 0
        self.array = [None] * (capacity + 1)
        self.capacity = capacity
        
    # 在队列尾部插入
    def offer(self, value):
        if self.isFull():
            return False
        self.array[self.tail] = value
        self.tail = (self.tail + 1) % len(self.array)
        return True

    # 获取队头的值(同时移除)
    def poll(self):
        if self.isEmpty():
            return None
        value = self.array[self.head]
        self.head = (self.head + 1) % len(self.array)
        return value

    # 获取队头的值(但不移除)
    def peek(self):
        if self.isEmpty():
            return None
        return self.array[self.head]

    # 检查队列是否为空
    def isEmpty(self):
        return self.head == self.tail

    # 检查队列是否已满
    def isFull(self):
        return (self.tail + 1) % len(self.array) == self.head

    # 遍历
    def __iter__(self):
        p = self.head
        while p != self.tail:
            print(self.array[p], end=' ')
            p = (p + 1) % len(self.array)
        print()
'''

# 引入size属性, 不需要capacity+1
'''
class ArrayQueue2:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, capacity=sys.maxsize):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.array = [None] * capacity
        self.capacity = capacity
        
    # 在队列尾部插入
    def offer(self, value):
        if self.isFull():
            return False
        self.array[self.tail] = value
        self.tail = (self.tail + 1) % len(self.array)
        self.size += 1
        return True

    # 获取队头的值(同时移除)
    def poll(self):
        if self.isEmpty():
            return None
        value = self.array[self.head]
        self.head = (self.head + 1) % len(self.array)
        self.size -= 1
        return value

    # 获取队头的值(但不移除)
    def peek(self):
        if self.isEmpty():
            return None
        return self.array[self.head]

    # 检查队列是否为空
    def isEmpty(self):
        return self.size == 0

    # 检查队列是否已满
    def isFull(self):
        return self.size == len(self.array)

    # 遍历
    def __iter__(self):
        p = self.head
        count = 0  # 遍历个数
        while count < self.size:
            print(self.array[p], end=' ')
            p = (p + 1) % len(self.array)
            count += 1
        print()
'''


# head tail只是不断递增的数(本身不是索引)，需要使用时再进行取模换算
class ArrayQueue3:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, capacity=sys.maxsize):
        self.head = 0
        self.tail = 0
        self.array = [None] * capacity
        self.capacity = capacity
        
    # 在队列尾部插入
    def offer(self, value):
        if self.isFull():
            return False
        self.array[self.tail % len(self.array)] = value
        self.tail += 1
        return True

    # 获取队头的值(同时移除)
    def poll(self):
        if self.isEmpty():
            return None
        value = self.array[self.head % len(self.array)]
        self.head += 1
        return value

    # 获取队头的值(但不移除)
    def peek(self):
        if self.isEmpty():
            return None
        return self.array[self.head % len(self.array)]

    # 检查队列是否为空
    def isEmpty(self):
        return self.head == self.tail

    # 检查队列是否已满
    def isFull(self):
        return self.tail - self.head == len(self.array)

    # 遍历
    def __iter__(self):
        p = self.head
        while p != self.tail:
            print(self.array[p % len(self.array)], end=' ')
            p += 1
        print()


queue = ArrayQueue3(4)
queue.offer(1)
queue.offer(2)
queue.offer(3)
print(queue.offer(4))
print(queue.poll())
queue.__iter__()
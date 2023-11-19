class DequeArray:
    def __init__(self, capacity):
        self.array = [None] * (capacity + 1)  # tail位置不存储元素，因此要+1
        self.head = self.tail = 0
    
    def isEmpty(self):
        return self.head == self.tail
    
    def isFull(self):
        if self.tail > self.head:
            # head 向右 -> 一直到tail是元素的个数
            '''
            head
                              tail
            a     b     c     None  <- addLast
            '''
            return self.tail - self.head == len(self.array)
        elif self.tail < self.head:
            '''
                   head          
            tail
            None    c     b     a    -> addFirst
            '''
            return self.head - self.tail == 1
        else:  # head==tail代表empty
            return False
    
    def offerLast(self, value):
        if self.isFull():
            return False
        self.array[self.tail] = value
        self.tail = self.increment(self.tail)  # tail++
        return True
    
    def offerFirst(self, value):
        if self.isFull():
            return False
        self.head = self.decrement(self.head)  # head--
        self.array[self.head] = value
        return True
    
    def pollFirst(self):
        if self.isEmpty():
            return None
        removed = self.array[self.head]
        # 内存释放 help GC
        self.array[self.head] = None
        self.head = self.increment(self.head)
        return removed
    
    def pollLast(self):
        if self.isEmpty():
            return None
        self.tail = self.decrement(self.tail)
        removed = self.array[self.tail]
        # 内存释放 help GC
        self.array[self.tail] = None
        return removed
    
    def peekFirst(self):
        if self.isEmpty():
            return None
        return self.array[self.head]
    
    def peekLast(self):
        if self.isEmpty():
            return None
        return self.array[self.decrement(self.tail)]
    
    # 两个换算索引的工具方法
    def increment(self, i):  # 处理+1后的越界
        if i + 1 >= len(self.array):
            return 0
        return i + 1
    
    def decrement(self, i):  # 处理-1时的越界
        if i - 1 < 0:
            return len(self.array) - 1
        return i - 1

    def __iter__(self):
        p = self.head
        while p != self.tail:
            print(self.array[p], end=' ')
            p = self.increment(p)
        print()


deque = DequeArray(7)
print(deque.isEmpty())
deque.offerLast(1)
deque.offerLast(2)
deque.offerLast(3)
deque.offerFirst(4)
deque.offerFirst(5)
deque.offerFirst(6)
deque.offerFirst(7)
print(deque.isFull())
deque.__iter__()

print(deque.pollFirst())
print(deque.pollFirst())
print(deque.pollLast())
print(deque.pollLast())
print(deque.pollLast())
print(deque.pollLast())
print(deque.pollLast())
print(deque.pollLast())
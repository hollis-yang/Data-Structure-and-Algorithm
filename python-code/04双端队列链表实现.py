class Deque:
    class Node:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev

    def __init__(self, capacity):
        self.sentinel = self.Node(None)  # 哨兵
        # 哨兵的prev和next都指向自己
        self.sentinel.next = self.sentinel.prev = self.sentinel
        self.capacity = capacity
        self.size = 0
    
    def __iter__(self):
        p = self.sentinel.next  # 环形链表遍历时不需要特判isEmpty
        while p != self.sentinel:
            value = p.value
            p = p.next
            print(value, end=' ')
        print()
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity

    def offerFirst(self, value):
        if self.isFull():
            return False
        a = self.sentinel
        b = self.sentinel.next
        added = self.Node(value, b, a)
        a.next = added
        b.prev = added
        self.size += 1
        return True
    
    def offerLast(self, value):
        if self.isFull():
            return False
        a = self.sentinel.prev
        b = self.sentinel
        added = self.Node(value, b, a)
        a.next = added
        b.prev = added
        self.size += 1
        return True
    
    def pollFirst(self):
        if self.isEmpty():
            return None
        a = self.sentinel
        removed = self.sentinel.next
        b = removed.next
        a.next = b
        b.prev = a
        self.size -= 1
        return removed.value
    
    def pollLast(self):
        if self.isEmpty():
            return None
        a = self.sentinel.prev.prev
        removed = a.next
        b = self.sentinel
        a.next = b
        b.prev = a
        self.size -= 1
        return removed.value
    
    def peekFirst(self):
        if self.isEmpty():
            return None
        return self.sentinel.next.value
    
    def peekLast(self):
        if self.isEmpty():
            return None
        return self.sentinel.prev.value


deque = Deque(5)
deque.offerFirst(1)
deque.offerFirst(2)
deque.offerFirst(3)
deque.offerLast(4)
deque.offerLast(5)
print(deque.offerLast(6))
deque.__iter__()

print(deque.pollFirst())
print(deque.pollFirst())
print(deque.pollLast())
print(deque.pollLast())
print(deque.pollLast())

print(deque.isEmpty())
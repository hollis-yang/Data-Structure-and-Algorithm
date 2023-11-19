class MyCircularDeque:

    def __init__(self, k: int):
        self.capacity = k
        self.head = self.tail = 0
        self.array = [None] * (k + 1)

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = self.decrement(self.head)
        self.array[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.array[self.tail] = value
        self.tail = self.increment(self.tail)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.array[self.head] = None
        self.head = self.increment(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = self.decrement(self.tail)
        self.array[self.tail] = None
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.array[self.decrement(self.tail)]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        if self.tail > self.head:
            return self.tail - self.head == len(self.array)
        elif self.tail < self.head:
            return self.head - self.tail == 1
        else:
            return False

    def increment(self, i):
        if i + 1 == len(self.array):
            return 0
        return i + 1
    
    def decrement(self, i):
        if i - 1 < 0:
            return len(self.array) - 1
        return i - 1

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.array = [None] * (k + 1)
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.array[self.tail] = value
        self.tail = (self.tail + 1) % len(self.array)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % len(self.array)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.array[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.array[(self.tail - 1) % len(self.array)]

    def isEmpty(self) -> bool:
        return self.head == self.tail

    def isFull(self) -> bool:
        return (self.tail + 1) % len(self.array) == self.head



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
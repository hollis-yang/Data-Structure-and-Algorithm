# 每一个带优先级的元素
class Priority:
        def __init__(self, value, p):
            self.value = value
            self.priority = p

class PriorityQueue:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0  # 可以理解成尾指针
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == len(self.array)
    
    # O(1)
    def offer(self, p):  # p -> class Priority
        if self.isFull():
            return False
        self.array[self.size] = p
        self.size += 1
        return True

    # 双指针返回优先级最高的索引 用于poll和peek
    def select_max(self):
        max = 0
        for i in range(1, self.size):
            if self.array[i].priority > self.array[max].priority:
                max = i
        return max

    # O(n)
    def peek(self):
        if self.isEmpty():
            return None
        max = self.select_max()
        return self.array[max]
    
    # O(n)
    def poll(self):
        if self.isEmpty():
            return None
        max = self.select_max()
        e = self.array[max]
        self.remove(max)
        return e

    def remove(self, index):
        if index < self.size - 1:  # 不是删最后一个元素的话需要移动后续元素
            self.array = self.array[:index] + self.array[index + 1:]
        self.size -= 1
        # help GC
        self.array[self.size] = None


queue = PriorityQueue(5)
queue.offer(Priority('task1', 4))
queue.offer(Priority('task2', 3))
queue.offer(Priority('task3', 2))
queue.offer(Priority('task4', 5))
queue.offer(Priority('task5', 1))
print(queue.poll().value)
print(queue.poll().value)
print(queue.poll().value)
print(queue.poll().value)
print(queue.poll().value)
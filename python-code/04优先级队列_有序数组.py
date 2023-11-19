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
    
    # O(n)
    def offer(self, p):  # p -> class Priority
        if self.isFull():
            return False
        # 插入排序找到对应位置
        self.insert(p)
        self.size += 1
        return True
    
    def insert(self, p):
        i = self.size - 1
        while i >= 0:
            if self.array[i].priority > p.priority:  # 比插入元素大就向上移
                self.array[i + 1] = self.array[i]  # 不会数组越界是因为事先已经判断了队列是否isFull
            else:  # 比插入元素小时插入在i+1位置
                break
            i -= 1
        self.array[i + 1] = p

    def peek(self):
        if self.isEmpty():
            return None
        return self.array[self.size - 1]
    
    def poll(self):
        if self.isEmpty():
            return None
        e = self.array[self.size - 1]
        self.size -= 1
        # help GC
        self.array[self.size] = None
        return e


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
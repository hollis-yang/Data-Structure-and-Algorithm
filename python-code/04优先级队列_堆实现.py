from math import floor

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
    
    # O(logn)
    def offer(self, p):  # p -> class Priority
        if self.isFull():
            return False
        child = self.size  # 没加新元素之前，末尾位置就是size
        self.size += 1  # 整个操作完成size+1
        # 找到正确的插入位置
        parent = floor((child - 1) / 2)
        while child > 0 and p.priority > self.array[parent].priority:
            self.array[child] = self.array[parent]
            child = parent
            parent = floor((child - 1) / 2)
        # 此时的child就是新元素应该插入的位置
        self.array[child] = p
        return True

    def peek(self):
        if self.isEmpty():
            return None
        return self.array[0]
    
    # O(logn)
    def poll(self):
        if self.isEmpty():
            return None
        # 获取优先级最高的元素并删除
        self.swap(0, self.size - 1)
        self.size -= 1
        pmax = self.array[self.size]  # 需要返回的优先级最高元素
        self.array[self.size] = None  # help GC
        # 下潜: 使得root位置是剩下元素中优先级最高的
        self.down(0)
        return pmax
        
    def down(self, parent):
        # 左右孩子
        left = 2 * parent + 1
        right = left + 1
        max = parent  # 先假设父元素优先级最高
        # 获得自己与左右孩子中优先级最大的
        if left < self.size and self.array[left].priority > self.array[max].priority:  max = left
        if right < self.size and self.array[right].priority > self.array[max].priority:  max = right
        if max != parent:
            self.swap(max, parent)
            self.down(max)  # 以当前的max为父元素递归，一旦max==parent(没有孩子比父亲大/没有孩子时停止)
    
    # 交换队列中两个元素
    def swap(self, i, j):
        t = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = t


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
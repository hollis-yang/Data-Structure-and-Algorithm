class MaxHeap:
    def __init__(self, array):
        self.array = array
        self.size = len(self.array)
        self.heapify()  # 在初始化MaxHeap时就heapify
    
    def heapify(self):  # 建堆
        # 找最后一个非叶子节点 size>>1-1，从后向前执行下潜
        for i in range(self.size >> 1 - 1, -1, -1):
            self.down(i)
    
    def down(self, parent):  # 下潜
        left = parent * 2 + 1
        right = left + 1
        max = parent
        if left < self.size and self.array[left] > self.array[max]:  max = left
        if right < self.size and self.array[right] > self.array[max]:  max = right
        if max != parent:  # 有更大的孩子
            self.swap(max, parent)
            self.down(max)
    
    def swap(self, i, j):  # 交换堆中的两个元素
        t = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = t

    def peek(self):
        if self.size == 0:
            return None
        return self.array[0]
    
    def poll(self):
        if self.size == 0:
            return None
        self.swap(0, self.size - 1)
        self.size -= 1
        top = self.array[self.size]
        self.array[self.size] = None
        self.down(0)  # 下潜
        return top

    def poll(self, index):  # 删除指定位置的元素
        if index >= self.size:
            return None
        self.swap(index, self.size - 1)
        self.size -= 1
        pop = self.array[self.size]
        self.array[self.size] = None
        self.down(index)
        return pop

    def replace(self, value):  # 更换堆顶元素重新heapify
        if self.size == 0:
            return False
        self.array[0] = value
        self.down(0)
        return True
    
    def offer(self, offered):  # 堆尾新增元素(涉及上浮)
        if self.size == len(self.array):
            return False
        self.up(offered)
        self.size += 1
    
    def up(self, offered):  # 上浮
        child = self.size
        parent = int((child - 1) / 2)
        while child > 0 and offered > self.array[parent]:
            self.array[child] = self.array[parent]
            child = parent
            parent = int((child - 1) / 2)
        self.array[child] = offered

array = [1,2,3,4,5,6,7]
heap = MaxHeap(array)
print(heap.array)
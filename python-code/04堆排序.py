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


array = [5,9,7,3,1,58,16,74,32,19,8]
heap = MaxHeap(array)

# 堆排序代码
while heap.size > 1:
    heap.swap(0, heap.size - 1)  # 交换堆顶与堆底(将最大的移到堆底)
    heap.size -= 1
    heap.down(0)  # 重新确定最大的堆顶元素
print(heap.array)
# 小顶堆实现
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = MinHeap(nums[:k])
        for i in range(k, len(nums)):
            top = minheap.array[0]  # 堆顶元素
            num = nums[i]
            if num > top:
                minheap.replace(num)
        return minheap.array[0]


class MinHeap:  # 小顶堆
    def __init__(self, array):
        self.array = array
        self.size = len(self.array)
        self.heapify()  # 在初始化minHeap时就heapify
    
    def heapify(self):  # 建堆
        # 找最后一个非叶子节点 size>>1-1，从后向前执行下潜
        for i in range(self.size >> 1 - 1, -1, -1):
            self.down(i)
    
    def down(self, parent):  # 下潜
        left = parent * 2 + 1
        right = left + 1
        min = parent
        if left < self.size and self.array[left] < self.array[min]:  min = left
        if right < self.size and self.array[right] < self.array[min]:  min = right
        if min != parent:  # 有更大的孩子
            self.swap(min, parent)
            self.down(min)
    
    def swap(self, i, j):  # 交换堆中的两个元素
        t = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = t

    def replace(self, value):  # 更换堆顶元素重新heapify
        if self.size == 0:
            return False
        self.array[0] = value
        self.down(0)
        return True
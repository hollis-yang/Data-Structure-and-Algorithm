class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.array = [None] * k
        self.size = 0
        for num in nums:
            self.add(num)  # 如果堆不满k就offer, 满了就判断大小决定是否replace
    
    def down(self, parent):
        left = parent * 2 + 1
        right = left + 1
        min = parent
        if left < self.size and self.array[left] < self.array[min]:  min = left
        if right < self.size and self.array[right] < self.array[min]:  min = right
        if min != parent:  # 有更大的孩子
            # swap
            tmp = self.array[min]
            self.array[min] = self.array[parent]
            self.array[parent] = tmp
            self.down(min)

    def offer(self, offered):
        if self.size == len(self.array):
            return
        self.up(offered)
        self.size += 1
    
    def up(self, offered):
        child = self.size
        parent = int((child - 1) / 2)
        while child > 0 and offered < self.array[parent]:
            self.array[child] = self.array[parent]
            child = parent
            parent = int((child - 1) / 2)
        self.array[child] = offered

    def add(self, val: int) -> int:
        if self.size < len(self.array):
            self.offer(val)
        elif val > self.array[0]:
            self.array[0] = val
            self.down(0)
        return self.array[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
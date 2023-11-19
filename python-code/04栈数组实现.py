class ArrayStack:
    # 0->底部，idx越大->顶部(对右边的操作性能更高)
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.top = 0  # top索引不存元素
        self.capacity = capacity
    
    def push(self, value):
        # 1  2  3  4  5
        # 0  1  2  3  4  top
        if self.isFull():
            return False
        self.array[self.top] = value
        self.top += 1
        return True
    
    def pop(self):
        if self.isEmpty():
            return None
        first = self.array[self.top - 1]
        self.top -= 1
        return first
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.array[self.top - 1]
    
    def isFull(self):
        return self.top == self.capacity
    
    def isEmpty(self):
        return self.top == 0
    
    def __iter__(self):
        # 从顶(右侧)开始遍历
        p = self.top
        while p > 0:
            print(self.array[p - 1], end=' ')
            p -= 1
        print()


st = ArrayStack(3)
st.push(1)
st.push(2)
st.push(3)
print(st.pop())
st.__iter__()
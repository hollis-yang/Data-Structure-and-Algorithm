class Stack:
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, capacity):
        self.head = self.Node(None)  # 栈只需要操作栈顶，只需要一个指针就可以
        self.capacity = capacity
        self.size = 0
    
    def push(self, value):
        # head(s) -> 1 -> None
        if self.isFull():
            return False
        node = self.Node(value, self.head.next)
        self.head.next = node
        self.size += 1
        return True
    
    def pop(self):
        if self.isEmpty():
            return None
        first = self.head.next
        self.head.next = first.next
        self.size -= 1
        return first.value
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value
    
    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.head == None  # self.size==0
    
    def __iter__(self):
        p = self.head.next
        while p:
            print(p.value, end=' ')
            p = p.next
        print()

st = Stack(3)
st.push(1)
st.push(2)
st.push(3)
print(st.pop())
st.__iter__()
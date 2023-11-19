class MyQueue:
    '''
    a, b -> 模拟栈
    stack.append -> 压入栈
    pop -> 弹出栈
    a[-1] -> 获取栈顶元素
    '''
    def __init__(self):
        self.a = []
        self.b = []

    def push(self, x: int) -> None:
        self.b.append(x)

    def pop(self) -> int:
        if not self.a:
            while self.b:
                self.a.append(self.b.pop())
        return self.a.pop()
        
    def peek(self) -> int:
        if not self.a:
            while self.b:
                self.a.append(self.b.pop())
        return self.a[-1]

    def empty(self) -> bool:
        if self.a or self.b:
            return False
        return True




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
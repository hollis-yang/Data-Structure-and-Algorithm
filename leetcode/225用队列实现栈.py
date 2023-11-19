class MyStack:

    def __init__(self):
        self.a = []
        self.size = 0

    def push(self, x: int) -> None:
        self.a.append(x)
        self.size += 1
        for i in range(self.size - 1):
            self.a.append(self.a.pop(0))

    def pop(self) -> int:
        self.size -= 1
        return self.a.pop(0)

    def top(self) -> int:
        return self.a[0]

    def empty(self) -> bool:
        if self.a:
            return False
        return True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class Node:
    def __init__(self, prev, value, next):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedListCycleSentinel:
    def __init__(self):
        self.sentinel = Node(None, 666, None)
        # 初始化时哨兵节点的前后指针都指向自己
        self.sentinel.prev = self.sentinel
        self.sentinel.next = self.sentinel
    
    # 头插和尾插
    def add_first(self, value):
        a = self.sentinel
        b = self.sentinel.next
        node = Node(a, value, b)
        a.next = node
        b.prev = node
    def add_last(self, value):
        b = self.sentinel
        a = self.sentinel.prev  # 原来的最后一个节点
        node = Node(a, value, b)
        a.next = node
        b.prev = node
        
    # 头删和尾删
    def remove_first(self):
        remove = self.sentinel.next
        if remove == self.sentinel:
            raise Exception('No Enough Node in Cycled LinkedList')
        a = self.sentinel
        b = remove.next
        a.next = b
        b.prev = a
    def remove_last(self):
        remove = self.sentinel.prev
        if remove == self.sentinel:
            raise Exception('No Enough Node in Cycled LinkedList')
        a = remove.prev
        b = self.sentinel
        a.next = b
        b.prev = a
    
    # 找到值的对应节点的工具方法
    def find_by_value(self, value):
        p = self.sentinel.next
        while p != self.sentinel:
            if p.value == value:
                return p
            p = p.next
        return None
        
    # 根据值删除
    def remove_by_value(self, value):
        node = self.find_by_value(value)
        if node is None:
            raise Exception('Value Not Find')
        a = node.prev
        b = node.next
        a.next = b
        b.prev = a
    
    # 遍历(回到哨兵节点时停止)
    def loop(self):
        cur = self.sentinel.next
        while cur != self.sentinel:
            print(cur.value)
            cur = cur.next


ll = LinkedListCycleSentinel()
ll.add_last(1)
ll.add_last(2)
ll.add_last(3)
ll.add_last(4)
ll.add_last(5)
ll.remove_by_value(6)

ll.loop()
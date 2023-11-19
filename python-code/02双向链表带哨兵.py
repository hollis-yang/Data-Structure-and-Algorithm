class Node:
    def __init__(self, prev, value, next):
        self.value = value
        self.prev = prev
        self.next = next

class DoubleLinkedListSentinel:
    def __init__(self):
        # 两个哨兵
        self.head = Node(None, 666, None)
        self.tail = Node(None, 888, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    # 根据索引获取节点的工具方法
    def find_node(self, index):
        i = -1
        cur = self.head
        while cur != self.tail:
            if i == index:
                return cur
            cur = cur.next
            i += 1
        return None
    
    # 插入
    def insert(self, index, value):
        prev = self.find_node(index - 1)  # 前一个节点
        if prev is None:
            raise Exception('LinkedList index out of range')
        else:
            next = prev.next  # 后一个节点
            node = Node(prev, value, next)  # 创建新节点和前后指针
            # 改变原先两个节点的前后指针
            next.prev = node
            prev.next = node

    # 删除
    def remove(self, index):
        prev = self.find_node(index - 1)  # 前一个节点
        if prev is None:
            raise Exception('LinkedList index out of range')
        node = prev.next  # 要删除的节点
        if node == self.tail:  # 尾哨兵不能删除
            raise Exception('LinkedList index out of range')
        next = node.next  # 后一个节点
        # 改变前后指针
        prev.next = next
        next.prev = prev
        
    # 由于有了尾哨兵，在进行尾插和尾删时不再需要遍历
    def add_last(self, value):
        prev = self.tail.prev
        node = Node(prev, value, self.tail)
        prev.next = node
        self.tail.prev = node
    def remove_last(self):
        remove = self.tail.prev
        # 要remove的节点不能是头哨兵
        if remove == self.head:
            raise Exception('No Enough Node in LinkedList')
        prev = remove.prev
        prev.next = self.tail
        self.tail.prev = prev
    
    # 遍历
    def loop(self):
        cur = self.head.next
        while cur != self.tail:
            print(cur.value)
            cur = cur.next



# ll = DoubleLinkedListSentinel()
# ll.add_last(1)
# ll.add_last(2)
# ll.add_last(3)
# ll.add_last(4)
# ll.insert(4, 5)
# ll.remove_last()
# # ll.remove(7)
# ll.loop()
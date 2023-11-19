class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedListSentinel:
    def __init__(self):
        self.head = Node(666, None)  # 头节点为哨兵节点使得后续无需判断头节点是否为空

    # 获取尾节点
    def find_last(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        return cur
    # 尾插
    def add_last(self, value):
        last = self.find_last()
        last.next = Node(value, None)
    
    # 普遍的插入(此时不再需要单独的头插)
    def insert(self, index, value):
        pre = self.find_node(index - 1)  # 找到上一个节点
        if pre is None:  # 找不到说明index越界
            return 'LinkedList index out of range'
        else:
            pre.next = Node(value, pre.next)
    
    # 普通遍历  
    def loop(self):
        cur = self.head.next  # 带哨兵时遍历起点变了
        while cur:
            print(cur.value)
            cur = cur.next

    # 递归遍历
    def recursive_loop(self):
        pass

    # 根据索引获取节点及其值
    def find_node(self, index):
        i = -1  # 哨兵的index为-1
        cur = self.head
        while cur:
            if i == index:
                return cur
            cur = cur.next
            i += 1
        return None
    def get(self, index):
        node = self.find_node(index)
        if node:
            return node.value
        else:
            return 'LinkedList index out of range'

    # 根据索引删除(此时不再需要单独的头删)
    def remove(self, index):
        pre = self.find_node(index - 1)  # 上一个节点
        if pre is None:
            return 'LinkedList index out of range'
        remove = pre.next  # 被删除的节点
        if remove is None:  # 找到index的上一个节点(已经在链表尾了)但未找到需要删除的节点
            return 'LinkedList index out of range'
        pre.next = remove.next



ll = LinkedListSentinel()
ll.add_last(1)
ll.add_last(2)
ll.add_last(3)
ll.add_last(4)
print(ll.remove(2))
ll.loop()
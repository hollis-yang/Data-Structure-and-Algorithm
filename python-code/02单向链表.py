class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # 头插
    def add_first(self, value):
        # 1.链表为空
        # self.head = Node(value, None)
        # 2.链表非空
        self.head = Node(value, self.head)
    
    # 获取尾节点
    def find_last(self):
        if self.head is None:  # 防止none.next空指针报错
            return None
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            return cur
    # 尾插
    def add_last(self, value):
        last = self.find_last()
        if last is None:  # 空链表的情况尾插与头插相同
            self.add_first(value)
        else:
            last.next = Node(value, None)
    
    # 普遍的插入
    def insert(self, index, value):
        if index == 0:
            self.add_first(value)
        else:
            pre = self.find_node(index - 1)  # 找到上一个节点
            if pre is None:  # 找不到说明index越界
                return 'LinkedList index out of range'
            else:
                pre.next = Node(value, pre.next)
    
    # 普通遍历  
    def loop(self):
        cur = self.head
        while cur:
            print(cur.value, end=' ')
            cur = cur.next

    # 递归遍历
    def recursive_loop(self):
        self.recursion(self.head)
    def recursion(self, cur):
        if cur is None:
            return
        self.recursion(cur.next)

    # 根据索引获取节点及其值
    def find_node(self, index):
        i = 0
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

    # 头删
    def remove_first(self):
        if not self.head:
            return 'LinkedList is empty'
        else:
            self.head = self.head.next
    
    # 根据索引删除
    def remove(self, index):
        if index == 0:
            self.remove_first()
        else:
            pre = self.find_node(index - 1)  # 上一个节点
            if pre is None:
                return 'LinkedList index out of range'
            remove = pre.next  # 被删除的节点
            if remove is None:  # 找到index的上一个节点(已经在链表尾了)但未找到需要删除的节点
                return 'LinkedList index out of range'
            pre.next = remove.next
            
            

ll = LinkedList()
ll.add_last(1)
ll.add_last(2)
ll.add_last(3)
ll.add_last(4)
ll.recursive_loop()
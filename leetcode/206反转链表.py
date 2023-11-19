# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1.构造一个新链表，从旧链表依次拿到每个节点，创建新节点添加至新链表头部
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        p = None
        while cur:
            p = ListNode(cur.val, p)
            cur = cur.next
        return p

# 2.构造一个新链表，从旧链表头部移除节点，添加到新链表头部
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ll1 = LinkedList(head)
        ll2 = LinkedList()
        while True:
            node = ll1.removeFirst()
            if not node:
                break
            else:
                ll2.addFirst(node)
        return ll2.head

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def addFirst(self, first) -> ListNode:
        first.next = self.head
        self.head = first  # 新的头节点
        return first
    def removeFirst(self) -> ListNode:
        first = self.head
        if first:
            self.head = first.next
        return first

# 3.递归
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.findLast(head)
    def findLast(self, p):
        if p is None or p.next is None:
            return p  # 找最后的节点，也就是新的头节点
        last = self.findLast(p.next)
        # last永远是最后一个, p在时刻变化
        p.next.next = p
        p.next = None
        return last

# 4.把链表分成两部分，不断从链表2的头，往链表1的头搬移
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        n1 = head  # 反转后的头节点
        o1 = head
        o2 = head.next  # 此时需要处理的节点
        # 1->2->3->4->5
        while o2:
            o1.next = o2.next  # 1->3
            o2.next = n1  # 2->1
            n1 = o2
            o2 = o1.next
        return n1

# 5.把链表分成两部分，不断从链表2的头，往链表1的头搬移
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n1 = None  # 反转后的头节点
        o1 = head  # 1
        # 1->2->3->4->5
        while o1:
            o2 = o1.next  # 2
            o1.next = n1  # 1->None
            n1 = o1  # 1
            o1 = o2  # 2
        return n1
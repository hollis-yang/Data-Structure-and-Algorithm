# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1.两次扫描(最容易想到的方法)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 求链表长度
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        # 要删除的元素下标
        idx = count - n
        # 删除的代码
        dummy = ListNode(-1, head)
        pre = dummy
        cur = head
        i = 0  # 当前cur对应的index
        while cur:
            if i == idx:
                pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next
                i += 1
        return dummy.next

    # 2.快慢指针一次扫描
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = ListNode(-1, head)
        p1 = p2 = s
        # 要返回倒数第n个就让快指针p2先移动n次
        for i in range(n):
            p2 = p2.next
        # 同时移动p1,p2 当p2.next指向None时p1就是倒数第n个节点前一个节点
        while p2.next:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return s.next

    # 3.递归
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = ListNode(-1, head)
        self.findRecurion(s, n)
        return s.next
    def findRecurion(self, p, n):
        if p is None:
            return 0
        nth = self.findRecurion(p.next, n)  # 下一个节点的倒数位置
        if nth == n:
            p.next = p.next.next  # 改变当前节点的指针
        return nth + 1  # 当前节点的倒数位置
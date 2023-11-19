# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        s = ListNode(-1, head)
        pre = s
        cur = head  # 1

        # (-1->)1->2->3->4->5, k=2
        knode = self.calculateNumK(cur, k)  # 2
        while knode:
            fut = knode.next  # 3
            newhead, newtail = self.reverseList(cur, knode)  # 2->1
            pre.next = newhead  # (-1->)2->1
            newtail.next = fut  # (-1->)2->1->3->4->5
            pre = newtail  # 1
            cur = fut  # 3
            knode = self.calculateNumK(cur, k)  # 4
        return s.next

    # 反转链表 O(1)
    def reverseList(self, head, tail):
        pre = None
        cur = head
        while pre != tail:
            fut = cur.next
            cur.next = pre
            pre = cur
            cur = fut
        return pre, head  # 反转后的头和尾
    
    # 计算从某节点后第k个节点
    def calculateNumK(self, head, k):
        cur = head
        count = 1
        while cur:
            cur = cur.next
            count += 1
            if count == k:
                return cur
        return None
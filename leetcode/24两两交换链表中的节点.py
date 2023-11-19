# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        s = ListNode(-1, head)
        pre = s
        while cur and cur.next:  # cur->偶数个 cur.next->奇数个
            fut1 = cur.next  # 一定不是None
            fut2 = fut1.next  # 可能是None
            # 两两交换
            pre.next = fut1
            fut1.next = cur
            cur.next = fut2
            # 更新pre cur
            pre = cur
            cur = fut2
        return s.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 1.hashset O(m+n) O(m)
        s = set()
        cur = headA
        while cur:
            s.add(cur)
            cur = cur.next
        p = headB
        while p:
            if p in s:
                return p
            p = p.next
        return None
      
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 2.双指针 O(m+n) O(1)
        p1 = headA
        p2 = headB
        while True:
            if p1 == p2:
                return p1
            else:
                if p1:
                    p1 = p1.next
                else:
                    p1 = headB
                if p2:
                    p2 = p2.next
                else:
                    p2 = headA
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1.递归
    def deleteDuplicates(self, p: Optional[ListNode]) -> Optional[ListNode]:
        if p == None or p.next == None:
            return p
        if p.val == p.next.val:
            cur = p.next.next
            while cur:
                if cur.val == p.val:
                    cur = cur.next
                else:
                    return self.deleteDuplicates(cur)
        else:
            p.next = self.deleteDuplicates(p.next)
            return p

    # 2.一次遍历
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
    
        s = ListNode(-999, head)
        pre = s
        cur = fut = head
        while fut and fut.next:
            fut = cur.next
            if cur.val != fut.val:
                pre = cur
                cur = fut
            else:
                p = fut.next
                while p:
                    if p.val == fut.val:
                        p = p.next
                    else:
                        break
                pre.next = p
                cur = fut = p
        return s.next
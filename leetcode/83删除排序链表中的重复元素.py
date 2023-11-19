# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1.双指针
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = fut = head
        while fut:
            fut = fut.next
            if fut == None or cur.val != fut.val:
                cur.next = fut
                cur = fut
        return head

    # 2.递归
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        if head.val == head.next.val:
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
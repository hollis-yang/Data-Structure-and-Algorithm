# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1.哨兵
    
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        s = ListNode(-1, head)
        pre = s
        cur = head
        while cur:
            if cur.val == val:
                # 删除节点，仅后移cur
                pre.next = cur.next
            else:
                # 继续遍历，cur/pre都后移
                pre = cur
            cur = cur.next
        return s.next
    
    # 2.递归
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        else:
            fut = self.removeElements(head.next, val)
            if head.val != val:
                head.next = fut
                return head
            else:
                return fut

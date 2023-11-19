# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        self.heap = [None] * len(lists)  # 小顶堆中最多只有链表个数的节点
        self.size = 0
        for linkedlist in lists:
            if linkedlist:  # 如果链表不为空则加入heap
                self.offer(linkedlist)
        sentinel = ListNode(-9999, None)
        cur = sentinel
        while self.size > 0:  # 当堆不为空时不断执行
            min = self.poll()
            if min.next:
                self.offer(min.next)
            cur.next = min
            cur = min      
        return sentinel.next

    
    def offer(self, node):
        child = self.size
        self.size += 1
        parent = int((child - 1) / 2)
        while child > 0 and node.val < self.heap[parent].val:
            self.heap[child] = self.heap[parent]
            child = parent
            parent = int((child - 1) / 2)
        self.heap[child] = node
    
    def poll(self):
        self.swap(0, self.size - 1)
        self.size -= 1
        pmin = self.heap[self.size]  # 优先级最低的
        self.heap[self.size] = None
        self.down(0)
        return pmin

    def down(self, parent):
        left = 2 * parent + 1
        right = left + 1
        min = parent
        if left < self.size and self.heap[left].val < self.heap[min].val:  min = left
        if right < self.size and self.heap[right].val < self.heap[min].val:  min = right
        if min != parent:
            self.swap(min, parent)
            self.down(min)
    
    def swap(self, i, j):
        t = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = t
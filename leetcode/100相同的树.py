# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = [p]
        queue2 = [q]
        while queue1:
            if len(queue1) != len(queue2):
                return False
            for i in range(len(queue1)):
                node1 = queue1.pop(0)
                node2 = queue2.pop(0)
                print(node1, node2)
                if node1 is None and node2 is None:
                    continue
                if node1 is None or node2 is None or node1.val != node2.val:
                    return False
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
        return True

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.check(p, q)

    def check(self, p, q):
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        else:
            if p.val != q.val:
                return False
            return self.check(p.left, q.left) and self.check(p.right, q.right)
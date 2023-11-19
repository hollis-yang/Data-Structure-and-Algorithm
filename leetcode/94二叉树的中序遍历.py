# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.recursion(root)
        return self.res
    
    def recursion(self, node):
        if node:
            self.recursion(node.left)
            self.res.append(node.val)
            self.recursion(node.right)

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.insert(0, cur)
                cur = cur.left
            else:
                pop = stack.pop(0)
                res.append(pop.val)
                cur = pop.right
        return res
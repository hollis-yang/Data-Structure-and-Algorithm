# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.recursion(root)
        return self.res
    
    def recursion(self, node):
        if node:
            self.res.append(node.val)
            self.recursion(node.left)
            self.recursion(node.right)


# 迭代
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.insert(0, cur)
                cur = cur.left
            else:
                pop = stack.pop(0)
                cur = pop.right
        return res
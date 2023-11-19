# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.recursion(root)
        return self.res
    
    def recursion(self, node):
        if node:
            self.recursion(node.left)
            self.recursion(node.right)
            self.res.append(node.val)

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        cur = root
        pop = None
        while cur or stack:
            if cur:
                stack.insert(0, cur)
                cur = cur.left
            else:
                peek = stack[0]
                if peek.right == None or peek.right == pop:
                    pop = stack.pop(0)
                    res.append(pop.val)
                else:
                    cur = peek.right
        return res
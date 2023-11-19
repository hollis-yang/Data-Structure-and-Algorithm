# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS后序（递归版）
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursion(root)
    
    def recursion(self, node):
        if node == None:
            return 0
        else:
            left_depth = self.recursion(node.left)  # 左子树深度
            right_depth = self.recursion(node.right)  # 右子树深度
            return max(left_depth, right_depth) + 1  # 要加上本层的深度

# DFS后序（非递归版）
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        cur = root
        pop = None
        stack = []
        max = 0  # 最大深度 -> 也就是栈中元素最多
        while cur or stack:
            if cur:
                stack.insert(0, cur)
                if max < len(stack):
                    max = len(stack)
                cur = cur.left
            else:
                peek = stack[0]
                if peek.right == None or peek.right == pop:
                    pop = stack.pop(0)
                else:
                    cur = peek.right
        return max

# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1  # 每次遍历完一层深度+1
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# DFS后序（递归版）
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursion(root)
    
    def recursion(self, node):
        if node == None:
            return 0
        else:
            left_depth = self.recursion(node.left)  # 左子树深度
            right_depth = self.recursion(node.right)  # 右子树深度
            if left_depth == 0 or right_depth == 0:  # 有一个子树为None其实是不算深度的
                return left_depth + right_depth + 1
            else:
                return min(left_depth, right_depth) + 1

# BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1  # 每次遍历完一层深度+1
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left == None and node.right == None:  # 判断是否是叶子节点
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return -1
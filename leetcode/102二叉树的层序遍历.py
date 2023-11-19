# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []
        queue = [root]  # 根节点初始入队 
        while queue:
            one_level_list = []  # 存一层内的值
            num = len(queue)  # 该层有几个不是None的节点
            for i in range(num):
                node = queue.pop(0)
                one_level_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(one_level_list)
        return res
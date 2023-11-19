# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        deque = [root]  # 双端队列
        num = 1  # 第一层
        while deque:
            one_level_list = []
            size = len(deque)  # 每层的遍历次数
            
            for i in range(size):
                popnode = None
                if num % 2 == 1:  # 奇数层(遍历方向->)
                    popnode = deque.pop(0)
                    if popnode.left: 
                        deque.append(popnode.left)
                    if popnode.right: 
                        deque.append(popnode.right)
                else:  # 偶数层(遍历方向<-)
                    popnode = deque.pop()
                    if popnode.right: 
                        deque.insert(0, popnode.right)
                    if popnode.left: 
                        deque.insert(0, popnode.left)
                one_level_list.append(popnode.val)
                
            res.append(one_level_list)
            num += 1
        return res

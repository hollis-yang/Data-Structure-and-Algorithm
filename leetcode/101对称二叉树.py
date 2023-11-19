# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # BFS+队列
        if root.left == None and root.right == None:
            return True
        elif root.left == None or root.right == None:
            return False
        queue = [root.left, root.right]
        while queue:
            res = []
            num = len(queue)
            for i in range(num):
                node = queue.pop(0)
                if node == None:
                    res.append(None)
                    continue
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            # check res是否对称
            print(res)
            i = 0
            j = len(res) - 1
            while i < j:
                if res[i] == res[j]:
                    i += 1
                    j -= 1
                    continue
                else:
                    return False
        return True

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)

    def check(self, left, right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            # 左右都不为空
            if left.val != right.val:
                return False
            return self.check(left.left, right.right) and self.check(left.right, right.left)
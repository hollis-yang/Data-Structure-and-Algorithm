# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        p = root
        while p:
            if p.val < val:
                p = p.right
            elif p.val > val:
                p = p.left
            else:
                return p
        return None
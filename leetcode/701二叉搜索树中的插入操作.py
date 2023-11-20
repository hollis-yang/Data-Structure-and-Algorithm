# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        p = root
        parent = None
        while p:
            parent = p
            if p.val < val:
                p = p.right
            else:
                p = p.left
        node = TreeNode(val)
        if val > parent.val:
            parent.right = node
        else:
            parent.left = node
        return root
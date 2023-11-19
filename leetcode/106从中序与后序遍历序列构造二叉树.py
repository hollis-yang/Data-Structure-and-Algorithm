# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root_value = postorder[len(postorder) - 1]
        root = TreeNode(root_value)
        for i in range(len(inorder)):
            if inorder[i] == root_value:
                root.left = self.buildTree(inorder[0:i], postorder[0:i])
                root.right = self.buildTree(inorder[i+1:], postorder[i:len(postorder) - 1])

                break
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:  # 留一个就行因为preorder和inorder的长度一定相等
            return None

        # 从前序获得root
        root_value = preorder[0]
        root = TreeNode(root_value)
        # 借助root和中序划分左右子树
        for i in range(len(inorder)):
            if inorder[i] == root_value:
                # 0~i-1 -> 左子树；i -> root；i+1~len(inorder) -> 右子树
                in_left = inorder[0:i]
                in_right = inorder[i+1:]

                # 前序遍历拆分左右子树
                pre_left = preorder[1: i+1]
                pre_right = preorder[i+1:]

                # 递归
                root.left = self.buildTree(pre_left, in_left)
                root.right = self.buildTree(pre_right, in_right)

                break  # 找到了整个树的root就可以break了
        return root
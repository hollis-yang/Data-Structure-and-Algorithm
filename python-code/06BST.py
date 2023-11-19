class BSTNode:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
class BST:
    def __init__(self):
        self.root = None
    
    
    # 查找关键字对应的值
    def get(self, key):
        return self.do_get(self.root, key)
    
    def do_get(self, node, key):
        # 每次找的逻辑是相同的，因此封装递归
        if not node:
            return None  # 没找到
        if key < node.key:  # 向左找
            self.do_get(node.left, key)
        elif key > node.key:  # 向右找
            self.do_get(node.right, key)
        else:
            return node.value
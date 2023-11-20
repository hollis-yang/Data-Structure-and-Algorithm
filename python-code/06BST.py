class BSTNode:
    def __init__(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
class BST:
    def __init__(self):
        self.root = None
    
    
    # 查找关键字对应的值(递归版)
    def get_recursion(self, key):
        return self.do_get(self.root, key)
    
    def do_get(self, node, key):
        # 每次找的逻辑是相同的，因此封装递归
        if not node:
            return None  # 没找到
        if key < node.key:  # 向左找
            return self.do_get(node.left, key)
        elif key > node.key:  # 向右找
            return self.do_get(node.right, key)
        else:
            return node.value


    # 查找关键字对应的值(非递归版)
    def get_norecur(self, key):
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                return node.value
        return None


    # 查找最小关键字对应值
    def min_recursion(self):
        return self.do_min(self.root)

    def do_min(self, node):
        if node is None:
            return None
        if node.left is None:
            return node.value
        return self.do_min(node.left)

    def min_norecur(self):
        if self.root is None:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.value
    
    
    # 查找最大关键字对应值
    def max_recursion(self):
        return self.do_max(self.root)

    def do_max(self, node):
        if node is None:
            return None
        if node.right is None:
            return node.value
        return self.do_max(node.right)

    def max_norecur(self):
        if self.root is None:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.value

    
    # 新增
    def put(self, key, value):
        # 查找是否已经在BST中
        parent = None  # 记录父节点
        node = self.root
        while node:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                # 相当于找到了, 进行key的替换
                node.value = value
                return 
        # 没有找到
        node = BSTNode(key, value)
        if parent is None:  # 树为空时
            self.root = node
            return
        if key < parent.key:
            parent.left = node
        else:  # 不可能相等
            parent.right = node
    
    
    # 查关键字的前驱值
    def predecessor(self, key):
        ancestor_left = None
        p = self.root
        while p:
            if key < p.key:
                p = p.left
            elif key > p.key:
                ancestor_left = p
                p = p.right  # 代表祖先自左而来
            else:
                break
        # 如果没找到，那肯定不存在前驱
        if p is None:
            return None
        # 下面是找到的情况
        # 情况1：节点有左子树，此时前驱节点就是左子树的最大值
        if p.left:
            return self.do_max(p.left)
        # 情况2：节点没有左子树，此时前驱节点是其祖先节点中第一个比它小的节点
        return ancestor_left.value if ancestor_left else None


    # 查关键字的后继值
    def successor(self, key):
        ancestor_right = None
        p = self.root
        while p:
            if key < p.key:
                ancestor_right = p
                p = p.left  # 代表祖先自右而来
            elif key > p.key:
                p = p.right  
            else:
                break
        # 如果没找到，那肯定不存在后继
        if p is None:
            return None
        # 下面是找到的情况
        # 情况1：节点有右子树，此时后继节点即为右子树的最小值
        if p.left:
            return self.do_min(p.right)
        # 情况2：节点没有右子树，若离它最近的祖先自从右而来，此祖先即为后继
        return ancestor_right.value if ancestor_right else None
    
    
    # 删除(非递归)
    def delete(self, key):
        # 先找到待删除节点并记录parent
        parent = None
        p = self.root
        while p:
            if key < p.key:
                parent = p
                p = p.left
            elif key > p.key:
                parent = p
                p = p.right
            else:
                break
        # 如果没找到，那没法删除
        if p is None:
            return None
        # 执行删除操作
        # 情况1：删除节点没有左孩子
        if p.left == None:
            self.shift(parent, p, p.right)
        # 情况2：删除节点没有右孩子
        elif p.left != None:
            self.shift(parent, p, p.left)
        # 情况3：删除节点没有孩子(已包含在情况1/情况2中)
        # 情况4：删除节点有左右孩子
        else:
            # 1 (在右子树中)找被删除节点的后继节点
            s = p.right  # 后继节点
            sparent = p  # 后继节点的父节点
            while s.left:
                sparent = s
                s = s.left
            # 2 如果删除节点和后继节点不相邻，需要处理后继节点的后事(右子树)
            # 做的操作其实就是删除后继节点
            if sparent != p:
                self.shift(sparent, s, s.right)  # 一定是s.right，否则s不是后继
            # 3 后继取代被删除节点
            self.shift(parent, p, s)
            s.left = p.left  # 考虑顶上去节点的左子树
        return p.value
            
    # 托孤
    def shift(self, parent, deleted, child):
        if parent is None:
            self.root = child
        elif deleted == parent.left:
            parent.left = child
        elif deleted == parent.right:
            parent.right = child
    
    
    # 删除(递归)
    def delete_recursion(self, key):
        result = []  # 保存被删除节点的值
        self.root = self.do_delete(self.root, key, result)
        if result:
            return result[0]
        return None

    def do_delete(self, node, key, result):
        # node -> 起点
        # return -> 删剩下的孩子 or None
        if node is None:
            return None
        if key < node.key:
            node.left = self.do_delete(node.left, key, result)
            return node
        if key > node.key:
            node.right = self.do_delete(node.right, key, result)
            return node
        result.append(node.value)
        # 情况1：只有右孩子
        if node.left is None:
            return node.right
        # 情况2：只有左孩子
        if node.right is None:
            return node.left
        # 情况3：两个孩子
        # 找后继节点
        s = node.right
        while node.left:
            s = s.left
        # 处理不相邻的情况
        s.right = self.do_delete(node.right, s.key, [])
        s.left = node.left
        return s
    
    
    # 找所有比 key 小的 value、
    def less(self, key):
        result = []
        p = self.root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                pop = stack.pop()
                # 处理值
                if pop.key < key:
                    result.append(pop.value)
                else:
                    break
                p = pop.right
        return result

    # 找所有比 key 大的 value
    def greater(self, key):
        result = []
        p = self.root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                pop = stack.pop()
                # 处理值
                if pop.key > key:
                    result.append(pop.value)
                p = pop.right
        return result

    # 找所有比 key 大的 value(update 反中序遍历)
    def greater_update(self, key):
        result = []
        p = self.root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.right
            else:
                pop = stack.pop()
                # 处理值
                if pop.key > key:
                    result.append(pop.value)
                else:
                    break
                p = pop.left
        return result
    
    # 找 >= key1 & <= key2的所有 value
    def between(self, key1, key2):
        result = []
        p = self.root
        stack = []
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                pop = stack.pop()
                # 处理值
                if pop.key <= key2 and pop.key >= key1:
                    result.append(pop.value)
                if pop.key > key2:
                    break
                p = pop.right
        return result
    
    
# 测试
# n1 = BSTNode(1, 'a')
# n3 = BSTNode(3, 'c')
# n2 = BSTNode(2, 'b', n1, n3)
# n5 = BSTNode(5, 'e')
# n7 = BSTNode(7, 'g')
# n6 = BSTNode(6, 'f', n5, n7)
# root = BSTNode(4, 'd', n2, n6)
bst = BST()
# bst.root = root
# bst.put(1, 'a')
# bst.put(3, 'c')
# bst.put(2, 'b')
# bst.put(5, 'e')
# bst.put(7, 'g')
# bst.put(6, 'f')
# bst.put(4, 'd')


# print(bst.get_recursion(1))
# print(bst.get_recursion(2))
# print(bst.get_recursion(3))
# print(bst.get_recursion(4))
# print(bst.get_recursion(5))
# print(bst.get_recursion(6))
# print(bst.get_recursion(7))
# print(bst.get_recursion(8))

# print(bst.get_norecur(1))
# print(bst.get_norecur(2))
# print(bst.get_norecur(3))
# print(bst.get_norecur(4))
# print(bst.get_norecur(5))
# print(bst.get_norecur(6))
# print(bst.get_norecur(7))
# print(bst.get_norecur(8))

# print(bst.min_recursion())
# print(bst.min_norecur())
# print(bst.max_recursion())
# print(bst.max_norecur())

# print(bst.predecessor(7))
# print(bst.successor(6))

n1 = BSTNode(1, 1)
n3 = BSTNode(3, 3)
n2 = BSTNode(2, 2, n1, n3)
n5 = BSTNode(5, 5)
n6 = BSTNode(6, 6, n5)
n7 = BSTNode(7, 7, n6)
root = BSTNode(4, 4, n2, n7)
bst.root = root

# bst.delete_recursion(5)
# bst.delete_recursion(6)
# print(bst.get_norecur(6))
print(bst.less(6))
print(bst.greater(5))
print(bst.greater_update(5))
print(bst.between(3, 5))
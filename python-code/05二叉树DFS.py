class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5), TreeNode(6)))

# pre-order递归
def pre_order(node):
    if node == None:
        return
    print(node.val, end=' ')
    pre_order(node.left)
    pre_order(node.right)

# in-order递归
def in_order(node):
    if node == None:
        return
    in_order(node.left)
    print(node.val, end=' ')
    in_order(node.right)

# post-order递归
def post_order(node):
    if node == None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.val, end=' ')


# pre_order(root)
# print()
# in_order(root)
# print()
# post_order(root)


# 无论哪种遍历，走的路是一样的，用栈来记录父节点
''' 前中序遍历
stack = []
cur = root  # 当前节点
while cur or stack:
    if cur:
        print('去', cur.val)  # 前序
        stack.append(cur)
        cur = cur.left
    else:
        pop = stack.pop()
        print('回', pop.val)  # 中序
        cur = pop.right
'''

''' 后序遍历
stack = []
pop = None  # 最近一次弹栈的元素
cur = root  # 当前节点
while cur or stack:
    if cur:
        stack.append(cur)
        cur = cur.left
    else:
        # 获取栈顶元素
        peek = stack[len(stack) - 1]
        # 判断右子树是否处理完成
        if peek.right == None or peek.right == pop:  # 本身没有右子树 or 右子树是上一个弹栈的
            pop = stack.pop()
            print(pop.val, end=' ')
        else:
            cur = peek.right
'''

stack = []
pop = None  # 最近一次弹栈的元素
cur = root  # 当前节点
while cur or stack:
    if cur:
        stack.append(cur)
        # print(cur.val, end=' ')  # 前序(在处理左前输出)
        # 待处理左子树
        cur = cur.left
    else:
        peek = stack[len(stack) - 1]
        # 本身没有右子树
        if peek.right == None:
            print(stack[len(stack) - 1].val, end=' ')  # 中序(在处理完左 且 没有右时输出) 
            pop = stack.pop()
            # print(pop.val, end=' ')  # 后序(在处理完右/没有右后输出)
        # 右子树处理完成
        elif peek.right == pop:
            pop = stack.pop()
            # print(pop.val, end=' ')  # 后序(在处理完右/没有右后输出)
        # 待处理右子树
        else:
            print(stack[len(stack) - 1].val, end=' ')  # 中序(在处理完左 且 未开始处理右时输出)
            cur = peek.right
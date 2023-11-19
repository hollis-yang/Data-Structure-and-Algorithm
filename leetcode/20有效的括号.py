class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # 模拟栈
        left = ['(', '[', '{']
        right = [')', ']', '}']
        for i in s:
            if i in left:  # 如果是左就把右压入栈
                stack.append(right[left.index(i)])
            else:  # 如果是右就与栈顶元素比较，相等则闭合(同时如果栈内无元素也一定不闭合)
                if stack and stack[-1] == i:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False
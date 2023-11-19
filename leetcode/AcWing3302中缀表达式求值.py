# 中缀表达式转后缀表达式
def infixToSuffix(str):
    stack = []
    suffix = []
    for i in str:
        if i not in '+-*/()':
            suffix.append(i)
        elif i == '(':  # 左括号直接入栈
            stack.append(i)
        elif i == ')':  # 遇到右括号就把栈内直到第一个左括号为止的元素全部弹出
            first = stack[-1]
            while first != '(':
                suffix.append(stack.pop())
                first = stack[-1]
            # (此时没用了
            stack.pop()
        else:
            # 如果栈为空，直接把运算符压入栈
            if not stack:
                stack.append(i)
            # 栈不是空的话，和栈顶元素比较优先级
            else:
                # 获取当前元素和栈顶元素的优先级
                priority = operator_priority(i)
                priority_stack = operator_priority(stack[-1])
                if priority > priority_stack:
                    stack.append(i)
                else:
                    # 要把所有比该运算符优先级高 / 相等的都出栈
                    while stack and priority <= operator_priority(stack[-1]):  # 前提:栈内有元素
                        suffix.append(stack.pop())
                    stack.append(i)
    # 循环结束腾空栈
    if stack:
        while stack:
            suffix.append(stack.pop())
    return suffix


# 定义优先级
def operator_priority(c):
    if c == '*' or c == '/':
        return 2
    elif c == '+' or c == '-':
        return 1
    elif c == '(':
        return 0
    else:
        return -1


# 计算后缀表达式
def evalRPN(tokens):
    stack = []
    operators = ['+', '-', '*', '/']
    for i in tokens:
        if i not in operators:
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()
            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))
    return stack[0]


# print(evalRPN(infixToSuffix(str(input()))))
print(evalRPN(infixToSuffix('(2+3*4-8)*4')))
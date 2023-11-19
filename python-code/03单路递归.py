def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

# print(fact(0))


def reverse_print(s, index):
    if index == len(s):
        return
    reverse_print(s, index + 1)
    print(s[index])

# reverse_print('abcde', 0)


def binary_search(a, target):
    return recursion(a, target, 0, len(a)-1)

def recursion(a, target, i, j):
    if i > j:
        return -1
    m = i + j >> 1
    if a[m] > target:
        return recursion(a, target, i, m - 1)
    elif a[m] < target:
        return recursion(a, target, m + 1, j)
    else:
        return m

# a = [7, 13, 21, 30, 38, 44, 52, 53]
# print(binary_search(a, 13))
# print(binary_search(a, 1))


def bubble_sort1(a, j):  # j是未排序区域的右边界
    if j == 0:
        return
    for i in range(0, j):
        # 比较i和i+1索引的两个元素
        if a[i] > a[i + 1]:
          tmp = a[i]
          a[i] = a[i + 1]
          a[i + 1] = tmp
    bubble_sort1(a, j - 1)

# a = [6, 4, 1, 7, 8, 12]
# bubble_sort1(a, len(a)-1)
# print(a)

def bubble_sort2(a, j):
    if j == 0:
        return
    x = 0  # 设置一个x来区分已排序/未排序减少不必要的递归
    for i in range(0, j):
        if a[i] > a[i + 1]:
          tmp = a[i]
          a[i] = a[i + 1]
          a[i + 1] = tmp
          x = i
    bubble_sort2(a, x)
    
# a = [6, 4, 1, 7, 8, 12]
# bubble_sort2(a, len(a)-1)
# print(a)


def insert_sort1(a, low):  # low是未排序区域的左边界
    if low == len(a):
        return
    tmp = a[low]  # 临时变量存储low位置的值用于后续比较
    i = low - 1  # 已排序区域的右边界
    
    # 从右向左找，第一个比tmp小的就是插入位置
    while a[i] > tmp and i >= 0:
        a[i + 1] = a[i]  # 右移一位空出插入位置
        i -= 1
    if i + 1 != low:  # low是被插入区域里最大的时不需要执行插入
        a[i + 1] = tmp  # 插入
    
    insert_sort1(a, low + 1)

# a = [6, 4, 1, 7, 8, 12]
# insert_sort1(a, 1)
# print(a)


def insert_sort2(a, low):  # low是未排序区域的左边界
    if low == len(a):
        return
    
    i = low - 1
    while i >= 0 and a[i] > a[i + 1]:
        # 交换a[i],a[i+1]
        t = a[i]
        a[i] = a[i + 1]
        a[i + 1] = t
        i -= 1
    
    insert_sort2(a, low - 1)  # 每次保证了最后一位是最大的
    
a = [6, 4, 1, 7, 8, 12]
insert_sort2(a, 1)
print(a)
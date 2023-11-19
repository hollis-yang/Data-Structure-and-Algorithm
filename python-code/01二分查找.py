# 基础版
def binary_search1(a, target) -> int:
    i, j = 0, len(a) - 1
    while i <= j:
        m = (i + j) >> 1
        if target < a[m]:
            j = m - 1
        elif target > a[m]:
            i = m + 1
        else:
            return m
    return -1


# 改动版
def binary_search2(a, target) -> int:
    i, j = 0, len(a)  #  j指向的不是查找目标
    while i < j:
        m = (i + j) >> 1
        if target < a[m]:
            j = m
        elif target > a[m]:
            i = m + 1
        else:
            return m
    return -1


# 平衡版
def binary_search3(a, target) -> int:
    i, j = 0, len(a)
    while 1 < j - i:  # 范围内待查找的元素个数
        m = (i + j) >> 1
        if target < a[m]:
            j = m
        else:
            i = m
    if target == a[i]:
        return i
    else:
        return -1


# 返回某元素第一次出现的位置 leftmost
def binary_search_left(a, target) -> int:
    i, j = 0, len(a) - 1
    candidate = -1
    while i <= j:
        m = (i + j) >> 1
        if target < a[m]:
            j = m - 1
        elif target > a[m]:
            i = m + 1
        else:
            candidate = m  # 记录候选位置
            j = m - 1  # 缩小右侧边界
    return candidate


# 返回某元素最后一次出现的位置 rightmost
def binary_search_right(a, target) -> int:
    i, j = 0, len(a) - 1
    candidate = -1
    while i <= j:
        m = (i + j) >> 1
        if target < a[m]:
            j = m - 1
        elif target > a[m]:
            i = m + 1
        else:
            candidate = m  # 记录候选位置
            i = m + 1  # 缩小左侧边界
    return candidate


# leftmost的修改 -> 返回>=target的最靠左的元素位置
def binary_search_left2(a, target) -> int:
    i, j = 0, len(a) - 1
    while i <= j:
        m = (i + j) >> 1
        if target <= a[m]:
            j = m - 1
        elif target > a[m]:
            i = m + 1
    if a[i] == target:
        return i
    else:
        return -i
    

# rightmost的修改 -> 返回<=target的最靠右的元素位置
def binary_search_right2(a, target) -> int:
    i, j = 0, len(a) - 1
    while i <= j:
        m = (i + j) >> 1
        if target < a[m]:
            j = m - 1
        elif target >= a[m]:
            i = m + 1
    if a[i] == target:
        return i - 1
    else:
        return -(i - 1)
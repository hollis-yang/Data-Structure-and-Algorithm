def YangHuiTriangle(i, j):  # 行列都从0开始
    if j == 0 or i == j:
        return 1
    return YangHuiTriangle(i - 1, j - 1) + YangHuiTriangle(i - 1, j)

# print(YangHuiTriangle(4, 2))


def print_yht(n):
    for i in range(n):
        print(' ' * (n - 1 - i) * 2, end='')
        for j in range(i + 1):
            print(YangHuiTriangle(i, j), end='   ')
        print()

# print_yht(5)


def YangHuiTriangle_memorization(i, j, triangle):
    if triangle[i][j] > 0:
        return triangle[i][j]
    else:
        if j == 0 or i == j:
            triangle[i][j] = 1
            return 1
        triangle[i][j] = YangHuiTriangle_memorization(i - 1, j - 1, triangle) + YangHuiTriangle_memorization(i - 1, j, triangle)
        return triangle[i][j]


def print_yht_memorization(n):
    triangle = [[]] * n  # n行
    for i in range(n):
        triangle[i] = [0] * (i + 1)
        print(' ' * (n - 1 - i) * 2, end='')
        for j in range(i + 1):
            print(YangHuiTriangle_memorization(i, j, triangle), end='   ')
        print()

# print_yht_memorization(5)


def create_row(row, i):
    if i == 0:
        row[0] = 1
        return
    # 生成第i行用的是第i-1行数据
    for j in range(i, 0, -1):  # 每一行的元素个数=最后一个元素下标+1=行号+1
        row[j] = row[j] + row[j - 1]

def print_yht_modify(n):
    row = [0] * n
    for i in range(n):  # 行号i
        create_row(row, i)  # 生成这一行的数据
        print(' ' * (n - 1 - i) * 2, end='')
        for j in range(i + 1):  # 打印每行的元素个数i+1
            print(row[j], end='   ')
        print()

print_yht_modify(5)


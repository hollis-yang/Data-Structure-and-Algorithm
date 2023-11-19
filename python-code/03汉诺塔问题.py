def init(n):
    for i in range(n, 0, -1):
        a.append(i)

def hanoi(n, a, b, c):
    if n == 0:
        return
    else:
        # step1:把n-1个圆盘a->b
        hanoi(n - 1, a, c, b)
        
        # step2:把最后的盘子a->c
        disk = a.pop()
        c.append(disk)
        print_hanoi()
        
        # step3:把n-1个圆盘b->c
        hanoi(n - 1, b, a, c)

def print_hanoi():
    print("-----------------------")
    print("A:", a)
    print("B:", b)
    print("C:", c)

a = []
b = []
c = []

init(3)
print_hanoi()
hanoi(3, a, b, c)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# print(fibonacci(8))


def fibonacci_memorization(n):
    # 记忆数组
    cache = [-1] * (n + 1)  # 用-1代表未计算的，因为f(n)的值也会存入，因此开辟n+1个位置
    # 前两项认为是已知的
    cache[0] = 0
    cache[1] = 1
    return f(n, cache)

def f(n, cache):
    if cache[n] != -1:
        return cache[n]
    else:
        x = f(n - 1, cache)
        y = f(n - 2, cache)
        cache[n] = x + y
        return cache[n]

for i in range(2, 14):
    print(fibonacci_memorization(i), end=' ')
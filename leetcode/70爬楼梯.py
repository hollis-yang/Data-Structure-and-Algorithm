class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n + 1)  # 存f(0)...f(n)共n+1个位置
        cache[0] = cache[1] = 1
        return self.f(n, cache)
    # 普通斐波那契(TLE)
    '''
    def f(self, n):
        if n == 1 or n == 0:
            return 1
        return self.f(n-1) + self.f(n-2)
    '''
    # 记忆化递归
    def f(self, n, cache):
        if cache[n] != -1:
            return cache[n]
        else:
            x = self.f(n - 1, cache)
            y = self.f(n - 2, cache)
            cache[n] = x + y
            return cache[n]
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = []
        for i in range(0, rowIndex + 1):
            res.append(1)  # 每一行的最后一定是1
            # 按上一行的结果倒着生成这一行
            for j in range(i-1, 0, -1):
                res[j] = res[j] + res[j - 1]
        return res
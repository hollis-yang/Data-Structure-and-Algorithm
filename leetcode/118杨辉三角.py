class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            data = [1]
            for j in range(1, i + 1):
                try:
                    data.append(res[i - 1][j - 1] + res[i - 1][j])
                except IndexError:
                    data.append(res[i - 1][j - 1])
            res.append(data)
        return res
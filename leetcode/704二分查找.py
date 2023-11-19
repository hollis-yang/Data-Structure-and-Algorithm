class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1 基础版
        i, j = 0, len(nums) - 1
        while i <= j:
            m = i + j >> 1
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                return m
        return -1
        # 2 改动版
        i, j = 0, len(nums)
        while i < j:
            m = i + j >> 1
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m
            else:
                return m
        return -1
        # 3 平衡版
        i, j = 0, len(nums)
        while 1 < j - i:  # 范围内待查找的元素个数
            m = i + j >> 1
            if target < nums[m]:
                j = m
            else:
                i = m
        if target == nums[i]:
            return i
        else:
            return -1
        
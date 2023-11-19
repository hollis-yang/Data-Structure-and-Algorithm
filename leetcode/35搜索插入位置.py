class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 改进的leftmost
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) >> 1
            if target <= nums[m]:
                j = m - 1
            elif target > nums[m]:
                i = m + 1
        return i
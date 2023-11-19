class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.leftmost(nums, target)
        if left == -1:
            return [-1, -1]
        else:
            return [left, self.rightmost(nums, target)]
    
    def leftmost(self, nums, target):
        i, j = 0, len(nums) - 1
        candidate = -1
        while i <= j:
            m = (i + j) >> 1
            if target < nums[m]:
                j = m - 1
            elif target > nums[m]:
                i = m + 1
            else:
                candidate = m
                j = m - 1
        return candidate
    
    def rightmost(self, nums, target):
        i, j = 0, len(nums) - 1
        candidate = -1
        while i <= j:
            m = (i + j) >> 1
            if target < nums[m]:
                j = m - 1
            elif target > nums[m]:
                i = m + 1
            else:
                candidate = m
                i = m + 1
        return candidate

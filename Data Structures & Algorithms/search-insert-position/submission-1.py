class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        if nums[r-1] < target:
            return r
        if nums[0] > target:
            return l

        while l < r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m
            elif nums[m] > target:
                r = m
            else:
                return m
            
            if r - l == 1:
                return l+1
        
        return (l+r) // 2
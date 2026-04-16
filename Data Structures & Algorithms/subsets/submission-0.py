class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sub = [], []
        def backtrack(index):
            if index >= len(nums):
                res.append(sub.copy())
                return
            
            # Include
            sub.append(nums[index])
            backtrack(index+1)

            # Not include
            sub.pop()
            backtrack(index+1)
        backtrack(0)
        return res
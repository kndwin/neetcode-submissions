class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sub = [], []
        def backtrack(idx):
            if sum(sub) == target:
                res.append(sub.copy())
            
            if idx >= len(nums) or sum(sub) >= target:
                return

            # Include same number
            sub.append(nums[idx])
            backtrack(idx)
            # Not include number, move to next number
            sub.pop()
            backtrack(idx+1)

        backtrack(0)
        return res

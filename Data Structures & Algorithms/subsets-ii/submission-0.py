class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sub, dic = [], [], {}
        def backtrack(idx):
            if idx >= len(nums) and str(sorted(sub)) not in dic:
                res.append(sub.copy())
                dic[str(sorted(sub).copy())] = True
                return
            if idx >= len(nums):
                return
            
            sub.append(nums[idx])
            backtrack(idx+1)
            sub.pop()
            backtrack(idx+1)
        backtrack(0)
        return res
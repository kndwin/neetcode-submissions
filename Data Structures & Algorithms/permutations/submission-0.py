class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur, rem):
            if len(rem) == 0:
                res.append(cur.copy())
                return
            
            for idx, val in enumerate(rem):
                backtrack(cur + [val], rem[:idx] + rem[idx+1:])

        backtrack([], nums)
        return res

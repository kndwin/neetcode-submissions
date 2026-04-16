class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sub, can = [], [], sorted(candidates)

        def backtrack(idx):
            if sum(sub) == target:
                res.append(sub.copy())
            
            if sum(sub) >= target or idx >= len(can):
                return

            sub.append(can[idx])
            backtrack(idx+1)
            sub.pop()
            
            newIdx = idx
            while newIdx < len(can)-1 and can[newIdx] == can[newIdx+1]:
                newIdx += 1
            backtrack(newIdx+1)
        backtrack(0)
        return res
        
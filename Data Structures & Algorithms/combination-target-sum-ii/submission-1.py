class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sub, can = [], [], sorted(candidates)
        def backtrack(idx, cur_sum):
            if cur_sum == target:
                res.append(sub.copy())
            
            if cur_sum >= target or idx >= len(can) or can[idx] > target:
                return

            sub.append(can[idx])
            backtrack(idx+1, cur_sum + can[idx])
            sub.pop()
            newIdx = idx
            while newIdx < len(can)-1 and can[newIdx] == can[newIdx+1]:
                newIdx += 1
            backtrack(newIdx+1, cur_sum)

        backtrack(0, 0)
        return res
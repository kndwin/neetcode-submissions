class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        res, seen, l, r = False, { nums[0]: 1}, 0, 1
        while r < len(nums):
            new = nums[r]
            if seen.get(new) is None or seen.get(new) == 0:
                r += 1
                seen[new] = 1
            else:
                if nums[l] == new and r-l <= k:
                    res = True
                    break
                else:
                    if nums[l] == new:
                        seen[new] -= 1
                    l += 1

        return res
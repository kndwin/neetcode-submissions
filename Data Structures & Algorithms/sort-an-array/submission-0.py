class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sortLoop, idx = True, 0
        while sortLoop:
            if idx == len(nums)-1:
                sortLoop = False
                break

            if nums[idx] > nums[idx+1]:
                findPos, j = True, idx+1
                while findPos:
                    if j == 0:
                        findPos = False
                        break
                    if nums[j] < nums[j-1]:
                        tmp = nums[j]
                        nums[j] = nums[j-1]
                        nums[j-1] = tmp
                        j -= 1
                    else:
                        findPos = False
                        break
            idx += 1
        return nums
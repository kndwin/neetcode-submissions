class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ls = len(nums)
        l = 0
        
        while l < ls:
            if nums[l] == 0:

                # stop if only zeros left
                if sum(nums[l:]) == 0:
                    l = ls
                    break
                # move to end
                shift, j = True, l
                while shift:
                    if j == ls-1:
                        shift = False
                        break
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
                    j += 1
            else:
                l += 1
        
        return nums
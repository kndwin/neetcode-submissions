class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Loop through each number and 2 pointer the other set
        results = []
        nums.sort()
        for idx in range(len(nums)-2):
            target = -nums[idx]
            remain = nums[idx+1:]
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            left, right = 0, len(remain)-1
            while left < right:   
                if (remain[left] + remain[right] > target):
                    right = right - 1
                elif (remain[left] + remain[right] < target):
                    left = left + 1
                else:
                    results.append([remain[left], remain[right], -target])
                    left = left + 1
                    right = right - 1
                        # Skip duplicates AFTER moving pointers
                    while left < right and remain[left] == remain[left-1]:
                        left += 1
                    while left < right and remain[right] == remain[right+1]:
                        right -= 1
        return results

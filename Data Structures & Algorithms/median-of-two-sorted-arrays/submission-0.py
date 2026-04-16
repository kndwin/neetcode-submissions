class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # WRONG: You swapped the variables in reverse order
        
        m, n = len(nums1), len(nums2)
        total = m + n  # WRONG: You never defined 'total'
        half = (m + n + 1) // 2  # WRONG: Your calculation didn't account for 0-indexing properly
        
        left, right = 0, m  # WRONG: You used len(nums1)-1, but we need to consider m elements
        
        while left <= right:
            partition1 = (left + right) // 2  # WRONG: You used int((l1+r1)/2) instead of integer division
            partition2 = half - partition1  # WRONG: Your calculation of second partition was off
            
            # WRONG: You didn't handle edge cases where partition is at the boundary
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # WRONG: Your comparison logic was incorrect and didn't handle boundaries
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Found the correct partition
                if total % 2 == 1:
                    # WRONG: You returned nums2[half-m1] without checking which max is larger
                    return max(maxLeft1, maxLeft2)
                else:
                    # WRONG: Your calculation was completely off - you need max of left and min of right
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                # partition1 is too big, need to go left
                right = partition1 - 1
            else:
                # partition1 is too small, need to go right
                left = partition1 + 1
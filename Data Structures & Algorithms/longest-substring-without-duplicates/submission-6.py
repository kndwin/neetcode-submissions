class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        if len(s) == 1: return 1
        left, right, currSet, longest = 0,1,{ s[0]: 0 },0
        while right < len(s):
            newChar = s[right]
            if newChar in currSet:
                left = max(currSet[newChar]+1, left)
            currSet[newChar] = right
            longest = max(longest, right - left + 1)
            right += 1
        return longest 
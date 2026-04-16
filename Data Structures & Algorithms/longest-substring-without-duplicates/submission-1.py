class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        longest, l, w = 0, 0, set()
        for r in range(len(s)):
            while s[r] in w:
                w.remove(s[l])
                l += 1
            w.add(s[r])
            longest = max(longest, len(w))
        return longest
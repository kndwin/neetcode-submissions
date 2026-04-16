class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, freq, window = 0, 0, {}
        for right in range(len(s)):
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1
            freq = max(freq, window[s[right]])
            if (right - left + 1) - freq > k:
                window[s[left]] -= 1
                left += 1
            
        return right - left + 1
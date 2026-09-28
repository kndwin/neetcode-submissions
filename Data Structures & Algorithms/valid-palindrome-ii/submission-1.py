class Solution:
    def validPalindrome(self, s: str) -> bool:

        if self.palindrome(s):
            return True
        
        for i in range(len(s)):
            word = s[:i] + s[i+1:]
            if self.palindrome(word):
                return True
        
        return False
        
    def palindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True
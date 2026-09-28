class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ls = len(s)
        for i in range(ls//2):
            tmp = s[i]
            s[i] = s[ls-i-1]
            s[ls-i-1] = tmp
        
        
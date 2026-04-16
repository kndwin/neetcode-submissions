class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        included = False
        charMap = { char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
        s1m = charMap.copy()
        
        for char in s1:
            s1m[char] += 1
        
        totalS1sum = 0
        for count in s1m.values():
            totalS1sum += count
        
        for right in range(len(s1), len(s2)+1):
            subset = s2[right-len(s1):right]
            
            s2m = charMap.copy()
            
            for char in subset:
                s2m[char] += 1

            if s1m == s2m:
                included = True
                break

        return included
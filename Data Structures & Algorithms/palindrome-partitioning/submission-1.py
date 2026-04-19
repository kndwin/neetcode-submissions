class Solution:
    def partition(self, s: str) -> List[List[str]]:
        total, seen = [], set()
        def isPalindrome(word):
            if word in seen:
                return True
            for i in range(len(word) // 2):
                if word[i] != word[-i-1]:
                    return False
            seen.add(word)
            return True

        def dfs(left, curr):
            if left == len(s):
                total.append(curr)
                return
            
            for i in range(len(s) - left):
                word = s[left:left+i+1]
                if isPalindrome(word):
                    dfs(left+i+1, curr + [word])
            
        dfs(0, [])
        return total
                

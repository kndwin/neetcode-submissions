class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        total = []
        d2c = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6" :"mno", "7": "pqrs", "8": "tuv", "9": "wxyz", "0": "+"}

        def dfs(height, curr):
            if height == len(digits):
                total.append(curr)
                return
            
            for char in d2c[digits[height]]:
                dfs(height+1, curr + char)
        dfs(0,"")
        return total


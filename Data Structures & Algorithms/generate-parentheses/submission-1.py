class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        total = []
        def dfs(curr):
            nonlocal total
            l, r = curr.count("("), curr.count(")")
            if l == n and r == n:
                total.append(curr)
                return
            if l == n:
                return dfs(curr+")")
            if r>l:
                return
            dfs(curr+")")
            dfs(curr+"(")
        dfs("")
        return total
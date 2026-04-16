class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sub = [], []
        def backtrack(open_count, closed_count):
            if open_count == closed_count == n:
                res.append("".join(sub))
            if open_count < n:
                sub.append("(")
                backtrack(open_count+1, closed_count)
                sub.pop()
            if closed_count < open_count:
                sub.append(")")
                backtrack(open_count, closed_count+1)
                sub.pop()
        backtrack(0,0)
        return res
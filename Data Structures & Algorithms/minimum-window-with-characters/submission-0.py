class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        have, need = dict(), dict(Counter(t))
        bestLeft, bestRight = -1, -1

        while right < len(s):
            curr = s[right]
            if have.get(curr):
                have[curr] += 1
            else:
                have[curr] = 1

            while all(have.get(char, 0) >= count for char, count in need.items()):
                if bestLeft == -1:
                    bestLeft, bestRight = left, right
                elif right-left < bestRight-bestLeft:
                    bestLeft, bestRight = left, right
                
                curr = s[left]
                if have.get(curr) > 1:
                    have[curr] -= 1
                else:
                    del have[curr]
                left += 1
            right += 1

        if bestLeft == -1:
            return ""

        return s[bestLeft:bestRight+1]
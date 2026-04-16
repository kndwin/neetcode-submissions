class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r, bl, br = 0, 0, None, None
        h, n = {}, Counter(t)
        hc, nc = 0, len(n)

        while r < len(s):
            c = s[r]
            h[c] =  h.get(c, 0) + 1

            if c in n and h[c] == n[c]:
                hc += 1
            
            while hc == nc:

                if bl == None or (r-l<br-bl):
                    bl, br = l, r
                c = s[l]
                if c in n and h[c] == n[c]:
                    hc -= 1
                
                h[c] -= 1
                l += 1
            r += 1
        
        return "" if bl is None else s[bl:br+1]

        
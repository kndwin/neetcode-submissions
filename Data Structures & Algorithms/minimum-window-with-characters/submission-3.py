class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        best_left, best_right = -1, -1
        have, need = {}, Counter(t)
        have_count, need_count = 0, len(need)

        while right < len(s):
            curr = s[right]
            have[curr] = have.get(curr, 0) + 1

            if curr in need and have[curr] == need[curr]:
                have_count += 1
            
            while have_count == need_count:
                if best_left == -1 or (right-left < best_right-best_left):
                    best_left, best_right = left, right
                curr = s[left]

                if curr in need and have[curr] == need[curr]:
                    have_count -= 1
                have[curr] -= 1
                left += 1
            
            right += 1
        return "" if best_left == -1 else s[best_left:best_right+1]

            
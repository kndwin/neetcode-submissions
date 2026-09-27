class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        should_loop, idx = True, 0
        while should_loop:
            curr = self.getChar(strs[0], idx)

            if curr is None:
                should_loop = False
                break
            
            for word in strs:
                char = self.getChar(word, idx)
                if char is None or char != curr:
                    should_loop = False
                    break

            if should_loop:
                idx += 1

        if idx > 0:
            return strs[0][0:idx]

        return ""
    
    def getChar(self, string: str, index: int):

        if len(string) < index+1:
            return None

        if len(string) == 1:
            return string
        
        return string[index]
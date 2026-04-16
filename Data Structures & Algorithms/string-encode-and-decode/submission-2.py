class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += f"^{len(s)}@{s}"
        return string

    def decode(self, s: str) -> List[str]:
        array, i = [], 0
        while i < len(s):
            j = i + 1
            while s[j] != '@': 
                j += 1
            length = int(s[i+1:j])
            word = s[j+1:j+1+length]
            array.append(word)
            i = j + 1 + length
        return array 
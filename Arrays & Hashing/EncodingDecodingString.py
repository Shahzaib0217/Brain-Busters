class Solution:
    
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            # Finding #
            while s[j] != '#':
                j += 1
            # Retrieving the str length number
            length = int(s[i:j])
            # pointing i to the char next to #
            i = j + 1
            # J pointing at the end of str
            j = i + length
            # Appending str to response
            res.append(s[i:j])
            # i pointing at the end of str
            i = j
            
        return res
class Solution:

    def encode(self, strs: List[str]) -> str:
        wrd = ""
        for i in strs:
            l = len(i)
            wrd += str(l) + '#' + i
        return wrd
        # 4#neet4code422love3you

    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        i = 0
        while i < len(s):
            if s[i] == '#':
                num = int(s[start:i])
                res.append(s[i + 1 : i + num + 1]) 
                i += num 
                start = i + 1
            i += 1
        return res 

            

            
            

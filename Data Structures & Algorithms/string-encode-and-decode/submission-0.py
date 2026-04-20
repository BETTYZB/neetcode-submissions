class Solution:

  

    def encode(self, strs: List[str]) -> str:
        s = ''
        for wrd in strs:
            s += str(len(wrd)) + "#" + wrd
        return s

    def decode(self, s: str) -> List[str]:
        pre = 0
        a = 0
        res = []
        # s = 1w2oo7abcdefg
        while a < len(s):
            pre = a
            while s[a] != "#":
                a += 1

            l = int(s[pre:a]) + 1
            
            res.append(s[a + 1:a + l])
            a += l

        return res
            


        

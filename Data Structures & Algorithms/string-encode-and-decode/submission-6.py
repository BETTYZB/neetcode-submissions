class Solution:

    def encode(self, strs: List[str]) -> str:
        wrd_hash = ''
        for wrd in strs:
            wrd_hash = wrd_hash + str(len(wrd)) + ':' + wrd

        return wrd_hash


    def decode(self, s: str) -> List[str]:
        res = []
        start = 0
        num = 0
        i = 0
        while i < len(s):
            if s[i] == ':':
                num = int(s[start:i])
                res.append(s[i + 1 : num + i + 1])
                start = num + i + 1
                i += num

            i += 1
            
        return res

    


            

            
            

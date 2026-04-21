class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyzxyz
        dict_alph = {}
        if len(s) < 2:
            return len(s)
            
        l, r = 0, 1
        length = 1
        dict_alph[s[l]] = l
        while r < len(s):
            if s[r] in dict_alph:
                l = dict_alph[s[r]] + 1
                dict_alph = {}
                dict_alph[s[l]] = l
                r = l
            else:
                dict_alph[s[r]] = r
            r += 1
            length = max(length, r - l)

        return length


        
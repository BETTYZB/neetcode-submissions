class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_frq = defaultdict(int)
        l, r = 0 , 0
        frq = 0
        max_len = 0
        while r < len(s):
            dict_frq[s[r]] += 1
            frq = max(frq, dict_frq[s[r]])
            while ((r - l + 1) - frq) > k:
                dict_frq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1

        return max_len

            


    
                




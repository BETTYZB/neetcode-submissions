class Solution:
    def isValid(self, s: str) -> bool:
        # {[(()]}
        dict_pa = {"{":"}", "(":")", "[":"]"}
        stck = []
        for i in s:
            if i in ("}", ")", "]"):
                if stck:
                    val = stck.pop()
                    if i != dict_pa[val]:
                        return False
                else:
                    return False
            else:
                stck.append(i)
        if stck:
            return False
        return True
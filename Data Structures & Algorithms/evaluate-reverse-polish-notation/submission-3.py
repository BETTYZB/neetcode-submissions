class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []
        pre = 0
        post = 0
        for i in tokens:
            if i not in ("+", "-", "*", "/"):
                stck.append(int(i))
            else:
                post = stck.pop()
                pre = stck.pop()

                if i == "+":
                    stck.append(post + pre)
                elif i == "*":
                    stck.append(post * pre)
                elif i == "/":
                    stck.append(int(pre / post))
                elif i == "-":
                    stck.append(pre - post)


        return stck[0]
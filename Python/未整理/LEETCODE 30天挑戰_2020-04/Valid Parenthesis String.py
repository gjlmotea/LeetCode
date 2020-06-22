class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        hi = 0
        for c in s:
            if c == '(':
                lo += 1
            else:
                lo -= 1

            if c != ')':
                hi += 1
            else:
                hi -= 1

            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0


##print(Solution().checkValidString("()"))
##print(Solution().checkValidString("(*)"))
##print(Solution().checkValidString("****"))
##print(Solution().checkValidString("****("))
##print(Solution().checkValidString("****())"))
print(Solution().checkValidString("(*()"))


class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi +=1
            elif c == ')':
                lo -= 1
                hi -= 1
            elif c == '*':
                hi += 1
            
            if hi < 0:
                return False
            if lo < 0:
                lo = 0

        if lo == 0:
            return True

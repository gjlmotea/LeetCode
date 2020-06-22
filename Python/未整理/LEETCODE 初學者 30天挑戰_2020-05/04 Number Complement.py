# 與 1009同題目
# https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, num: int) -> int:
        numList = [] 
        while num != 0:
            if num % 2 == 0:
                numList.append(1)
            else:
                numList.append(0)
            num = num // 2
        ans = 0
        
        for n in reversed(numList):
            ans = ans * 2 + n
        return ans


print(Solution().bitwiseComplement(5))
print(Solution().bitwiseComplement(10))
print(Solution().bitwiseComplement(15))


import math
class Solution:
    def findComplement(self, num: int) -> int:
        a="{0:b}".format(num)
        b=str(a)
        listr=[]
        for i in b:
            if i=='1':
                listr.append(0)
            elif i=='0':
                listr.append(1)
        res = "".join(map(str, listr)) 
        return (int(res,2))


class Solution:
    def findComplement(self, num: int) -> int:
        if num == 1:
            return 0
        else:
            return 2**(int(log2(num))+1)-1 - num

class Solution:
    def findComplement(self, N: int) -> int:
        X = 1
        while N > X: 
            X = X * 2 + 1
        return X - N

class Solution:
    def findComplement(self, num: int) -> int:
        return (1 << num.bit_length()) - 1 - num if num else 1

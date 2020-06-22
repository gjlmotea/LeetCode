class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 2147483647 = ，2進位 1111111111111111111111111111111 (32個1)
        val = [1] * 32
        for v in val:
            print(v)
            #還沒想出來
        return val
        


print(Solution().rangeBitwiseAnd(5,7))
print(Solution().rangeBitwiseAnd(0,1))
print(Solution().rangeBitwiseAnd(0,2147483647))

#### 超時 8256 / 8266 test cases passed.
##class Solution:
##    def rangeBitwiseAnd(self, m: int, n: int) -> int:
##        val = n
##        for i in range(m, n):
##            val = val & i
##        return val
##        


## 最佳解
##def rangeBitwiseAnd(m, n):
##    k = 0
##    while n != m:
##        n >>= 1
##        m >>= 1
##        k += 1
##    return n << k

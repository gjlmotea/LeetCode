class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 0
        while n * n <= num:
            if n * n == num:
                return True
            n += 1
        return False


print(Solution().isPerfectSquare(16))
print(Solution().isPerfectSquare(14))
print(Solution().isPerfectSquare(1))

## 超時
##class Solution:
##    def isPerfectSquare(self, num: int) -> bool:
##        for i in range(num // 2 + 2):
##            if num == i * i:
##                return True
##        return False


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while(r >= l):
            mid = int((l + r) / 2)
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                r = mid - 1
            else:
                l = mid + 1
        return False

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = num**0.5
        if a == int(a):
            return True
        else:
            return False

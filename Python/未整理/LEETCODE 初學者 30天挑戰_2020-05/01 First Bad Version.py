class Solution:
    def firstBadVersion(self, n):
        l = 1
        r = n
        ans = -1
        
        while l <= r:
            #m = l + (r-l) // 2
            m = (l + r) // 2
            if isBadVersion(m):
                r = m - 1
                ans = m
            else:
                l = m + 1
        return ans

print(Solution().firstBadVersion(5))





#暴力法
##class Solution:
##    def firstBadVersion(self, n):
##        for i in range(n+1):
##            if isBadVersion(i):
##                return i
##
##print(Solution().firstBadVersion(5))


##
##import bisect
##class Solution():
##    def firstBadVersion(self, n):
##        """
##        :type n: int
##        :rtype: int
##        """
##        self.__getitem__ = isBadVersion
##        return bisect.bisect_left(self, True, 1, n)


##class Solution:
##    def firstBadVersion(self, n):
##        #A Different implementation of Binary Search where Right Pointer is Exclusive
##        l=1; r=n+1 #1st Change, Now 'r' becomes 'n+1'
##        ans = -1
##        while l<r:#2nd Change , No more equality
##            mid = l + (r-l)//2
##            if isBadVersion(mid):
##                ans = mid
##                r=mid #3rd Change, 'r' now moves to mid
##            else:
##                l=mid+1
##        return ans

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        findAns = False
        while True:
             
            
        return -1
                

print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 3))


## 笨方法但居然可以過
##class Solution:
##    def search(self, nums: List[int], target: int) -> int:
##        for n, num in enumerate(nums):
##            if num == target:
##                return n
##        return -1


##class Solution:
##    def search(self, nums: List[int], target: int) -> int:
##        n = len(nums)
##
##        def find(l, r):
##            if l > r:
##                return -1
##            if nums[l] <= nums[r]:
##                if nums[l] <= target <= nums[r]:
##                    # binary search here
##                    while l <= r:
##                        m = (l + r) // 2
##                        if target == nums[m]:
##                            return m
##                        elif target > nums[m]:
##                            l = m+1
##                        else:
##                            r = m-1
##                return -1
##            elif target >= nums[l] or target <= nums[r]:
##                # divide and conquer
##                m = (l + r) // 2
##                return max(find(l, m), find(m+1, r))
##            return -1
##
##        return find(0, n-1)

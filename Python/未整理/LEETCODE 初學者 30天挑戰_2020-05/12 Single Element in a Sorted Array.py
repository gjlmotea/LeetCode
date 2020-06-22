from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sum(set(nums))*2-sum(nums)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while True:
            mid = (low + high) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid < high and nums[mid] == nums[mid+1]:
                low = mid + 2
            elif mid > low and nums[mid] == nums[mid-1]:
                high = mid - 2
            else:
                return nums[mid]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = {}
        for num in nums:
            if num in N:
                N[num] += 1
            else:
                N[num] = 1
            if N[num] == 2:
                del N[num]
        for k in N:
            return k

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        t = nums[0]
        for i in range(1, len(nums)):
            t = t ^ nums[i]
        return t

print(Solution().singleNonDuplicate([1,1,2,3,3,4,4,8,8]))

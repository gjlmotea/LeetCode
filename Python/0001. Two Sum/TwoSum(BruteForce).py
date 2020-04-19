from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return j, i



## Test
'''
nums = [2,7,11,15]
target = 9
print(Solution().twoSum(nums, target))  #0, 1
'''

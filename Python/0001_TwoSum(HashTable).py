from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        
        for i in range(len(nums)):
            if (target-nums[i]) in numsDict.keys() :
                return numsDict[target-nums[i]], i
            numsDict[nums[i]] = i


## 測試
#nums = [10, 30, 30, 20, 40, 50]
#target = 60
#a = Solution
#print(Solution.twoSum(object(), nums, target))

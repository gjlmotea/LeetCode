class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] + nums[j] == target:
                    return j, i
        

## 測試
## nums = [2,7,11,15]
## target = 9

## print(Solution.twoSum(None, nums, target))

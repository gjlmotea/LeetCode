from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        windowSum = nums[0]
        maxSum = nums[0]
        for num in nums:
            windowSum = max(windowSum + num, num)
            maxSum = max(maxSum, windowSum)
        #print(maxSum)
        return maxSum


Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
Solution().maxSubArray([-10000, 2, 3, 4, 5, -10, 999])
Solution().maxSubArray([-10, 11, -3, 5])    #13

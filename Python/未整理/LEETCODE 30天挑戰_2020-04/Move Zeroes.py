from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        z = 0
        #紀錄目前數值為0的個數
        p = 0
        #紀錄目前已填非0數字的point

        while p + z < len(nums):
            if nums[p+z] == 0:
                z += 1
            else:
                nums[p] = nums[p+z]
                p += 1
        for i in range(p, len(nums)):
            nums[i] = 0
            
        

        print(nums)

Solution().moveZeroes([0,1,0,3,12]) #1, 3, 12, 0, 0

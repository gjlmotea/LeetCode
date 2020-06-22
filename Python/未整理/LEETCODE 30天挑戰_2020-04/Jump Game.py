from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        numLen = len(nums)
        boolList = ["F"] * numLen
        boolList[0] = 'T'
        for i in range(len(nums)):
            for j in range(nums[i]):
                if i + j < numLen:
                    boolList[i + j] = 'T'
                    
            
            
        print(boolList)
        if boolList[len(nums) -1 ] == 'T':
            return True
        else:
            return False
        

print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([2,1,1,0,4]))
print(Solution().canJump([1,1,1,1,1]))
print(Solution().canJump([1,2,3]))
print(Solution().canJump([3,2,1,0,4]))
